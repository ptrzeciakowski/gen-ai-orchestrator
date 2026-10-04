import os
import subprocess

OUT_DIR = "/Users/pawel/git/gen-ai-orchestrator/sandbox/2026-09-26-projekt-szafy/rysunki"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def render_svg_to_png(svg_path, png_path, width, height):
    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        f"--screenshot={png_path}",
        f"--window-size={width},{height}",
        "--default-background-color=00000000",
        svg_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(png_path):
        print(f"OK: {os.path.basename(png_path)} ({os.path.getsize(png_path)} bytes)")
    else:
        print(f"Error {png_path}: {res.stderr}")

COMMON_STYLES = '''
    <style>
        text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }
        .title { font-size: 24px; font-weight: 800; fill: #0F172A; letter-spacing: -0.5px; }
        .subtitle { font-size: 13.5px; font-weight: 500; fill: #475569; }
        .corp-frame { fill: #FFFFFF; stroke: #0F172A; stroke-width: 3.5; }
        .corp-inner { fill: #F8FAFC; stroke: #94A3B8; stroke-width: 1.5; }
        .shelf { fill: #FFFFFF; stroke: #334155; stroke-width: 2.5; }
        .dryer-bg { fill: #E0F2FE; stroke: #0284C7; stroke-width: 2; rx: 6px; }
        .laundry-niche { fill: #F0FDF4; stroke: #16A34A; stroke-width: 1.5; stroke-dasharray: 4,4; rx: 4px; }
        .drawer { fill: #F1F5F9; stroke: #475569; stroke-width: 2; rx: 4px; }
        .basket { fill: #F8FAFC; stroke: #64748B; stroke-width: 1.5; stroke-dasharray: 4,3; rx: 3px; }
        .shoe-shelf-bg { fill: #F1F5F9; stroke: #64748B; stroke-width: 1.5; rx: 4px; }
        .hanging-area { fill: #FAF5FF; stroke: #A855F7; stroke-width: 1.5; stroke-dasharray: 4,4; rx: 5px; }
        .rod { stroke: #475569; stroke-width: 4; stroke-linecap: round; }
        .item-text { font-size: 11px; font-weight: 700; fill: #1E293B; }
        .item-sub { font-size: 9.5px; font-weight: 500; fill: #64748B; }
        .dim-text { font-size: 11px; font-weight: 700; fill: #DC2626; }
        .dim-title { font-size: 12.5px; font-weight: 800; fill: #DC2626; }
        .tag { font-size: 10px; font-weight: 700; fill: #FFFFFF; rx: 3px; }
    </style>
    <defs>
        <marker id="arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#DC2626"/>
        </marker>
        <marker id="arr-rev" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#DC2626"/>
        </marker>
    </defs>
'''

def h_dim(x1, x2, y, text, offset=-24):
    dy = y + offset
    return f'''
    <g>
        <line x1="{x1}" y1="{y}" x2="{x1}" y2="{dy-4}" stroke="#DC2626" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="{x2}" y1="{y}" x2="{x2}" y2="{dy-4}" stroke="#DC2626" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="{x1+4}" y1="{dy}" x2="{x2-4}" y2="{dy}" stroke="#DC2626" stroke-width="1.5" marker-start="url(#arr-rev)" marker-end="url(#arr)"/>
        <text x="{(x1+x2)/2}" y="{dy-5}" class="dim-text" text-anchor="middle">{text}</text>
    </g>'''

def v_dim(y1, y2, x, text, offset=28, anchor="start"):
    dx = x + offset
    tx = dx + 12 if anchor == "start" else dx - 12
    return f'''
    <g>
        <line x1="{x}" y1="{y1}" x2="{dx+4}" y2="{y1}" stroke="#DC2626" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="{x}" y1="{y2}" x2="{dx+4}" y2="{y2}" stroke="#DC2626" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="{dx}" y1="{y1+4}" x2="{dx}" y2="{y2-4}" stroke="#DC2626" stroke-width="1.5" marker-start="url(#arr-rev)" marker-end="url(#arr)"/>
        <text x="{tx}" y="{(y1+y2)/2 + 4}" class="dim-text" text-anchor="{anchor}">{text}</text>
    </g>'''

# ==============================================================================
# 1. SZAFA NA WYMIAR (WEJŚCIE)
# ==============================================================================
def gen_szafa_wejscie():
    sc = 3.5
    ox, oy = 175, 145
    
    w_tot = 125 * sc
    h_tot = 240 * sc
    
    b_l = 12 * sc
    w_c1 = 50 * sc
    w_div = 2 * sc
    w_c = 51 * sc
    b_r = 10 * sc
    
    x_c1 = ox + b_l
    x_c2 = x_c1 + w_c1 + w_div
    
    h_top = 45 * sc
    h_hang = 160 * sc
    h_bot = 35 * sc
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 1120" width="920" height="1120" style="background:#FFFFFF;">
    {COMMON_STYLES}
    
    <text x="{ox}" y="45" class="title">SZAFA NA WYMIAR PRZY WEJŚCIU – WARIANT 1</text>
    <text x="{ox}" y="70" class="subtitle">Wnęka 125 cm × głębokość 62 cm | Lewa: Długie płaszcze (160 cm luzu) | Prawa: Regał obuwniczy</text>
    
    <rect x="{ox}" y="{oy}" width="{w_tot}" height="{h_tot}" class="corp-frame" />
    
    <!-- BLENDY BOCZNE -->
    <rect x="{ox}" y="{oy}" width="{b_l}" height="{h_tot}" fill="#F1F5F9" stroke="#94A3B8" stroke-dasharray="3,3" />
    <text x="{ox + b_l/2}" y="{oy + h_tot/2}" class="item-sub" text-anchor="middle" transform="rotate(-90 {ox + b_l/2} {oy + h_tot/2})">BLENDA 12 cm</text>
    
    <rect x="{x_c2 + w_c}" y="{oy}" width="{b_r}" height="{h_tot}" fill="#F1F5F9" stroke="#94A3B8" stroke-dasharray="3,3" />
    <text x="{x_c2 + w_c + b_r/2}" y="{oy + h_tot/2}" class="item-sub" text-anchor="middle" transform="rotate(-90 {x_c2 + w_c + b_r/2} {oy + h_tot/2})">BLENDA 10 cm</text>
    
    <!-- KOLUMNA LEWA (50 cm) -->
    <rect x="{x_c1}" y="{oy}" width="{w_c1}" height="{h_tot}" fill="#FFFFFF" stroke="#334155" stroke-width="1.5" />
    
    <!-- Pawlacz lewy -->
    <rect x="{x_c1+4}" y="{oy+4}" width="{w_c1-8}" height="{h_top-6}" fill="#F8FAFC" rx="4"/>
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top/2}" class="item-text" text-anchor="middle">PAWLACZ GÓRNY (45 cm)</text>
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top/2 + 15}" class="item-sub" text-anchor="middle">pudła sezonowe / torby podróżne</text>
    <line x1="{x_c1}" y1="{oy + h_top}" x2="{x_c1 + w_c1}" y2="{oy + h_top}" class="shelf" />
    
    <!-- Strefa wieszania 160 cm -->
    <rect x="{x_c1+6}" y="{oy + h_top + 6}" width="{w_c1-12}" height="{h_hang-12}" class="hanging-area" />
    <line x1="{x_c1+12}" y1="{oy + h_top + 32}" x2="{x_c1 + w_c1 - 12}" y2="{oy + h_top + 32}" class="rod" />
    <circle cx="{x_c1+16}" cy="{oy + h_top + 32}" r="4" fill="#334155" />
    <circle cx="{x_c1 + w_c1 - 16}" cy="{oy + h_top + 32}" r="4" fill="#334155" />
    
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top + 65}" class="item-text" fill="#7E22CE" font-size="12" text-anchor="middle">DRĄŻEK POPRZECZNY</text>
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top + 85}" class="item-text" text-anchor="middle">DŁUGIE PŁASZCZE ZIMOWE</text>
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top + 104}" class="item-sub" text-anchor="middle">trencze, długie kurtki puchowe</text>
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top + 120}" class="item-sub" text-anchor="middle">marynarki i kurtki wyjściowe</text>
    
    <rect x="{x_c1 + 18}" y="{oy + h_top + h_hang/2 - 22}" width="{w_c1 - 36}" height="44" fill="#EDE9FE" stroke="#A855F7" stroke-width="1.5" rx="6"/>
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top + h_hang/2}" class="item-text" fill="#6B21A8" font-size="12" text-anchor="middle">160 cm W ŚWIETLE</text>
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top + h_hang/2 + 15}" class="item-sub" fill="#7E22CE" text-anchor="middle">płaszcz wisi prosto bez zaginania!</text>
    
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top + h_hang - 25}" class="item-sub" text-anchor="middle">Dno: wolne / gumowy ociekacz</text>
    
    <!-- Dolna szuflada -->
    <line x1="{x_c1}" y1="{oy + h_top + h_hang}" x2="{x_c1 + w_c1}" y2="{oy + h_top + h_hang}" class="shelf" />
    <rect x="{x_c1+6}" y="{oy + h_top + h_hang + 6}" width="{w_c1-12}" height="{h_bot-12}" class="drawer" />
    <line x1="{x_c1 + w_c1/2 - 25}" y1="{oy + h_top + h_hang + h_bot/2}" x2="{x_c1 + w_c1/2 + 25}" y2="{oy + h_top + h_hang + h_bot/2}" stroke="#94A3B8" stroke-width="3" stroke-linecap="round"/>
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top + h_hang + h_bot/2 + 16}" class="item-text" text-anchor="middle">SZUFLADA DOLNA (35 cm)</text>
    
    <!-- PRZEGRODA ŚRODKOWA -->
    <rect x="{x_c1 + w_c1}" y="{oy}" width="{w_div}" height="{h_tot}" fill="#334155" />
    
    <!-- KOLUMNA PRAWA (51 cm) -->
    <rect x="{x_c2}" y="{oy}" width="{w_c}" height="{h_tot}" fill="#FFFFFF" stroke="#334155" stroke-width="1.5" />
    
    <rect x="{x_c2+4}" y="{oy+4}" width="{w_c-8}" height="{h_top-6}" fill="#F8FAFC" rx="4"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_top/2}" class="item-text" text-anchor="middle">NADSTAWKA (45 cm)</text>
    <text x="{x_c2 + w_c/2}" y="{oy + h_top/2 + 15}" class="item-sub" text-anchor="middle">pudła / segregatory / zapasy</text>
    <line x1="{x_c2}" y1="{oy + h_top}" x2="{x_c2 + w_c}" y2="{oy + h_top}" class="shelf" />
    '''
    
    sh_heights = [26, 22, 22, 24, 24, 24, 24, 29]
    cur_y = oy + h_top
    shelf_labels = [
        ("PÓŁKA 1 (26 cm)", "koszyki na czapki i kapelusze"),
        ("PÓŁKA 2 (22 cm)", "szaliki, kominy, rękawiczki"),
        ("PÓŁKA 3 (22 cm)", "klucze, portfele, okulary"),
        ("PÓŁKA 4 – BUTY (24 cm)", "bieżące sneakersy / pantofle"),
        ("PÓŁKA 5 – BUTY (24 cm)", "bieżące półbuty / obuwie codzienne"),
        ("PÓŁKA 6 – BUTY (24 cm)", "buty sportowe / wyjściowe"),
        ("PÓŁKA 7 – BUTY (24 cm)", "buty wyjściowe / kapcie"),
        ("DNO REGAŁU (29 cm)", "trzewiki / wyższe buty zimowe")
    ]
    
    for i, (h_cm, (title, sub)) in enumerate(zip(sh_heights, shelf_labels)):
        h_px = h_cm * sc
        svg += f'''
        <rect x="{x_c2+4}" y="{cur_y+2}" width="{w_c-8}" height="{h_px-4}" fill="{'#F1F5F9' if i>=3 else '#F8FAFC'}" rx="3"/>
        <text x="{x_c2 + w_c/2}" y="{cur_y + h_px/2 - 2}" class="item-text" text-anchor="middle">{title}</text>
        <text x="{x_c2 + w_c/2}" y="{cur_y + h_px/2 + 11}" class="item-sub" text-anchor="middle">{sub}</text>
        '''
        cur_y += h_px
        if i < len(sh_heights) - 1:
            svg += f'<line x1="{x_c2}" y1="{cur_y}" x2="{x_c2 + w_c}" y2="{cur_y}" class="shelf" />'
            
    # DIMENSIONS
    svg += h_dim(ox, ox + w_tot, oy, "CAŁKOWITA SZEROKOŚĆ WNĘKI: 125 cm", -50)
    svg += h_dim(x_c1, x_c1 + w_c1, oy, "LEWA: 50 cm", -22)
    svg += h_dim(x_c2, x_c2 + w_c, oy, "PRAWA: 51 cm", -22)
    
    svg += v_dim(oy, oy + h_tot, ox, "WYSOKOŚĆ: 240 cm", -40, anchor="end")
    svg += v_dim(oy + h_top, oy + h_top + h_hang, x_c1, "ŚWIATŁO: 160 cm", -25, anchor="end")
    svg += v_dim(oy + h_top + h_hang, oy + h_tot, x_c1, "SZUFLADA: 35 cm", -25, anchor="end")
    
    svg += v_dim(oy, oy + h_top, ox + w_tot, "PAWLACZ: 45 cm", 25)
    svg += v_dim(oy + h_top, oy + h_tot, ox + w_tot, "REGAŁ PÓŁKOWY: 195 cm", 25)
    
    svg += '</svg>'
    
    with open(f"{OUT_DIR}/szafa_1_na_wymiar_wejscie.svg", "w") as f:
        f.write(svg)
    render_svg_to_png(f"{OUT_DIR}/szafa_1_na_wymiar_wejscie.svg", f"{OUT_DIR}/szafa_1_na_wymiar_wejscie.png", 920, 1120)

# ==============================================================================
# 2. NOWY PAX 35 CM (150 CM = 2 × 75 CM)
# ==============================================================================
def gen_nowy_pax_35():
    sc = 3.6
    ox, oy = 175, 145
    
    w_tot = 150 * sc
    h_tot = 236 * sc
    w_c = 75 * sc
    
    x_c1 = ox
    x_c2 = ox + w_c
    
    # Left module (75 cm):
    # Pawlacz: 36 cm
    # 6 skośnych półek KOMPLEMENT (co 28 cm) = 168 cm
    # Cokół: 32 cm na dole (ostatnia półka i dno)
    h_paw = 36 * sc
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 1120" width="950" height="1120" style="background:#FFFFFF;">
    {COMMON_STYLES}
    
    <text x="{ox}" y="45" class="title">NOWY PAX 35 cm (2 × 75 cm) – WARIANT 1</text>
    <text x="{ox}" y="70" class="subtitle">Ściana 150 cm | Głębokość korpusu 35 cm (z drzwiami ~44 cm) | Wys. 236 cm (drzwi przesuwne)</text>
    
    <!-- MAIN CONTOUR -->
    <rect x="{ox}" y="{oy}" width="{w_tot}" height="{h_tot}" class="corp-frame" />
    
    <!-- DIVIDER -->
    <line x1="{x_c2}" y1="{oy}" x2="{x_c2}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    
    <!-- ==================== LEWY MODUŁ 75 CM (100% BUTY R. 44-45) ==================== -->
    <!-- Pawlacz -->
    <rect x="{x_c1+6}" y="{oy+6}" width="{w_c-12}" height="{h_paw-10}" fill="#F8FAFC" rx="4"/>
    <text x="{x_c1 + w_c/2}" y="{oy + h_paw/2}" class="item-text" text-anchor="middle">PAWLACZ: PÓŁKA 75×35 cm (36 cm)</text>
    <text x="{x_c1 + w_c/2}" y="{oy + h_paw/2 + 15}" class="item-sub" text-anchor="middle">pudła SKUBB na buty poza sezonem</text>
    <line x1="{x_c1}" y1="{oy + h_paw}" x2="{x_c2}" y2="{oy + h_paw}" class="shelf" />
    
    <!-- 6 skośnych półek metalowych KOMPLEMENT -->
    '''
    
    # 6 shelves distributed across remaining ~190 cm
    # Spacing ~ 28 cm each
    shoe_levels = [
        ("PÓŁKA SKOŚNA 1 (KOMPLEMENT)", "3-4 pary butów r. 44-45 (zimowe/trzewiki)"),
        ("PÓŁKA SKOŚNA 2 (KOMPLEMENT)", "3-4 pary butów r. 44-45 (półbuty/eleganckie)"),
        ("PÓŁKA SKOŚNA 3 (KOMPLEMENT)", "3-4 pary butów r. 44-45 (sneakersy skórzane)"),
        ("PÓŁKA SKOŚNA 4 (KOMPLEMENT)", "3-4 pary butów r. 44-45 (sneakersy sportowe)"),
        ("PÓŁKA SKOŚNA 5 (KOMPLEMENT)", "3-4 pary butów (buty codzienne)"),
        ("PÓŁKA SKOŚNA 6 (KOMPLEMENT)", "3-4 pary butów (lekkie / trampki)")
    ]
    
    cur_y = oy + h_paw
    h_shoe_step = (h_tot - h_paw - 30) / 6.0
    
    for i, (title, sub) in enumerate(shoe_levels):
        y_top = cur_y
        y_bot = cur_y + h_shoe_step
        
        # Angled shelf representation (slanted plate)
        svg += f'''
        <g>
            <rect x="{x_c1+8}" y="{y_top+4}" width="{w_c-16}" height="{h_shoe_step-8}" class="shoe-shelf-bg" />
            <!-- Angled shelf plate line -->
            <line x1="{x_c1+16}" y1="{y_top+14}" x2="{x_c2-16}" y2="{y_bot-14}" stroke="#0284C7" stroke-width="2.5" stroke-linecap="round"/>
            <circle cx="{x_c1+16}" cy="{y_top+14}" r="3" fill="#0284C7"/>
            <circle cx="{x_c2-16}" cy="{y_bot-14}" r="3" fill="#0284C7"/>
            
            <text x="{x_c1 + w_c/2 + 20}" y="{y_top + h_shoe_step/2 - 2}" class="item-text" text-anchor="middle">{title}</text>
            <text x="{x_c1 + w_c/2 + 20}" y="{y_top + h_shoe_step/2 + 12}" class="item-sub" text-anchor="middle">{sub}</text>
        </g>
        '''
        cur_y += h_shoe_step
        
    svg += f'''
    <rect x="{x_c1+20}" y="{oy + h_tot - 25}" width="{w_c-40}" height="20" fill="#E2E8F0" rx="3"/>
    <text x="{x_c1 + w_c/2}" y="{oy + h_tot - 11}" class="item-sub" text-anchor="middle" font-weight="700">ŁĄCZNA POJEMNOŚĆ LEWEJ SZAFIARKI: 20–24 PARY</text>
    
    <!-- ==================== PRAWY MODUŁ 75 CM (HYBRYDA) ==================== -->
    <!-- Pawlacz -->
    <rect x="{x_c2+6}" y="{oy+6}" width="{w_c-12}" height="{h_paw-10}" fill="#F8FAFC" rx="4"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw/2}" class="item-text" text-anchor="middle">PAWLACZ: PÓŁKA 75×35 cm (36 cm)</text>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw/2 + 15}" class="item-sub" text-anchor="middle">pudła SKUBB na czapki i akcesoria</text>
    <line x1="{x_c2}" y1="{oy + h_paw}" x2="{ox + w_tot}" y2="{oy + h_paw}" class="shelf" />
    
    <!-- Wysuwany wieszak KOMPLEMENT (90 cm) -->
    '''
    h_hanger = 90 * sc
    y_h_start = oy + h_paw
    svg += f'''
    <rect x="{x_c2+8}" y="{y_h_start+6}" width="{w_c-16}" height="{h_hanger-12}" class="hanging-area" />
    
    <!-- Telescopic pullout hanger rail -->
    <line x1="{x_c2 + w_c/2}" y1="{y_h_start + 15}" x2="{x_c2 + w_c/2}" y2="{y_h_start + 70}" stroke="#475569" stroke-width="5" stroke-linecap="round"/>
    <rect x="{x_c2 + w_c/2 - 25}" y="{y_h_start + 12}" width="50" height="12" fill="#334155" rx="3"/>
    <text x="{x_c2 + w_c/2}" y="{y_h_start + 21}" fill="#FFFFFF" font-size="8" font-weight="700" text-anchor="middle">WYSUW</text>
    
    <text x="{x_c2 + w_c/2}" y="{y_h_start + 105}" class="item-text" fill="#7E22CE" font-size="12" text-anchor="middle">WYSUWANY WIESZAK KOMPLEMENT</text>
    <text x="{x_c2 + w_c/2}" y="{y_h_start + 125}" class="item-text" text-anchor="middle">5–6 LEKKICH KURTEK CODZIENNYCH</text>
    <text x="{x_c2 + w_c/2}" y="{y_h_start + 142}" class="item-sub" text-anchor="middle">wiatrówki, ramoneski, bluzy, kardigany</text>
    <line x1="{x_c2}" y1="{y_h_start + h_hanger}" x2="{ox + w_tot}" y2="{y_h_start + h_hanger}" class="shelf" />
    '''
    
    # 2 Szuflady KOMPLEMENT (po 16 cm) = 32 cm
    h_dr = 16 * sc
    y_dr1 = y_h_start + h_hanger
    y_dr2 = y_dr1 + h_dr
    
    svg += f'''
    <!-- Szuflada 1 -->
    <rect x="{x_c2+8}" y="{y_dr1+4}" width="{w_c-16}" height="{h_dr-8}" class="drawer" />
    <line x1="{x_c2 + w_c/2 - 25}" y1="{y_dr1 + h_dr/2}" x2="{x_c2 + w_c/2 + 25}" y2="{y_dr1 + h_dr/2}" stroke="#94A3B8" stroke-width="3" stroke-linecap="round"/>
    <text x="{x_c2 + w_c/2}" y="{y_dr1 + h_dr/2 + 14}" class="item-text" text-anchor="middle">SZUFLADA 1: okulary, rękawiczki, smycze</text>
    
    <!-- Szuflada 2 -->
    <rect x="{x_c2+8}" y="{y_dr2+4}" width="{w_c-16}" height="{h_dr-8}" class="drawer" />
    <line x1="{x_c2 + w_c/2 - 25}" y1="{y_dr2 + h_dr/2}" x2="{x_c2 + w_c/2 + 25}" y2="{y_dr2 + h_dr/2}" stroke="#94A3B8" stroke-width="3" stroke-linecap="round"/>
    <text x="{x_c2 + w_c/2}" y="{y_dr2 + h_dr/2 + 14}" class="item-text" text-anchor="middle">SZUFLADA 2: akcesoria do butów, pasty</text>
    <line x1="{x_c2}" y1="{y_dr2 + h_dr}" x2="{ox + w_tot}" y2="{y_dr2 + h_dr}" class="shelf" />
    '''
    
    # 3 skośne półki na dole
    y_sh_r_start = y_dr2 + h_dr
    h_r_rem = (oy + h_tot) - y_sh_r_start - 10
    h_sh_r_step = h_r_rem / 3.0
    
    r_shoe_levels = [
        ("PÓŁKA SKOŚNA 7 (KOMPLEMENT)", "3-4 pary butów damskich / dziecięcych"),
        ("PÓŁKA SKOŚNA 8 (KOMPLEMENT)", "3-4 pary butów sportowych"),
        ("PÓŁKA SKOŚNA 9 (KOMPLEMENT)", "3-4 pary butów codziennych")
    ]
    
    cur_yr = y_sh_r_start
    for i, (title, sub) in enumerate(r_shoe_levels):
        y_top = cur_yr
        y_bot = cur_yr + h_sh_r_step
        svg += f'''
        <g>
            <rect x="{x_c2+8}" y="{y_top+4}" width="{w_c-16}" height="{h_sh_r_step-8}" class="shoe-shelf-bg" />
            <line x1="{x_c2+16}" y1="{y_top+12}" x2="{ox+w_tot-16}" y2="{y_bot-12}" stroke="#0284C7" stroke-width="2.5" stroke-linecap="round"/>
            <circle cx="{x_c2+16}" cy="{y_top+12}" r="3" fill="#0284C7"/>
            <circle cx="{ox+w_tot-16}" cy="{y_bot-12}" r="3" fill="#0284C7"/>
            
            <text x="{x_c2 + w_c/2 + 20}" y="{y_top + h_sh_r_step/2 - 2}" class="item-text" text-anchor="middle">{title}</text>
            <text x="{x_c2 + w_c/2 + 20}" y="{y_top + h_sh_r_step/2 + 11}" class="item-sub" text-anchor="middle">{sub}</text>
        </g>
        '''
        cur_yr += h_sh_r_step
        
    # DIMENSIONS
    svg += h_dim(ox, ox + w_tot, oy, "ŁĄCZNA SZEROKOŚĆ ŚCIANY: 150 cm", -50)
    svg += h_dim(x_c1, x_c2, oy, "MODUŁ LEWY: 75 cm", -22)
    svg += h_dim(x_c2, ox + w_tot, oy, "MODUŁ PRAWY: 75 cm", -22)
    
    svg += v_dim(oy, oy + h_tot, ox, "WYSOKOŚĆ: 236 cm", -40, anchor="end")
    svg += v_dim(oy, oy + h_paw, ox, "PAWLACZ: 36 cm", -18, anchor="end")
    svg += v_dim(oy + h_paw, oy + h_tot, ox, "STREFA OBUWNICZA: 200 cm", -18, anchor="end")
    
    svg += v_dim(y_h_start, y_h_start + h_hanger, ox + w_tot, "WIESZAK: 90 cm", 25)
    svg += v_dim(y_dr1, y_dr2 + h_dr, ox + w_tot, "SZUFLADY: 32 cm", 25)
    svg += v_dim(y_sh_r_start, oy + h_tot, ox + w_tot, "PÓŁKI BUTY: 78 cm", 25)
    
    svg += '</svg>'
    
    with open(f"{OUT_DIR}/szafa_2_nowy_pax_35.svg", "w") as f:
        f.write(svg)
    render_svg_to_png(f"{OUT_DIR}/szafa_2_nowy_pax_35.svg", f"{OUT_DIR}/szafa_2_nowy_pax_35.png", 950, 1120)

# ==============================================================================
# 3. ISTNIEJĄCY PAX 58 CM (270 CM = 100 + 100 + 50 + 20 CM)
# ==============================================================================
def gen_istniejacy_pax_58():
    sc = 3.2
    ox, oy = 175, 145
    
    w_tot = 270 * sc
    h_tot = 236 * sc
    
    w_m1 = 100 * sc
    w_m2 = 100 * sc
    w_m3 = 50 * sc
    w_m4 = 20 * sc
    
    x_m1 = ox
    x_m2 = x_m1 + w_m1
    x_m3 = x_m2 + w_m2
    x_m4 = x_m3 + w_m3
    
    h_paw = 36 * sc
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1260 1080" width="1260" height="1080" style="background:#FFFFFF;">
    {COMMON_STYLES}
    
    <text x="{ox}" y="45" class="title">ISTNIEJĄCY PAX 58 cm (270 cm) – WARIANT 1</text>
    <text x="{ox}" y="70" class="subtitle">Moduł 1 (100 cm): Pralnia | Moduł 2 (100 cm): Garderoba sypialniana | Moduł 3 (50 cm): AGD/Narzędzia | Dob. 20 cm: Deska</text>
    
    <rect x="{ox}" y="{oy}" width="{w_tot}" height="{h_tot}" class="corp-frame" />
    
    <!-- PODZIAŁY MODUŁÓW -->
    <line x1="{x_m2}" y1="{oy}" x2="{x_m2}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    <line x1="{x_m3}" y1="{oy}" x2="{x_m3}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    <line x1="{x_m4}" y1="{oy}" x2="{x_m4}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    
    <!-- ==================== MODUŁ 1: 100 CM (PRALNIA) ==================== -->
    <!-- Pawlacz -->
    <rect x="{x_m1+4}" y="{oy+4}" width="{w_m1-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m1 + w_m1/2}" y="{oy + h_paw/2}" class="item-text" text-anchor="middle">PAWLACZ: CZARNA WALIZKA PODRÓŻNA (36 cm)</text>
    <line x1="{x_m1}" y1="{oy + h_paw}" x2="{x_m2}" y2="{oy + h_paw}" class="shelf" />
    
    <!-- Półka 1 (ręczniki, pościele) -->
    '''
    h_p1 = 32 * sc
    y_p1 = oy + h_paw
    h_p2 = 30 * sc
    y_p2 = y_p1 + h_p1
    h_p3 = 30 * sc
    y_p3 = y_p2 + h_p2
    
    svg += f'''
    <rect x="{x_m1+6}" y="{y_p1+4}" width="{w_m1-12}" height="{h_p1-8}" fill="#F8FAFC" rx="3"/>
    <text x="{x_m1 + w_m1/2}" y="{y_p1 + h_p1/2}" class="item-text" text-anchor="middle">PÓŁKA 100 cm: KOŁDRY, KOCE, POŚCIELE (32 cm)</text>
    <line x1="{x_m1}" y1="{y_p1 + h_p1}" x2="{x_m2}" y2="{y_p1 + h_p1}" class="shelf" />
    
    <rect x="{x_m1+6}" y="{y_p2+4}" width="{w_m1-12}" height="{h_p2-8}" fill="#F8FAFC" rx="3"/>
    <text x="{x_m1 + w_m1/2}" y="{y_p2 + h_p2/2}" class="item-text" text-anchor="middle">PÓŁKA 100 cm: RĘCZNIKI KĄPIELOWE (30 cm)</text>
    <line x1="{x_m1}" y1="{y_p2 + h_p2}" x2="{x_m2}" y2="{y_p2 + h_p2}" class="shelf" />
    
    <rect x="{x_m1+6}" y="{y_p3+4}" width="{w_m1-12}" height="{h_p3-8}" fill="#F8FAFC" rx="3"/>
    <text x="{x_m1 + w_m1/2}" y="{y_p3 + h_p3/2}" class="item-text" text-anchor="middle">PÓŁKA 100 cm: KOSZE Z PRANIEM / CHEMIA</text>
    <line x1="{x_m1}" y1="{y_p3 + h_p3}" x2="{x_m2}" y2="{y_p3 + h_p3}" class="shelf" />
    '''
    
    # Strefa dolna modułu 1 (100 cm szerokości, wys. ok. 100 cm)
    # Suszarka Beko: 60 cm szer. x 85 cm wys.
    # Wnęka obok: 31 cm szer. x 85 cm wys.
    y_dryer_top = y_p3 + h_p3
    w_dryer = 60 * sc
    w_niche = 31 * sc
    h_dryer = 85 * sc
    
    svg += f'''
    <!-- Suszarka Beko 60 cm -->
    <rect x="{x_m1+8}" y="{y_dryer_top + 10}" width="{w_dryer}" height="{h_dryer}" class="dryer-bg" />
    <!-- Bęben suszarki okrąg -->
    <circle cx="{x_m1 + 8 + w_dryer/2}" cy="{y_dryer_top + 10 + h_dryer/2}" r="65" fill="#BAE6FD" stroke="#0284C7" stroke-width="2.5" />
    <circle cx="{x_m1 + 8 + w_dryer/2}" cy="{y_dryer_top + 10 + h_dryer/2}" r="50" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="4,2" />
    <!-- Panel sterowania -->
    <rect x="{x_m1 + 16}" y="{y_dryer_top + 18}" width="{w_dryer - 16}" height="28" fill="#0284C7" rx="3" />
    <circle cx="{x_m1 + 8 + w_dryer/2}" cy="{y_dryer_top + 32}" r="8" fill="#FFFFFF" />
    <text x="{x_m1 + 8 + w_dryer/2}" y="{y_dryer_top + 10 + h_dryer/2 + 5}" class="item-text" fill="#0369A1" font-size="12" text-anchor="middle">SUSZARKA BEKO</text>
    <text x="{x_m1 + 8 + w_dryer/2}" y="{y_dryer_top + 10 + h_dryer/2 + 20}" class="item-sub" fill="#0284C7" text-anchor="middle">szer. 60 cm | wys. 85 cm</text>
    <text x="{x_m1 + 8 + w_dryer/2}" y="{y_dryer_top + 10 + h_dryer/2 + 33}" class="item-sub" fill="#0284C7" text-anchor="middle">kasetka na skropliny (manual)</text>
    
    <!-- Wnęka 31 cm obok suszarki -->
    <rect x="{x_m1 + 16 + w_dryer}" y="{y_dryer_top + 10}" width="{w_niche}" height="{h_dryer}" class="laundry-niche" />
    <text x="{x_m1 + 16 + w_dryer + w_niche/2}" y="{y_dryer_top + h_dryer/2 - 15}" class="item-text" fill="#15803D" text-anchor="middle">WNĘKA 31 cm</text>
    <text x="{x_m1 + 16 + w_dryer + w_niche/2}" y="{y_dryer_top + h_dryer/2 + 5}" class="item-sub" fill="#166534" text-anchor="middle">Regał slim cargo</text>
    <text x="{x_m1 + 16 + w_dryer + w_niche/2}" y="{y_dryer_top + h_dryer/2 + 20}" class="item-sub" fill="#166534" text-anchor="middle">lub pionowy kosz</text>
    <text x="{x_m1 + 16 + w_dryer + w_niche/2}" y="{y_dryer_top + h_dryer/2 + 35}" class="item-sub" fill="#166534" text-anchor="middle">na brudne pranie</text>
    
    <!-- ==================== MODUŁ 2: 100 CM (GARDEROBA GŁÓWNA) ==================== -->
    <rect x="{x_m2+4}" y="{oy+4}" width="{w_m2-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw/2}" class="item-text" text-anchor="middle">PAWLACZ: CZERWONA DUŻA WALIZKA (36 cm)</text>
    <line x1="{x_m2}" y1="{oy + h_paw}" x2="{x_m3}" y2="{oy + h_paw}" class="shelf" />
    
    <!-- Drążek 100 cm (120 cm wys.) -->
    '''
    h_m2_hang = 120 * sc
    y_m2_hang = oy + h_paw
    svg += f'''
    <rect x="{x_m2+6}" y="{y_m2_hang+6}" width="{w_m2-12}" height="{h_m2_hang-12}" class="hanging-area" />
    <line x1="{x_m2+16}" y1="{y_m2_hang+28}" x2="{x_m3-16}" y2="{y_m2_hang+28}" class="rod" />
    <circle cx="{x_m2+16}" cy="{y_m2_hang+28}" r="4" fill="#334155" />
    <circle cx="{x_m3-16}" cy="{y_m2_hang+28}" r="4" fill="#334155" />
    
    <text x="{x_m2 + w_m2/2}" y="{y_m2_hang + 60}" class="item-text" fill="#7E22CE" font-size="12" text-anchor="middle">DRĄŻEK 100 cm: GARDEROBA BAZOWA</text>
    <text x="{x_m2 + w_m2/2}" y="{y_m2_hang + 80}" class="item-text" text-anchor="middle">Garnitury, koszule, marynarki, spodnie w kant</text>
    <text x="{x_m2 + w_m2/2}" y="{y_m2_hang + 96}" class="item-sub" text-anchor="middle">Wysokość wiszenia: 120 cm (idealna na ubrania męskie/damskie)</text>
    <line x1="{x_m2}" y1="{y_m2_hang + h_m2_hang}" x2="{x_m3}" y2="{y_m2_hang + h_m2_hang}" class="shelf" />
    '''
    
    # 3 Szuflady KOMPLEMENT + 1 Kosz druciany
    h_m2_dr = 16 * sc
    y_m2_d1 = y_m2_hang + h_m2_hang
    y_m2_d2 = y_m2_d1 + h_m2_dr
    y_m2_d3 = y_m2_d2 + h_m2_dr
    y_m2_basket = y_m2_d3 + h_m2_dr
    
    svg += f'''
    <rect x="{x_m2+6}" y="{y_m2_d1+3}" width="{w_m2-12}" height="{h_m2_dr-6}" class="drawer" />
    <line x1="{x_m2 + w_m2/2 - 30}" y1="{y_m2_d1 + h_m2_dr/2}" x2="{x_m2 + w_m2/2 + 30}" y2="{y_m2_d1 + h_m2_dr/2}" stroke="#94A3B8" stroke-width="3" stroke-linecap="round"/>
    <text x="{x_m2 + w_m2/2}" y="{y_m2_d1 + h_m2_dr/2 + 13}" class="item-text" text-anchor="middle">SZUFLADA 1: bielizna osobista, skarpetki</text>
    
    <rect x="{x_m2+6}" y="{y_m2_d2+3}" width="{w_m2-12}" height="{h_m2_dr-6}" class="drawer" />
    <line x1="{x_m2 + w_m2/2 - 30}" y1="{y_m2_d2 + h_m2_dr/2}" x2="{x_m2 + w_m2/2 + 30}" y2="{y_m2_d2 + h_m2_dr/2}" stroke="#94A3B8" stroke-width="3" stroke-linecap="round"/>
    <text x="{x_m2 + w_m2/2}" y="{y_m2_d2 + h_m2_dr/2 + 13}" class="item-text" text-anchor="middle">SZUFLADA 2: t-shirty, bluzki, topy</text>
    
    <rect x="{x_m2+6}" y="{y_m2_d3+3}" width="{w_m2-12}" height="{h_m2_dr-6}" class="drawer" />
    <line x1="{x_m2 + w_m2/2 - 30}" y1="{y_m2_d3 + h_m2_dr/2}" x2="{x_m2 + w_m2/2 + 30}" y2="{y_m2_d3 + h_m2_dr/2}" stroke="#94A3B8" stroke-width="3" stroke-linecap="round"/>
    <text x="{x_m2 + w_m2/2}" y="{y_m2_d3 + h_m2_dr/2 + 13}" class="item-text" text-anchor="middle">SZUFLADA 3: spodnie, bluzy, swetry</text>
    
    <rect x="{x_m2+6}" y="{y_m2_basket+3}" width="{w_m2-12}" height="{h_m2_dr-6}" class="basket" />
    <text x="{x_m2 + w_m2/2}" y="{y_m2_basket + h_m2_dr/2 + 5}" class="item-text" text-anchor="middle">KOSZ DRUCIANY KOMPLEMENT: koce / dodatki / pościel</text>
    
    <!-- ==================== MODUŁ 3: 50 CM (GOSPODARCZY / AGD) ==================== -->
    <rect x="{x_m3+4}" y="{oy+4}" width="{w_m3-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m3 + w_m3/2}" y="{oy + h_paw/2 + 5}" class="item-text" text-anchor="middle">PAWLACZ</text>
    <line x1="{x_m3}" y1="{oy + h_paw}" x2="{x_m4}" y2="{oy + h_paw}" class="shelf" />
    
    <!-- Wnęka wysoka 130 cm -->
    '''
    h_m3_tall = 130 * sc
    y_m3_tall = oy + h_paw
    svg += f'''
    <rect x="{x_m3+6}" y="{y_m3_tall+6}" width="{w_m3-12}" height="{h_m3_tall-12}" fill="#F1F5F9" stroke="#64748B" stroke-dasharray="3,3" rx="4"/>
    <text x="{x_m3 + w_m3/2}" y="{y_m3_tall + 40}" class="item-text" text-anchor="middle">WNĘKA GOSPODARCZA</text>
    <text x="{x_m3 + w_m3/2}" y="{y_m3_tall + 60}" class="item-sub" text-anchor="middle">- Odkurzacz Amica</text>
    <text x="{x_m3 + w_m3/2}" y="{y_m3_tall + 78}" class="item-sub" text-anchor="middle">- Składana drabina alu</text>
    <text x="{x_m3 + w_m3/2}" y="{y_m3_tall + 96}" class="item-sub" text-anchor="middle">- Skrzynka Parkside</text>
    <line x1="{x_m3}" y1="{y_m3_tall + h_m3_tall}" x2="{x_m4}" y2="{y_m3_tall + h_m3_tall}" class="shelf" />
    
    <!-- Dolny kosz i półka -->
    <rect x="{x_m3+6}" y="{y_m3_tall + h_m3_tall + 4}" width="{w_m3-12}" height="{h_m2_dr-8}" class="basket" />
    <text x="{x_m3 + w_m3/2}" y="{y_m3_tall + h_m3_tall + h_m2_dr/2 + 2}" class="item-sub" font-weight="700" text-anchor="middle">Kosz druciany 50 cm</text>
    
    <rect x="{x_m3+6}" y="{y_m3_tall + h_m3_tall + h_m2_dr + 4}" width="{w_m3-12}" height="{(h_tot - (h_paw + h_m3_tall + h_m2_dr)) - 10}" fill="#E2E8F0" rx="3" />
    <text x="{x_m3 + w_m3/2}" y="{oy + h_tot - 20}" class="item-sub" font-weight="700" text-anchor="middle">Walizki Parkside</text>
    
    <!-- ==================== MODUŁ 4: 20 CM (DOBUDÓWKA DESKA) ==================== -->
    <rect x="{x_m4+4}" y="{oy+4}" width="{w_m4-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_paw/2 - 4}" class="item-text" font-size="10" text-anchor="middle">ŻELAZ-</text>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_paw/2 + 10}" class="item-text" font-size="10" text-anchor="middle">KO</text>
    <line x1="{x_m4}" y1="{oy + h_paw}" x2="{ox + w_tot}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_m4+4}" y="{oy + h_paw + 6}" width="{w_m4-8}" height="{h_tot - h_paw - 12}" fill="#F8FAFC" stroke="#94A3B8" stroke-dasharray="2,2" rx="3"/>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_tot/2 - 20}" class="item-text" font-size="10" text-anchor="middle">DESKA</text>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_tot/2}" class="item-text" font-size="10" text-anchor="middle">DO</text>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_tot/2 + 20}" class="item-text" font-size="10" text-anchor="middle">PRASO-</text>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_tot/2 + 40}" class="item-text" font-size="10" text-anchor="middle">WANIA</text>
    '''
    
    # DIMENSIONS
    svg += h_dim(ox, ox + w_tot, oy, "ŁĄCZNA SZEROKOŚĆ ZABUDOWY PAX 58: 270 cm", -50)
    svg += h_dim(x_m1, x_m2, oy, "PRALNIA: 100 cm", -22)
    svg += h_dim(x_m2, x_m3, oy, "GARDEROBA: 100 cm", -22)
    svg += h_dim(x_m3, x_m4, oy, "AGD: 50 cm", -22)
    svg += h_dim(x_m4, ox + w_tot, oy, "20", -22)
    
    svg += v_dim(oy, oy + h_tot, ox, "WYSOKOŚĆ: 236 cm", -40, anchor="end")
    svg += v_dim(oy, oy + h_paw, ox, "PAWLACZ: 36 cm", -18, anchor="end")
    svg += v_dim(y_p1, y_dryer_top, ox, "PÓŁKI: 92 cm", -18, anchor="end")
    svg += v_dim(y_dryer_top, oy + h_tot, ox, "SUSZARKA: 100 cm", -18, anchor="end")
    
    svg += v_dim(oy + h_paw, y_m2_hang + h_m2_hang, ox + w_tot, "DRĄŻEK: 120 cm", 25)
    svg += v_dim(y_m2_hang + h_m2_hang, oy + h_tot, ox + w_tot, "SZUFLADY: 80 cm", 25)
    
    svg += '</svg>'
    
    with open(f"{OUT_DIR}/szafa_3_istniejacy_pax_58.svg", "w") as f:
        f.write(svg)
    render_svg_to_png(f"{OUT_DIR}/szafa_3_istniejacy_pax_58.svg", f"{OUT_DIR}/szafa_3_istniejacy_pax_58.png", 1260, 1080)

# ==============================================================================
# 4. PANORAMA WSZYSTKICH 3 SZAF W SKALI (OD PRAWEJ DO LEWEJ)
# ==============================================================================
def gen_panorama():
    # Scale: 1 cm = 2.4 px
    # Total widths:
    # Szafa na wymiar: 125 cm = 300 px
    # Nowy PAX 35: 150 cm = 360 px
    # PAX 58: 270 cm = 648 px
    # Spacing between wardrobes: 70 px
    # Layout from LEFT to RIGHT in apartment perspective or ordered visually:
    # User asked: "od prawej do lewej: na wymiar, nowy pax 35, pax 58"
    # That means when viewing from Left to Right: PAX 58 -> Nowy PAX 35 -> Na wymiar (so Na wymiar is on the far right!)
    sc = 2.4
    ox, oy = 90, 140
    
    w_pax58 = 270 * sc # 648 px
    gap1 = 65
    w_pax35 = 150 * sc # 360 px
    gap2 = 65
    w_wymiar = 125 * sc # 300 px
    
    x_pax58 = ox
    x_pax35 = x_pax58 + w_pax58 + gap1
    x_wymiar = x_pax35 + w_pax35 + gap2
    
    h_pax = 236 * sc # 566.4 px
    h_wymiar = 240 * sc # 576 px
    
    svg_w = int(x_wymiar + w_wymiar + 90)
    svg_h = int(oy + h_wymiar + 120)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}" style="background:#FFFFFF;">
    {COMMON_STYLES}
    
    <text x="{ox}" y="45" class="title">PANORAMA UKŁADU SZAF W CAŁYM MIESZKANIU – WARIANT 1</text>
    <text x="{ox}" y="70" class="subtitle">Wszystkie szafy narysowane w JEDNEJ wspólnej skali geometrycznej (1 cm = 2.4 px) | Widok od lewej do prawej</text>
    
    <!-- 1. PAX 58 CM (PO LEWEJ) -->
    <rect x="{x_pax58}" y="{oy}" width="{w_pax58}" height="{h_pax}" class="corp-frame" />
    <rect x="{x_pax58}" y="{oy-28}" width="{w_pax58}" height="24" fill="#0F172A" rx="4"/>
    <text x="{x_pax58 + w_pax58/2}" y="{oy-12}" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">1. ISTNIEJĄCY PAX 58 cm (szer. 270 cm, gł. 58 cm) – PRALNIA &amp; GARDEROBA</text>
    
    <!-- Moduł 1: 100 cm (Pralnia z suszarką) -->
    <line x1="{x_pax58 + 100*sc}" y1="{oy}" x2="{x_pax58 + 100*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <!-- Suszarka -->
    <rect x="{x_pax58 + 6}" y="{oy + h_pax - 85*sc}" width="{60*sc}" height="{85*sc - 6}" class="dryer-bg"/>
    <circle cx="{x_pax58 + 6 + 30*sc}" cy="{oy + h_pax - 42*sc}" r="45" fill="#BAE6FD" stroke="#0284C7" stroke-width="2"/>
    <text x="{x_pax58 + 6 + 30*sc}" y="{oy + h_pax - 40*sc}" class="item-text" fill="#0369A1" text-anchor="middle">SUSZARKA</text>
    <text x="{x_pax58 + 6 + 30*sc}" y="{oy + h_pax - 26*sc}" class="item-sub" fill="#0284C7" text-anchor="middle">BEKO 60cm</text>
    
    <!-- Wnęka 31 cm -->
    <rect x="{x_pax58 + 6 + 60*sc + 4}" y="{oy + h_pax - 85*sc}" width="{31*sc - 6}" height="{85*sc - 6}" class="laundry-niche"/>
    <text x="{x_pax58 + 6 + 60*sc + 15*sc}" y="{oy + h_pax - 40*sc}" class="item-sub" fill="#15803D" font-weight="700" text-anchor="middle">KOSZ /</text>
    <text x="{x_pax58 + 6 + 60*sc + 15*sc}" y="{oy + h_pax - 26*sc}" class="item-sub" fill="#15803D" font-weight="700" text-anchor="middle">CHEMIA</text>
    
    <!-- Półki nad suszarką -->
    <line x1="{x_pax58}" y1="{oy + 36*sc}" x2="{x_pax58 + 100*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <line x1="{x_pax58}" y1="{oy + 68*sc}" x2="{x_pax58 + 100*sc}" y2="{oy + 68*sc}" class="shelf"/>
    <line x1="{x_pax58}" y1="{oy + 98*sc}" x2="{x_pax58 + 100*sc}" y2="{oy + 98*sc}" class="shelf"/>
    <line x1="{x_pax58}" y1="{oy + 128*sc}" x2="{x_pax58 + 100*sc}" y2="{oy + 128*sc}" class="shelf"/>
    <text x="{x_pax58 + 50*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Walizka czarna</text>
    <text x="{x_pax58 + 50*sc}" y="{oy + 54*sc}" class="item-sub" text-anchor="middle">Półka 100cm: pościele / koce</text>
    <text x="{x_pax58 + 50*sc}" y="{oy + 84*sc}" class="item-sub" text-anchor="middle">Półka 100cm: ręczniki</text>
    <text x="{x_pax58 + 50*sc}" y="{oy + 114*sc}" class="item-sub" text-anchor="middle">Półka 100cm: zapasy chemii</text>
    
    <!-- Moduł 2: 100 cm (Środek - Garderoba) -->
    <line x1="{x_pax58 + 200*sc}" y1="{oy}" x2="{x_pax58 + 200*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_pax58 + 100*sc}" y1="{oy + 36*sc}" x2="{x_pax58 + 200*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Walizka czerwona</text>
    <!-- Drążek 100 cm -->
    <rect x="{x_pax58 + 104*sc}" y="{oy + 40*sc}" width="{92*sc}" height="{115*sc}" class="hanging-area"/>
    <line x1="{x_pax58 + 110*sc}" y1="{oy + 55*sc}" x2="{x_pax58 + 190*sc}" y2="{oy + 55*sc}" class="rod"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 100*sc}" class="item-text" fill="#7E22CE" text-anchor="middle">DRĄŻEK 100 cm (Koszule / Garnitury)</text>
    <!-- 3 szuflady + kosz -->
    <rect x="{x_pax58 + 104*sc}" y="{oy + 160*sc}" width="{92*sc}" height="{16*sc}" class="drawer"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 172*sc}" class="item-sub" text-anchor="middle">Szuflada KOMPLEMENT 1</text>
    <rect x="{x_pax58 + 104*sc}" y="{oy + 178*sc}" width="{92*sc}" height="{16*sc}" class="drawer"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 190*sc}" class="item-sub" text-anchor="middle">Szuflada KOMPLEMENT 2</text>
    <rect x="{x_pax58 + 104*sc}" y="{oy + 196*sc}" width="{92*sc}" height="{16*sc}" class="drawer"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 208*sc}" class="item-sub" text-anchor="middle">Szuflada KOMPLEMENT 3</text>
    <rect x="{x_pax58 + 104*sc}" y="{oy + 214*sc}" width="{92*sc}" height="{16*sc}" class="basket"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 226*sc}" class="item-sub" text-anchor="middle">Kosz druciany KOMPLEMENT</text>
    
    <!-- Moduł 3: 50 cm (AGD) -->
    <line x1="{x_pax58 + 250*sc}" y1="{oy}" x2="{x_pax58 + 250*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Pawlacz</text>
    <line x1="{x_pax58 + 200*sc}" y1="{oy + 36*sc}" x2="{x_pax58 + 250*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <rect x="{x_pax58 + 204*sc}" y="{oy + 40*sc}" width="{42*sc}" height="{130*sc}" fill="#F1F5F9" stroke="#94A3B8" stroke-dasharray="2,2"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 85*sc}" class="item-sub" font-weight="700" text-anchor="middle">ODKURZACZ</text>
    <text x="{x_pax58 + 225*sc}" y="{oy + 100*sc}" class="item-sub" font-weight="700" text-anchor="middle">DRABINA</text>
    <text x="{x_pax58 + 225*sc}" y="{oy + 115*sc}" class="item-sub" font-weight="700" text-anchor="middle">PARKSIDE</text>
    <rect x="{x_pax58 + 204*sc}" y="{oy + 175*sc}" width="{42*sc}" height="{18*sc}" class="basket"/>
    <rect x="{x_pax58 + 204*sc}" y="{oy + 196*sc}" width="{42*sc}" height="{35*sc}" fill="#E2E8F0"/>
    
    <!-- Moduł 4: 20 cm (Deska) -->
    <text x="{x_pax58 + 260*sc}" y="{oy + 22*sc}" class="item-sub" font-size="8" text-anchor="middle">Żelazko</text>
    <line x1="{x_pax58 + 250*sc}" y1="{oy + 36*sc}" x2="{x_pax58 + 270*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 260*sc}" y="{oy + h_pax/2}" class="item-sub" font-size="9" font-weight="700" text-anchor="middle" transform="rotate(-90 {x_pax58 + 260*sc} {oy + h_pax/2})">DESKA DO PRASOWANIA</text>
    
    <!-- 2. NOWY PAX 35 CM (W ŚRODKU) -->
    <rect x="{x_pax35}" y="{oy}" width="{w_pax35}" height="{h_pax}" class="corp-frame" />
    <rect x="{x_pax35}" y="{oy-28}" width="{w_pax35}" height="24" fill="#0284C7" rx="4"/>
    <text x="{x_pax35 + w_pax35/2}" y="{oy-12}" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">2. NOWY PAX 35 cm (szer. 150 cm, gł. 35/44 cm)</text>
    
    <line x1="{x_pax35 + 75*sc}" y1="{oy}" x2="{x_pax35 + 75*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <!-- Lewy 75 cm: Buty -->
    <line x1="{x_pax35}" y1="{oy + 36*sc}" x2="{x_pax35 + 75*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Pudła SKUBB</text>
    
    <!-- 6 angled shoe lines -->
    '''
    sh_step_pan = (h_pax - 36*sc - 20) / 6.0
    for i in range(6):
        y_s = oy + 36*sc + i * sh_step_pan
        svg += f'''
        <line x1="{x_pax35 + 8}" y1="{y_s + 8}" x2="{x_pax35 + 75*sc - 8}" y2="{y_s + sh_step_pan - 4}" stroke="#0284C7" stroke-width="2"/>
        <text x="{x_pax35 + 37.5*sc}" y="{y_s + sh_step_pan/2 + 2}" class="item-sub" font-size="8.5" text-anchor="middle">Półka skośna {i+1} (r. 44-45)</text>
        '''
        
    svg += f'''
    <!-- Prawy 75 cm: Wieszak wysuwany + szuflady + buty -->
    <line x1="{x_pax35 + 75*sc}" y1="{oy + 36*sc}" x2="{x_pax35 + 150*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Pudła SKUBB</text>
    
    <rect x="{x_pax35 + 78*sc}" y="{oy + 40*sc}" width="{70*sc}" height="{85*sc}" class="hanging-area"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 85*sc}" class="item-text" font-size="10" fill="#7E22CE" text-anchor="middle">WIESZAK WYSUWANY</text>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 98*sc}" class="item-sub" text-anchor="middle">5-6 kurtek lekkich</text>
    
    <!-- Szuflady -->
    <rect x="{x_pax35 + 78*sc}" y="{oy + 130*sc}" width="{70*sc}" height="{16*sc}" class="drawer"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 141*sc}" class="item-sub" text-anchor="middle">Szuflada 1: akcesoria</text>
    <rect x="{x_pax35 + 78*sc}" y="{oy + 148*sc}" width="{70*sc}" height="{16*sc}" class="drawer"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 159*sc}" class="item-sub" text-anchor="middle">Szuflada 2: pasty/buty</text>
    
    <!-- 3 półki na buty -->
    '''
    sh_step_pan_r = (h_pax - 170*sc) / 3.0
    for i in range(3):
        y_sr = oy + 168*sc + i * sh_step_pan_r
        svg += f'''
        <line x1="{x_pax35 + 75*sc + 8}" y1="{y_sr + 6}" x2="{x_pax35 + 150*sc - 8}" y2="{y_sr + sh_step_pan_r - 4}" stroke="#0284C7" stroke-width="2"/>
        <text x="{x_pax35 + 112.5*sc}" y="{y_sr + sh_step_pan_r/2 + 2}" class="item-sub" font-size="8.5" text-anchor="middle">Półka skośna {i+7}</text>
        '''
        
    svg += f'''
    <!-- 3. SZAFA NA WYMIAR (PO PRAWEJ PRZY WEJŚCIU) -->
    <rect x="{x_wymiar}" y="{oy}" width="{w_wymiar}" height="{h_wymiar}" class="corp-frame" />
    <rect x="{x_wymiar}" y="{oy-28}" width="{w_wymiar}" height="24" fill="#7E22CE" rx="4"/>
    <text x="{x_wymiar + w_wymiar/2}" y="{oy-12}" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">3. SZAFA WEJŚCIOWA (szer. 125 cm, gł. 62 cm)</text>
    
    <!-- Blenda lewa 12cm, lewa 50cm, podział 2cm, prawa 51cm, blenda prawa 10cm -->
    <line x1="{x_wymiar + 12*sc}" y1="{oy}" x2="{x_wymiar + 12*sc}" y2="{oy + h_wymiar}" stroke="#94A3B8" stroke-dasharray="2,2"/>
    <line x1="{x_wymiar + 64*sc}" y1="{oy}" x2="{x_wymiar + 64*sc}" y2="{oy + h_wymiar}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_wymiar + 115*sc}" y1="{oy}" x2="{x_wymiar + 115*sc}" y2="{oy + h_wymiar}" stroke="#94A3B8" stroke-dasharray="2,2"/>
    
    <!-- Pawlacze -->
    <line x1="{x_wymiar}" y1="{oy + 45*sc}" x2="{x_wymiar + w_wymiar}" y2="{oy + 45*sc}" class="shelf"/>
    <text x="{x_wymiar + 38*sc}" y="{oy + 26*sc}" class="item-sub" text-anchor="middle">Pawlacz 50cm</text>
    <text x="{x_wymiar + 89*sc}" y="{oy + 26*sc}" class="item-sub" text-anchor="middle">Nadstawka 51cm</text>
    
    <!-- Strefa wieszania długich płaszczy 160 cm -->
    <rect x="{x_wymiar + 14*sc}" y="{oy + 48*sc}" width="{48*sc}" height="{156*sc}" class="hanging-area"/>
    <line x1="{x_wymiar + 18*sc}" y1="{oy + 65*sc}" x2="{x_wymiar + 60*sc}" y2="{oy + 65*sc}" class="rod"/>
    <text x="{x_wymiar + 38*sc}" y="{oy + 105*sc}" class="item-text" font-size="10" fill="#7E22CE" text-anchor="middle">DRĄŻEK 160 cm</text>
    <text x="{x_wymiar + 38*sc}" y="{oy + 120*sc}" class="item-text" font-size="9" text-anchor="middle">DŁUGIE PŁASZCZE</text>
    <text x="{x_wymiar + 38*sc}" y="{oy + 135*sc}" class="item-sub" font-size="8.5" text-anchor="middle">i trencze zimowe</text>
    
    <!-- Dolna szuflada -->
    <line x1="{x_wymiar + 12*sc}" y1="{oy + 205*sc}" x2="{x_wymiar + 64*sc}" y2="{oy + 205*sc}" class="shelf"/>
    <rect x="{x_wymiar + 14*sc}" y="{oy + 208*sc}" width="{48*sc}" height="{30*sc}" class="drawer"/>
    <text x="{x_wymiar + 38*sc}" y="{oy + 224*sc}" class="item-sub" text-anchor="middle">Szuflada 35cm</text>
    
    <!-- Regał obuwniczy (prawa kolumna 51 cm) -->
    '''
    sh_step_w = (h_wymiar - 45*sc) / 8.0
    for i in range(8):
        y_w = oy + 45*sc + i * sh_step_w
        if i < 7:
            svg += f'<line x1="{x_wymiar + 64*sc}" y1="{y_w + sh_step_w}" x2="{x_wymiar + 115*sc}" y2="{y_w + sh_step_w}" class="shelf"/>'
        label = "Czapki / szale" if i < 3 else f"Buty bieżące {i-2}"
        svg += f'<text x="{x_wymiar + 89*sc}" y="{y_w + sh_step_w/2 + 3}" class="item-sub" font-size="8.5" text-anchor="middle">{label}</text>'
        
    # DIMENSION LABELS ACROSS BOTTOM
    svg += f'''
    <g transform="translate(0, {oy + h_wymiar + 35})">
        {h_dim(x_pax58, x_pax58 + w_pax58, 0, "SZEROKOŚĆ PAX 58: 270 cm", 0)}
        {h_dim(x_pax35, x_pax35 + w_pax35, 0, "NOWY PAX 35: 150 cm", 0)}
        {h_dim(x_wymiar, x_wymiar + w_wymiar, 0, "NA WYMIAR: 125 cm", 0)}
    </g>
    '''
    
    svg += '</svg>'
    
    with open(f"{OUT_DIR}/01_panorama_wariantu_1.svg", "w") as f:
        f.write(svg)
    render_svg_to_png(f"{OUT_DIR}/01_panorama_wariantu_1.svg", f"{OUT_DIR}/01_panorama_wariantu_1.png", svg_w, svg_h)

# Execute all generators
gen_nowy_pax_35()
gen_istniejacy_pax_58()
gen_panorama()
print("All drawings generated and rendered successfully!")
