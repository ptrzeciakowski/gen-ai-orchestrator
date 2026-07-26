## Context

This project initializes the `gen-ai-orchestrator` repository, which serves as an orchestration layer for Generative AI agents. 
The system aims to be AI tool-agnostic with local shell scripting capabilities and integrated seamlessly with the Open Spec framework. Current state is established with directory structure under `.ai/` and symlinks in `.agents/`.

## Goals / Non-Goals

**Goals:**
- Establish a single source of truth for repository structure and agent requirements via `README.md`.
- Implement a clear layout matching `.ai/agents`, `.ai/skills`, and `.ai/tools` with backwards compatible `.agents/` symlinks.
- Automate Open Spec integration (e.g. automatic `README.md` appending tooling).

**Non-Goals:**
- Creating actual, domain-specific AI agents or skills within this initial foundation phase.
- Integrating GUI capabilities or non-terminal bindings.

## Decisions

- **Agnostic directory (.ai)**: Separates AI logic into generic structure rather than pinning to a specific framework (e.g. `.claude/` or `.cursor/`).
- **Symlinks for compatibility (.agents)**: Keeps compatibility with legacy or strictly structured internal tools that expect `.agents` without duplicating configurations.
- **OpenSpec as primary alignment (openspec/changes/)**: Changes to the orchestrator layer must be logged as explore/proposal changes inside Open Spec to maintain traceability and align with https://openspec.dev/ principles.
- **Bash tooling for automated appending**: Using `openspec-update-readme.sh` provides native terminal compatibility, avoiding complex runtime dependencies for simple text-appending tasks.

## Risks / Trade-offs

- [Risk] Symlinks not rendering properly in Windows or specific IDE configurations → Mitigation: Implemented absolute/parent relative strict symlinking.
- [Risk] OpenSpec file structure rigidity blocking loose explorations → Mitigation: Enforcing `proposal.md` standardization as an entry point for `openspec` to recognize explorations correctly.
