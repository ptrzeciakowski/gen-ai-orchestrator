/*
 * samsung-duplex-wrapper.c
 * Universal CUPS filter wrapper for Samsung M2020/M2026 Series Manual Duplex on macOS.
 *
 * Automatically translates standard macOS / CUPS print dialog settings:
 *   - Duplex=DuplexNoTumble / sides=two-sided-long-edge -> SECManualDuplexOption=LongEdge
 *   - Duplex=DuplexTumble   / sides=two-sided-short-edge -> SECManualDuplexOption=ShortEdge
 *   - Duplex=None           / sides=one-sided           -> SECManualDuplexOption=None
 *   - (Default on duplex queue)                         -> SECManualDuplexOption=LongEdge
 *
 * In CUPS, argv[0] is set to the PRINTER NAME (e.g. "Samsung_M2026W_Duplex"), NOT the filter binary name!
 * Therefore, we determine the target either via compile-time TARGET_FILTER or runtime _NSGetExecutablePath().
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <libgen.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <mach-o/dyld.h>

#ifndef TARGET_FILTER
#define TARGET_FILTER ""
#endif

#define REAL_PREFILTER   "/Library/Printers/Samsung/UPD/Filters/prefilter"
#define REAL_RASTERTOSEC  "/Library/Printers/Samsung/UPD/Filters/rastertosec"
#define CACHE_FILE       "/Library/Caches/com.sec.printer"

static void ensure_cache_file(void) {
    int fd = open(CACHE_FILE, O_RDWR | O_CREAT, 0666);
    if (fd >= 0) {
        fchmod(fd, 0666);
        close(fd);
    }
}

int main(int argc, char *argv[]) {
    if (argc < 6) {
        fprintf(stderr, "ERROR: samsung-duplex-wrapper called with insufficient arguments (argc=%d)\n", argc);
        return 1;
    }

    const char *target = TARGET_FILTER;

    // If not set at compile time, detect target via actual binary path
    if (strlen(target) == 0) {
        char exec_path[1024];
        uint32_t size = sizeof(exec_path);
        if (_NSGetExecutablePath(exec_path, &size) == 0) {
            char *bname = basename(exec_path);
            if (strstr(bname, "prefilter") != NULL) {
                target = REAL_PREFILTER;
            } else if (strstr(bname, "raster") != NULL) {
                target = REAL_RASTERTOSEC;
            }
        }
    }

    // Safety fallback
    if (strlen(target) == 0) {
        if (strstr(argv[0], "prefilter") != NULL) {
            target = REAL_PREFILTER;
        } else {
            // Default to prefilter if still uncertain
            target = REAL_PREFILTER;
        }
    }

    // Ensure cache file exists and is world-writable
    ensure_cache_file();

    // Ensure critical environment variables are set to prevent prefilter null-pointer crashes
    if (!getenv("CONTENT_TYPE")) {
        setenv("CONTENT_TYPE", "application/pdf", 1);
    }
    if (!getenv("PPD")) {
        setenv("PPD", "/private/etc/cups/ppd/Samsung_M2026W_Duplex.ppd", 1);
    }

    const char *orig_opts = argv[5];
    char new_opts[8192];
    new_opts[0] = '\0';

    if (strstr(orig_opts, "SECManualDuplexOption") != NULL) {
        // Option is already explicitly provided
        snprintf(new_opts, sizeof(new_opts), "%s", orig_opts);
    } else {
        // Detect standard macOS / IPP duplex attributes
        int is_none = (strstr(orig_opts, "Duplex=None") != NULL ||
                       strstr(orig_opts, "sides=one-sided") != NULL ||
                       strstr(orig_opts, "PMDuplexing..n.=1") != NULL);

        int is_tumble = (strstr(orig_opts, "Duplex=DuplexTumble") != NULL ||
                         strstr(orig_opts, "sides=two-sided-short-edge") != NULL ||
                         strstr(orig_opts, "PMDuplexing..n.=3") != NULL ||
                         strstr(orig_opts, "DuplexBindingEdge..n.=3") != NULL);

        if (is_none) {
            snprintf(new_opts, sizeof(new_opts), "%s SECManualDuplexOption=None", orig_opts);
        } else if (is_tumble) {
            snprintf(new_opts, sizeof(new_opts), "%s SECManualDuplexOption=ShortEdge", orig_opts);
        } else {
            // Default on this duplex queue: LongEdge
            snprintf(new_opts, sizeof(new_opts), "%s SECManualDuplexOption=LongEdge", orig_opts);
        }
    }

    // Allocate new argv
    char **new_argv = malloc((argc + 1) * sizeof(char *));
    if (!new_argv) {
        perror("malloc");
        return 1;
    }
    for (int i = 0; i < argc; i++) {
        new_argv[i] = argv[i];
    }
    // argv[0] must be preserved (printer name for CUPS)
    new_argv[5] = new_opts;
    new_argv[argc] = NULL;

    execv(target, new_argv);

    perror("execv failed");
    return 1;
}
