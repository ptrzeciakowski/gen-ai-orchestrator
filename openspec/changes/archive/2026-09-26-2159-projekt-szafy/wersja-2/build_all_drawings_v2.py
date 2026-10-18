import os
import subprocess

OUT_DIR = "/Users/pawel/git/gen-ai-orchestrator/sandbox/2026-09-26-projekt-szafy/wersja-2"
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
        .title { font-size: 23px; font-weight: 800; fill: #0F172A; letter-spacing: -0.5px; }
        .subtitle { font-size: 13px; font-weight: 500; fill: #475569; }
        .corp-frame { fill: #FFFFFF; stroke: #0F172A; stroke-width: 3.5; }
        .corp-inner { fill: #F8FAFC; stroke: #94A3B8; stroke-width: 1.5; }
        .shelf { fill: #FFFFFF; stroke: #334155; stroke-width: 2.5; }
        .dryer-bg { fill: #E0F2FE; stroke: #0284C7; stroke-width: 2; rx: 6px; }
        .laundry-niche { fill: #F0FDF4; stroke: #16A34A; stroke-width: 1.5; stroke-dasharray: 4,4; rx: 4px; }
        .drawer { fill: #F1F5F9; stroke: #475569; stroke-width: 2; rx: 4px; }
        .basket { fill: #F8FAFC; stroke: #64748B; stroke-width: 1.5; stroke-dasharray: 4,3; rx: 3px; }
        .shoe-shelf-bg { fill: #F1F5F9; stroke: #64748B; stroke-width: 1.5; rx: 4px; }
        .hanging-area { fill: #FAF5FF; stroke: #A855F7; stroke-width: 1.5; stroke-dasharray: 4,4; rx: 5px; }
        .guitar-area { fill: #FEF3C7; stroke: #D97706; stroke-width: 1.8; rx: 5px; }
        .dyson-area { fill: #FDF2F8; stroke: #DB2777; stroke-width: 1.8; rx: 5px; }
        .vacuum-area { fill: #F5F3FF; stroke: #7C3AED; stroke-width: 1.8; rx: 5px; }
        .ladder-area { fill: #F1F5F9; stroke: #475569; stroke-width: 1.8; rx: 4px; }
        .paper-towel-area { fill: #ECFDF5; stroke: #059669; stroke-width: 1.5; rx: 4px; }
        .backpack-area { fill: #EFF6FF; stroke: #2563EB; stroke-width: 1.5; rx: 4px; }
        .rod { stroke: #475569; stroke-width: 4; stroke-linecap: round; }
        .item-text { font-size: 11px; font-weight: 700; fill: #1E293B; }
        .item-sub { font-size: 9.5px; font-weight: 500; fill: #64748B; }
        .dim-text { font-size: 11px; font-weight: 700; fill: #DC2626; }
        .dim-title { font-size: 12.5px; font-weight: 800; fill: #DC2626; }
        .tag { font-size: 10px; font-weight: 700; fill: #FFFFFF; rx: 3px; }
        .badge-green { fill: #15803D; rx: 4px; }
        .badge-purple { fill: #7E22CE; rx: 4px; }
        .badge-amber { fill: #B45309; rx: 4px; }
        .badge-blue { fill: #1D4ED8; rx: 4px; }
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
# 1. SZAFA NA WYMIAR (WEJŚCIE) – 100% BEZ ZMIAN (JEDYNA BAZA OBUWNICZA)
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
    
    <text x="{ox}" y="42" class="title">SZAFA NA WYMIAR PRZY WEJŚCIU – BEZ ZMIAN</text>
    <text x="{ox}" y="66" class="subtitle">Wnęka 125 cm × głębokość 62 cm | Lewa: Długie płaszcze (160 cm luzu) | Prawa: Regał obuwniczy (JEDYNA baza butów w domu)</text>
    
    <rect x="{ox}" y="85" width="460" height="28" fill="#FEF3C7" stroke="#D97706" rx="4"/>
    <text x="{ox + 230}" y="103" fill="#B45309" font-size="11.5" font-weight="700" text-anchor="middle">ZAŁOŻENIE WERSJI 2: ZACHOWANIE 100% AKTUALNEJ ZABUDOWY NA BUTY</text>
    
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
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top + 104}" class="item-sub" text-anchor="middle">trencze, kurtki puchowe, marynarki</text>
    
    <rect x="{x_c1 + 18}" y="{oy + h_top + h_hang/2 - 22}" width="{w_c1 - 36}" height="44" fill="#EDE9FE" stroke="#A855F7" stroke-width="1.5" rx="6"/>
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top + h_hang/2}" class="item-text" fill="#6B21A8" font-size="12" text-anchor="middle">160 cm W ŚWIETLE</text>
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top + h_hang/2 + 15}" class="item-sub" fill="#7E22CE" text-anchor="middle">płaszcz wisi prosto bez zaginania!</text>
    
    <text x="{x_c1 + w_c1/2}" y="{oy + h_top + h_hang - 25}" class="item-sub" text-anchor="middle">Dno: wolne / plecak podręczny / torba</text>
    
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
    <text x="{x_c2 + w_c/2}" y="{oy + h_top/2}" class="item-text" text-anchor="middle">NADSTAWKA Z PRZEGRÓDKAMI (45 cm)</text>
    <text x="{x_c2 + w_c/2}" y="{oy + h_top/2 + 15}" class="item-sub" text-anchor="middle">pudła / dokumenty / segregatory</text>
    <line x1="{x_c2}" y1="{oy + h_top}" x2="{x_c2 + w_c}" y2="{oy + h_top}" class="shelf" />
    '''
    
    sh_heights = [26, 22, 22, 24, 24, 24, 24, 29]
    cur_y = oy + h_top
    shelf_labels = [
        ("PÓŁKA 1 (26 cm)", "pudełko z akcesoriami / drobiazgi"),
        ("PÓŁKA 2 (22 cm)", "szaliki, rękawiczki, kominy"),
        ("PÓŁKA 3 (22 cm)", "klucze, portfele, okulary"),
        ("PÓŁKA 4 – BUTY (24 cm)", "bieżące sneakersy / obuwie sportowe"),
        ("PÓŁKA 5 – BUTY (24 cm)", "półbuty codzienne domowników"),
        ("PÓŁKA 6 – BUTY (24 cm)", "buty wyjściowe / sneakersy"),
        ("PÓŁKA 7 – BUTY (24 cm)", "kapcie domowe / sandały"),
        ("DNO REGAŁU (29 cm)", "wyższe trzewiki / trapery zimowe")
    ]
    
    for i, (h_cm, (title, sub)) in enumerate(zip(sh_heights, shelf_labels)):
        h_px = h_cm * sc
        is_shoe = i >= 3
        bg = "#EFF6FF" if is_shoe else "#F8FAFC"
        border_st = 'stroke="#3B82F6" stroke-width="1"' if is_shoe else ''
        svg += f'''
        <rect x="{x_c2+4}" y="{cur_y+2}" width="{w_c-8}" height="{h_px-4}" fill="{bg}" {border_st} rx="3"/>
        <text x="{x_c2 + w_c/2}" y="{cur_y + h_px/2 - 2}" class="item-text" text-anchor="middle">{title}</text>
        <text x="{x_c2 + w_c/2}" y="{cur_y + h_px/2 + 11}" class="item-sub" text-anchor="middle">{sub}</text>
        '''
        cur_y += h_px
        if i < len(sh_heights) - 1:
            svg += f'<line x1="{x_c2}" y1="{cur_y}" x2="{x_c2 + w_c}" y2="{cur_y}" class="shelf" />'
            
    # DIMENSIONS
    svg += h_dim(ox, ox + w_tot, oy, "CAŁKOWITA SZEROKOŚĆ WNĘKI: 125 cm", -45)
    svg += h_dim(x_c1, x_c1 + w_c1, oy, "LEWA: 50 cm", -18)
    svg += h_dim(x_c2, x_c2 + w_c, oy, "PRAWA: 51 cm", -18)
    
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
# 2. NOWY PAX 35 CM (150 CM = 2 × 75 CM) – WARIANT 1
# ==============================================================================
def gen_nowy_pax_35_w1():
    sc = 3.6
    ox, oy = 175, 145
    w_tot = 150 * sc
    h_tot = 236 * sc
    w_c = 75 * sc
    x_c1, x_c2 = ox, ox + w_c
    h_paw = 36 * sc
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 1120" width="950" height="1120" style="background:#FFFFFF;">
    {COMMON_STYLES}
    
    <text x="{ox}" y="42" class="title">NOWY PAX 35 cm (2 × 75 cm) – WARIANT 1 (REKOMENDOWANY)</text>
    <text x="{ox}" y="66" class="subtitle">Zero butów! | Komoda szufladowa na czapki i rękawiczki | Półki na plecaki, zgrzewki ręczników i drobne AGD</text>
    
    <rect x="{ox}" y="85" width="540" height="28" fill="#ECFDF5" stroke="#10B981" rx="4"/>
    <text x="{ox + 270}" y="103" fill="#065F46" font-size="11.5" font-weight="700" text-anchor="middle">5 DUŻYCH SZUFLAD 75×35 cm + ZAPASY AGD I PAPIERU + PLECAKI</text>
    
    <rect x="{ox}" y="{oy}" width="{w_tot}" height="{h_tot}" class="corp-frame" />
    <line x1="{x_c2}" y1="{oy}" x2="{x_c2}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    
    <!-- LEWY MODUŁ 75 CM -->
    <rect x="{x_c1+6}" y="{oy+6}" width="{w_c-12}" height="{h_paw-10}" fill="#F8FAFC" rx="4"/>
    <text x="{x_c1 + w_c/2}" y="{oy + h_paw/2}" class="item-text" text-anchor="middle">PAWLACZ: PÓŁKA 75×35 cm (36 cm)</text>
    <text x="{x_c1 + w_c/2}" y="{oy + h_paw/2 + 15}" class="item-sub" text-anchor="middle">pudła SKUBB z rzeczami sezonowymi</text>
    <line x1="{x_c1}" y1="{oy + h_paw}" x2="{x_c2}" y2="{oy + h_paw}" class="shelf" />
    
    <!-- Półka 1: Zgrzewki ręczników papierowych (32 cm) -->
    '''
    h_p1 = 32 * sc
    y_p1 = oy + h_paw
    h_p2 = 36 * sc
    y_p2 = y_p1 + h_p1
    
    svg += f'''
    <rect x="{x_c1+6}" y="{y_p1+4}" width="{w_c-12}" height="{h_p1-8}" class="paper-towel-area" />
    <text x="{x_c1 + w_c/2}" y="{y_p1 + h_p1/2 - 3}" class="item-text" fill="#047857" text-anchor="middle">RĘCZNIKI PAPIEROWE (ZGRZEWKI)</text>
    <text x="{x_c1 + w_c/2}" y="{y_p1 + h_p1/2 + 13}" class="item-sub" fill="#065F46" text-anchor="middle">zapas 2 wielkich zgrzewek (głębokość 35 cm idealna na rolki)</text>
    <line x1="{x_c1}" y1="{y_p1 + h_p1}" x2="{x_c2}" y2="{y_p1 + h_p1}" class="shelf" />
    
    <!-- Półka 2: Plecaki podręczne / szkolne (36 cm) -->
    <rect x="{x_c1+6}" y="{y_p2+4}" width="{w_c-12}" height="{h_p2-8}" class="backpack-area" />
    <text x="{x_c1 + w_c/2}" y="{y_p2 + h_p2/2 - 3}" class="item-text" fill="#1D4ED8" text-anchor="middle">PLECAKI I TORBY CODZIENNE</text>
    <text x="{x_c1 + w_c/2}" y="{y_p2 + h_p2/2 + 13}" class="item-sub" fill="#1E40AF" text-anchor="middle">miejsce na 4-5 plecaków stojących swobodnie bez gniecenia</text>
    <line x1="{x_c1}" y1="{y_p2 + h_p2}" x2="{x_c2}" y2="{y_p2 + h_p2}" class="shelf" />
    '''
    
    h_dr = 20 * sc
    y_dr1 = y_p2 + h_p2
    y_dr2 = y_dr1 + h_dr
    y_dr3 = y_dr2 + h_dr
    
    svg += f'''
    <!-- Szuflada 1 -->
    <rect x="{x_c1+6}" y="{y_dr1+4}" width="{w_c-12}" height="{h_dr-8}" class="drawer" />
    <line x1="{x_c1 + w_c/2 - 35}" y1="{y_dr1 + h_dr/2}" x2="{x_c1 + w_c/2 + 35}" y2="{y_dr1 + h_dr/2}" stroke="#94A3B8" stroke-width="3" stroke-linecap="round"/>
    <text x="{x_c1 + w_c/2}" y="{y_dr1 + h_dr/2 + 14}" class="item-text" text-anchor="middle">SZUFLADA 1 (KOMPLEMENT): Czapki zimowe, kapelusze, opaski</text>
    <line x1="{x_c1}" y1="{y_dr1 + h_dr}" x2="{x_c2}" y2="{y_dr1 + h_dr}" class="shelf" />
    
    <!-- Szuflada 2 -->
    <rect x="{x_c1+6}" y="{y_dr2+4}" width="{w_c-12}" height="{h_dr-8}" class="drawer" />
    <line x1="{x_c1 + w_c/2 - 35}" y1="{y_dr2 + h_dr/2}" x2="{x_c1 + w_c/2 + 35}" y2="{y_dr2 + h_dr/2}" stroke="#94A3B8" stroke-width="3" stroke-linecap="round"/>
    <text x="{x_c1 + w_c/2}" y="{y_dr2 + h_dr/2 + 14}" class="item-text" text-anchor="middle">SZUFLADA 2 (KOMPLEMENT): Rękawiczki, szale, kominy, apaszki</text>
    <line x1="{x_c1}" y1="{y_dr2 + h_dr}" x2="{x_c2}" y2="{y_dr2 + h_dr}" class="shelf" />
    
    <!-- Szuflada 3 -->
    <rect x="{x_c1+6}" y="{y_dr3+4}" width="{w_c-12}" height="{h_dr-8}" class="drawer" />
    <line x1="{x_c1 + w_c/2 - 35}" y1="{y_dr3 + h_dr/2}" x2="{x_c1 + w_c/2 + 35}" y2="{y_dr3 + h_dr/2}" stroke="#94A3B8" stroke-width="3" stroke-linecap="round"/>
    <text x="{x_c1 + w_c/2}" y="{y_dr3 + h_dr/2 + 14}" class="item-text" text-anchor="middle">SZUFLADA 3 (KOMPLEMENT): Drobne AGD, golarki ubrań, ładowarki</text>
    <line x1="{x_c1}" y1="{y_dr3 + h_dr}" x2="{x_c2}" y2="{y_dr3 + h_dr}" class="shelf" />
    
    <!-- Dno lewe -->
    <rect x="{x_c1+6}" y="{y_dr3 + h_dr + 4}" width="{w_c-12}" height="{(oy + h_tot) - (y_dr3 + h_dr) - 8}" fill="#F8FAFC" rx="3"/>
    <text x="{x_c1 + w_c/2}" y="{y_dr3 + h_dr + 25}" class="item-text" text-anchor="middle">DNO / PÓŁKA DOLNA: Worki do odkurzacza / filtry</text>
    <text x="{x_c1 + w_c/2}" y="{y_dr3 + h_dr + 40}" class="item-sub" text-anchor="middle">zapasowe akcesoria do sprzętów domowych</text>
    '''
    
    # PRAWY MODUŁ 75 CM
    h_hanger = 85 * sc
    y_h_start = oy + h_paw
    
    svg += f'''
    <rect x="{x_c2+6}" y="{oy+6}" width="{w_c-12}" height="{h_paw-10}" fill="#F8FAFC" rx="4"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw/2}" class="item-text" text-anchor="middle">PAWLACZ: PÓŁKA 75×35 cm (36 cm)</text>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw/2 + 15}" class="item-sub" text-anchor="middle">pudła SKUBB na akcesoria zapasowe</text>
    <line x1="{x_c2}" y1="{oy + h_paw}" x2="{ox + w_tot}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_c2+8}" y="{y_h_start+6}" width="{w_c-16}" height="{h_hanger-12}" class="hanging-area" />
    <line x1="{x_c2 + w_c/2}" y1="{y_h_start + 15}" x2="{x_c2 + w_c/2}" y2="{y_h_start + 65}" stroke="#475569" stroke-width="5" stroke-linecap="round"/>
    <rect x="{x_c2 + w_c/2 - 25}" y="{y_h_start + 12}" width="50" height="12" fill="#334155" rx="3"/>
    <text x="{x_c2 + w_c/2}" y="{y_h_start + 21}" fill="#FFFFFF" font-size="8" font-weight="700" text-anchor="middle">WYSUW</text>
    
    <text x="{x_c2 + w_c/2}" y="{y_h_start + 95}" class="item-text" fill="#7E22CE" font-size="12" text-anchor="middle">WYSUWANY WIESZAK KOMPLEMENT</text>
    <text x="{x_c2 + w_c/2}" y="{y_h_start + 115}" class="item-text" text-anchor="middle">5–6 LEKKICH KURTEK CODZIENNYCH</text>
    <text x="{x_c2 + w_c/2}" y="{y_h_start + 132}" class="item-sub" text-anchor="middle">wiatrówki, ramoneski, bluzy wiszące wzdłuż</text>
    <line x1="{x_c2}" y1="{y_h_start + h_hanger}" x2="{ox + w_tot}" y2="{y_h_start + h_hanger}" class="shelf" />
    '''
    
    y_dr_r1 = y_h_start + h_hanger
    y_dr_r2 = y_dr_r1 + h_dr
    
    svg += f'''
    <rect x="{x_c2+6}" y="{y_dr_r1+4}" width="{w_c-12}" height="{h_dr-8}" class="drawer" />
    <line x1="{x_c2 + w_c/2 - 35}" y1="{y_dr_r1 + h_dr/2}" x2="{x_c2 + w_c/2 + 35}" y2="{y_dr_r1 + h_dr/2}" stroke="#94A3B8" stroke-width="3" stroke-linecap="round"/>
    <text x="{x_c2 + w_c/2}" y="{y_dr_r1 + h_dr/2 + 14}" class="item-text" text-anchor="middle">SZUFLADA 4: Ściereczki z mikrofibry, zapasy czyszczące</text>
    <line x1="{x_c2}" y1="{y_dr_r1 + h_dr}" x2="{ox + w_tot}" y2="{y_dr_r1 + h_dr}" class="shelf" />
    
    <rect x="{x_c2+6}" y="{y_dr_r2+4}" width="{w_c-12}" height="{h_dr-8}" class="drawer" />
    <line x1="{x_c2 + w_c/2 - 35}" y1="{y_dr_r2 + h_dr/2}" x2="{x_c2 + w_c/2 + 35}" y2="{y_dr_r2 + h_dr/2}" stroke="#94A3B8" stroke-width="3" stroke-linecap="round"/>
    <text x="{x_c2 + w_c/2}" y="{y_dr_r2 + h_dr/2 + 14}" class="item-text" text-anchor="middle">SZUFLADA 5: Domowa apteczka, zapasy higieniczne, baterie</text>
    <line x1="{x_c2}" y1="{y_dr_r2 + h_dr}" x2="{ox + w_tot}" y2="{y_dr_r2 + h_dr}" class="shelf" />
    '''
    
    y_p_bot1 = y_dr_r2 + h_dr
    h_p_bot = ((oy + h_tot) - y_p_bot1) / 2.0
    
    svg += f'''
    <rect x="{x_c2+6}" y="{y_p_bot1+4}" width="{w_c-12}" height="{h_p_bot-8}" fill="#F8FAFC" rx="3"/>
    <text x="{x_c2 + w_c/2}" y="{y_p_bot1 + h_p_bot/2 - 2}" class="item-text" text-anchor="middle">PÓŁKA: PAPIER TOALETOWY (ZAPAS)</text>
    <text x="{x_c2 + w_c/2}" y="{y_p_bot1 + h_p_bot/2 + 12}" class="item-sub" text-anchor="middle">zgrzewka papieru / chusteczki higieniczne</text>
    <line x1="{x_c2}" y1="{y_p_bot1 + h_p_bot}" x2="{ox + w_tot}" y2="{y_p_bot1 + h_p_bot}" class="shelf" />
    
    <rect x="{x_c2+6}" y="{y_p_bot1 + h_p_bot + 4}" width="{w_c-12}" height="{h_p_bot-8}" fill="#F8FAFC" rx="3"/>
    <text x="{x_c2 + w_c/2}" y="{y_p_bot1 + 1.5*h_p_bot - 2}" class="item-text" text-anchor="middle">DNO: ZAPASY CHEMII GOSPODARCZEJ</text>
    <text x="{x_c2 + w_c/2}" y="{y_p_bot1 + 1.5*h_p_bot + 12}" class="item-sub" text-anchor="middle">płyny do szyb, mydła, wkłady, gąbki</text>
    '''
    
    # DIMENSIONS
    svg += h_dim(ox, ox + w_tot, oy, "ŁĄCZNA SZEROKOŚĆ ŚCIANY: 150 cm", -45)
    svg += h_dim(x_c1, x_c2, oy, "MODUŁ LEWY: 75 cm", -18)
    svg += h_dim(x_c2, ox + w_tot, oy, "MODUŁ PRAWY: 75 cm", -18)
    
    svg += v_dim(oy, oy + h_tot, ox, "WYSOKOŚĆ: 236 cm", -40, anchor="end")
    svg += v_dim(oy, oy + h_paw, ox, "PAWLACZ: 36 cm", -18, anchor="end")
    svg += v_dim(y_p1, y_dr1, ox, "PÓŁKI ZAPASY: 68 cm", -18, anchor="end")
    svg += v_dim(y_dr1, y_dr3 + h_dr, ox, "3 SZUFLADY: 60 cm", -18, anchor="end")
    
    svg += v_dim(y_h_start, y_h_start + h_hanger, ox + w_tot, "WIESZAK: 85 cm", 25)
    svg += v_dim(y_dr_r1, y_dr_r2 + h_dr, ox + w_tot, "2 SZUFLADY: 40 cm", 25)
    svg += v_dim(y_p_bot1, oy + h_tot, ox + w_tot, "PÓŁKI DOLNE: 75 cm", 25)
    
    svg += '</svg>'
    
    with open(f"{OUT_DIR}/szafa_2_nowy_pax_35_wariant_1.svg", "w") as f:
        f.write(svg)
    render_svg_to_png(f"{OUT_DIR}/szafa_2_nowy_pax_35_wariant_1.svg", f"{OUT_DIR}/szafa_2_nowy_pax_35_wariant_1.png", 950, 1120)

# ==============================================================================
# 3. ISTNIEJĄCY PAX 58 CM – WARIANT 1
# ==============================================================================
def gen_istniejacy_pax_58_w1():
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
    
    <text x="{ox}" y="42" class="title">ISTNIEJĄCY PAX 58 cm (270 cm) – WARIANT 1 (REKOMENDOWANY)</text>
    <text x="{ox}" y="66" class="subtitle">Drążek nad suszarką ZOSTAJE | Wiadro + kij mopa we wnęce 31 cm | Odkurzacz Amica na dnie 100 cm | Gitara + Drabina + Dyson w 50 cm</text>
    
    <rect x="{ox}" y="85" width="680" height="28" fill="#F5F3FF" stroke="#8B5CF6" rx="4"/>
    <text x="{ox + 340}" y="103" fill="#6D28D9" font-size="11.5" font-weight="700" text-anchor="middle">ROZWIĄZANIE DLA GITARY, DRABINY, ODKURZACZY (AMICA + DYSON), WIADRA I MISEK!</text>
    
    <rect x="{ox}" y="{oy}" width="{w_tot}" height="{h_tot}" class="corp-frame" />
    <line x1="{x_m2}" y1="{oy}" x2="{x_m2}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    <line x1="{x_m3}" y1="{oy}" x2="{x_m3}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    <line x1="{x_m4}" y1="{oy}" x2="{x_m4}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    
    <!-- MODUŁ 1: 100 CM -->
    <rect x="{x_m1+4}" y="{oy+4}" width="{w_m1-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m1 + w_m1/2}" y="{oy + h_paw/2}" class="item-text" text-anchor="middle">PAWLACZ: CZARNA WALIZKA PODRÓŻNA (36 cm)</text>
    <line x1="{x_m1}" y1="{oy + h_paw}" x2="{x_m2}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_m1+6}" y="{oy + h_paw + 6}" width="{w_m1-12}" height="{95*sc - 12}" class="hanging-area" />
    <line x1="{x_m1+16}" y1="{oy + h_paw + 28}" x2="{x_m2-16}" y2="{oy + h_paw + 28}" class="rod" />
    <text x="{x_m1 + w_m1/2}" y="{oy + h_paw + 52}" class="item-text" fill="#7E22CE" font-size="12" text-anchor="middle">DRĄŻEK 100 cm NAD SUSZARKĄ (ZOSTAJE!)</text>
    <text x="{x_m1 + w_m1/2}" y="{oy + h_paw + 72}" class="item-text" text-anchor="middle">Koszule dosychające po suszeniu / kurtki codzienne</text>
    <text x="{x_m1 + w_m1/2}" y="{oy + h_paw + 88}" class="item-sub" text-anchor="middle">Wysokość wiszenia: 95 cm – swobodny zwis nad płytą suszarki</text>
    <line x1="{x_m1}" y1="{oy + h_paw + 95*sc}" x2="{x_m2}" y2="{oy + h_paw + 95*sc}" class="shelf" />
    
    <!-- Dół modułu 1: Suszarka Beko + Wnęka 31 cm -->
    <rect x="{x_m1+8}" y="{oy + h_paw + 95*sc + 10}" width="{60*sc}" height="{85*sc}" class="dryer-bg" />
    <circle cx="{x_m1 + 8 + 30*sc}" cy="{oy + h_paw + 95*sc + 10 + 42.5*sc}" r="65" fill="#BAE6FD" stroke="#0284C7" stroke-width="2.5" />
    <circle cx="{x_m1 + 8 + 30*sc}" cy="{oy + h_paw + 95*sc + 10 + 42.5*sc}" r="50" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="4,2" />
    <rect x="{x_m1 + 16}" y="{oy + h_paw + 95*sc + 18}" width="{60*sc - 16}" height="28" fill="#0284C7" rx="3" />
    <circle cx="{x_m1 + 8 + 30*sc}" cy="{oy + h_paw + 95*sc + 32}" r="8" fill="#FFFFFF" />
    <text x="{x_m1 + 8 + 30*sc}" y="{oy + h_paw + 95*sc + 10 + 42.5*sc + 5}" class="item-text" fill="#0369A1" font-size="12" text-anchor="middle">SUSZARKA BEKO</text>
    <text x="{x_m1 + 8 + 30*sc}" y="{oy + h_paw + 95*sc + 10 + 42.5*sc + 20}" class="item-sub" fill="#0284C7" text-anchor="middle">szer. 60 cm | wys. 85 cm</text>
    
    <rect x="{x_m1 + 16 + 60*sc}" y="{oy + h_paw + 95*sc + 10}" width="{31*sc}" height="{85*sc}" class="laundry-niche" />
    <rect x="{x_m1 + 20 + 60*sc}" y="{oy + h_tot - 32*sc}" width="{31*sc - 8}" height="{26*sc}" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5" rx="3"/>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc}" y="{oy + h_tot - 18*sc}" class="item-text" fill="#15803D" text-anchor="middle">WIADRO NA MOPA</text>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc}" y="{oy + h_tot - 8*sc}" class="item-sub" fill="#166534" text-anchor="middle">(szer. 28 cm pasuje idealnie!)</text>
    
    <line x1="{x_m1 + 22 + 60*sc}" y1="{oy + h_paw + 95*sc + 15}" x2="{x_m1 + 22 + 60*sc}" y2="{oy + h_tot - 34*sc}" stroke="#16A34A" stroke-width="4" stroke-linecap="round"/>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc + 8}" y="{oy + h_paw + 95*sc + 35}" class="item-text" fill="#15803D" text-anchor="middle">KIJ DO MOPA</text>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc + 8}" y="{oy + h_paw + 95*sc + 50}" class="item-sub" fill="#166534" text-anchor="middle">uchwyt ścienny</text>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc + 8}" y="{oy + h_paw + 95*sc + 75}" class="item-text" fill="#15803D" text-anchor="middle">MISKA PIONOWO</text>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc + 8}" y="{oy + h_paw + 95*sc + 90}" class="item-sub" fill="#166534" text-anchor="middle">+ płyny / proszki</text>
    
    <!-- MODUŁ 2: 100 CM -->
    <rect x="{x_m2+4}" y="{oy+4}" width="{w_m2-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw/2}" class="item-text" text-anchor="middle">PAWLACZ: CZERWONA DUŻA WALIZKA (36 cm)</text>
    <line x1="{x_m2}" y1="{oy + h_paw}" x2="{x_m3}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_m2+6}" y="{oy + h_paw + 6}" width="{w_m2-12}" height="{115*sc - 12}" class="hanging-area" />
    <line x1="{x_m2+16}" y1="{oy + h_paw + 28}" x2="{x_m3-16}" y2="{oy + h_paw + 28}" class="rod" />
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 55}" class="item-text" fill="#7E22CE" font-size="12" text-anchor="middle">DRĄŻEK 100 cm: GŁÓWNA GARDEROBA (ZOSTAJE!)</text>
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 75}" class="item-text" text-anchor="middle">Garnitury w pokrowcach, koszule, marynarki, spodnie</text>
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 92}" class="item-sub" text-anchor="middle">Wysokość wiszenia 115 cm (głębokość 58 cm – brak zagnieceń)</text>
    <line x1="{x_m2}" y1="{oy + h_paw + 115*sc}" x2="{x_m3}" y2="{oy + h_paw + 115*sc}" class="shelf" />
    
    <rect x="{x_m2+6}" y="{oy + h_paw + 115*sc + 3}" width="{w_m2-12}" height="{16*sc - 6}" class="drawer" />
    <line x1="{x_m2 + w_m2/2 - 35}" y1="{oy + h_paw + 115*sc + 8*sc}" x2="{x_m2 + w_m2/2 + 35}" y2="{oy + h_paw + 115*sc + 8*sc}" stroke="#94A3B8" stroke-width="3" stroke-linecap="round"/>
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 115*sc + 8*sc + 13}" class="item-text" text-anchor="middle">SZUFLADA 1 (KOMPLEMENT 100 cm): Bielizna osobista i skarpetki</text>
    <line x1="{x_m2}" y1="{oy + h_paw + 131*sc}" x2="{x_m3}" y2="{oy + h_paw + 131*sc}" class="shelf" />
    
    <!-- Dolna wnęka gospodarcza 100 cm -->
    <rect x="{x_m2+6}" y="{oy + h_paw + 131*sc + 4}" width="{w_m2-12}" height="{(h_tot - (h_paw + 131*sc)) - 8}" class="vacuum-area" />
    <rect x="{x_m2+16}" y="{oy + h_paw + 131*sc + 14}" width="{52*sc}" height="{(h_tot - (h_paw + 131*sc)) - 28}" fill="#EDE9FE" stroke="#7C3AED" stroke-width="1.5" rx="5"/>
    <text x="{x_m2 + 16 + 26*sc}" y="{oy + h_paw + 131*sc + 38}" class="item-text" fill="#6D28D9" font-size="12" text-anchor="middle">ODKURZACZ TRADYCYJNY AMICA</text>
    <text x="{x_m2 + 16 + 26*sc}" y="{oy + h_paw + 131*sc + 56}" class="item-sub" fill="#7C3AED" text-anchor="middle">strefa szer. 55 cm | z wężem i szczotką</text>
    
    <rect x="{x_m2 + 20 + 52*sc}" y="{oy + h_paw + 131*sc + 14}" width="{w_m2 - 52*sc - 32}" height="{(h_tot - (h_paw + 131*sc)) - 28}" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5" rx="5"/>
    <text x="{x_m2 + 20 + 52*sc + (w_m2 - 52*sc - 32)/2}" y="{oy + h_paw + 131*sc + 38}" class="item-text" fill="#15803D" font-size="12" text-anchor="middle">MISKI GOSPODARCZE</text>
    <text x="{x_m2 + 20 + 52*sc + (w_m2 - 52*sc - 32)/2}" y="{oy + h_paw + 131*sc + 56}" class="item-sub" fill="#166534" text-anchor="middle">włożone jedna w drugą</text>
    <text x="{x_m2 + 20 + 52*sc + (w_m2 - 52*sc - 32)/2}" y="{oy + h_paw + 131*sc + 72}" class="item-sub" fill="#166534" text-anchor="middle">+ kosze z praniem</text>
    
    <!-- MODUŁ 3: 50 CM (Gitara + Drabina + Dyson + Narzędzia) -->
    <rect x="{x_m3+4}" y="{oy+4}" width="{w_m3-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m3 + w_m3/2}" y="{oy + h_paw/2 + 5}" class="item-text" text-anchor="middle">PAWLACZ</text>
    <line x1="{x_m3}" y1="{oy + h_paw}" x2="{x_m4}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_m3+6}" y="{oy + h_paw + 6}" width="{w_m3-12}" height="{135*sc - 12}" class="corp-inner" />
    
    <!-- Gitara -->
    <rect x="{x_m3+8}" y="{oy + h_paw + 8}" width="{23*sc}" height="{135*sc - 16}" class="guitar-area" />
    <text x="{x_m3 + 8 + 11.5*sc}" y="{oy + h_paw + 30}" class="item-text" fill="#B45309" text-anchor="middle">GITARA</text>
    <text x="{x_m3 + 8 + 11.5*sc}" y="{oy + h_paw + 46}" class="item-sub" fill="#92400E" text-anchor="middle">w pokrowcu</text>
    <text x="{x_m3 + 8 + 11.5*sc}" y="{oy + h_paw + 62}" class="item-sub" fill="#92400E" text-anchor="middle">bezpieczna</text>
    <text x="{x_m3 + 8 + 11.5*sc}" y="{oy + h_paw + 78}" class="item-sub" fill="#92400E" text-anchor="middle">pionowo</text>
    
    <!-- Drabina -->
    <rect x="{x_m3 + 10 + 23*sc}" y="{oy + h_paw + 8}" width="{12*sc}" height="{135*sc - 16}" class="ladder-area" />
    <text x="{x_m3 + 10 + 29*sc}" y="{oy + h_paw + 67.5*sc - 10}" class="item-text" text-anchor="middle" transform="rotate(-90 {x_m3 + 10 + 29*sc} {oy + h_paw + 67.5*sc - 10})">DRABINA ALUMINIOWA</text>
    
    <!-- Dyson -->
    <rect x="{x_m3 + 12 + 35*sc}" y="{oy + h_paw + 8}" width="{w_m3 - 35*sc - 20}" height="{135*sc - 16}" class="dyson-area" />
    <text x="{x_m3 + 12 + 35*sc + (w_m3 - 35*sc - 20)/2}" y="{oy + h_paw + 30}" class="item-text" fill="#BE185D" text-anchor="middle">DYSON</text>
    <text x="{x_m3 + 12 + 35*sc + (w_m3 - 35*sc - 20)/2}" y="{oy + h_paw + 46}" class="item-sub" fill="#9D174D" text-anchor="middle">stacja ścienna</text>
    
    <line x1="{x_m3}" y1="{oy + h_paw + 135*sc}" x2="{x_m4}" y2="{oy + h_paw + 135*sc}" class="shelf" />
    
    <!-- Półki narzędziowe Parkside -->
    <rect x="{x_m3+6}" y="{oy + h_paw + 135*sc + 4}" width="{w_m3-12}" height="{20*sc}" fill="#F1F5F9" rx="3"/>
    <text x="{x_m3 + w_m3/2}" y="{oy + h_paw + 135*sc + 16}" class="item-text" text-anchor="middle">WALIZKA PARKSIDE 1</text>
    <line x1="{x_m3}" y1="{oy + h_paw + 157*sc}" x2="{x_m4}" y2="{oy + h_paw + 157*sc}" class="shelf" />
    
    <rect x="{x_m3+6}" y="{oy + h_paw + 157*sc + 4}" width="{w_m3-12}" height="{20*sc}" fill="#F1F5F9" rx="3"/>
    <text x="{x_m3 + w_m3/2}" y="{oy + h_paw + 157*sc + 16}" class="item-text" text-anchor="middle">SKRZYNKA PARKSIDE 2</text>
    <line x1="{x_m3}" y1="{oy + h_paw + 179*sc}" x2="{x_m4}" y2="{oy + h_paw + 179*sc}" class="shelf" />
    
    <rect x="{x_m3+6}" y="{oy + h_paw + 179*sc + 4}" width="{w_m3-12}" height="{20*sc}" class="basket"/>
    <text x="{x_m3 + w_m3/2}" y="{oy + h_paw + 179*sc + 16}" class="item-sub" font-weight="700" text-anchor="middle">Kosz druciany KOMPLEMENT</text>
    
    <!-- MODUŁ 4: 20 CM -->
    <rect x="{x_m4+4}" y="{oy+4}" width="{w_m4-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_paw/2 - 4}" class="item-text" font-size="10" text-anchor="middle">ŻELAZ-</text>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_paw/2 + 10}" class="item-text" font-size="10" text-anchor="middle">KO</text>
    <line x1="{x_m4}" y1="{oy + h_paw}" x2="{ox + w_tot}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_m4+4}" y="{oy + h_paw + 6}" width="{w_m4-8}" height="{h_tot - h_paw - 12}" fill="#F8FAFC" stroke="#94A3B8" stroke-dasharray="2,2" rx="3"/>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_tot/2}" class="item-text" font-size="10" text-anchor="middle" transform="rotate(-90 {x_m4 + w_m4/2} {oy + h_tot/2})">DESKA DO PRASOWANIA</text>
    
    {h_dim(ox, ox + w_tot, oy, "ŁĄCZNA SZEROKOŚĆ ZABUDOWY PAX 58: 270 cm", -45)}
    </svg>'''
    
    with open(f"{OUT_DIR}/szafa_3_istniejacy_pax_58_wariant_1.svg", "w") as f:
        f.write(svg)
    render_svg_to_png(f"{OUT_DIR}/szafa_3_istniejacy_pax_58_wariant_1.svg", f"{OUT_DIR}/szafa_3_istniejacy_pax_58_wariant_1.png", 1260, 1080)

# ==============================================================================
# 4. PANORAMA CAŁEGO UKŁADU W JEDNEJ SKALI (WARIANT 1)
# ==============================================================================
def gen_panorama_w1():
    sc = 2.4
    ox, oy = 90, 140
    w_pax58 = 270 * sc
    gap1 = 65
    w_pax35 = 150 * sc
    gap2 = 65
    w_wymiar = 125 * sc
    
    x_pax58 = ox
    x_pax35 = x_pax58 + w_pax58 + gap1
    x_wymiar = x_pax35 + w_pax35 + gap2
    
    h_pax = 236 * sc
    h_wymiar = 240 * sc
    
    svg_w = int(x_wymiar + w_wymiar + 90)
    svg_h = int(oy + h_wymiar + 120)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}" style="background:#FFFFFF;">
    {COMMON_STYLES}
    
    <text x="{ox}" y="42" class="title">PANORAMA UKŁADU SZAF W CAŁYM MIESZKANIU – WERSJA 2 (WARIANT 1)</text>
    <text x="{ox}" y="66" class="subtitle">Wszystkie szafy narysowane w JEDNEJ wspólnej skali geometrycznej (1 cm = 2.4 px) | Widok od lewej do prawej</text>
    
    <!-- 1. PAX 58 CM (PO LEWEJ) -->
    <rect x="{x_pax58}" y="{oy}" width="{w_pax58}" height="{h_pax}" class="corp-frame" />
    <rect x="{x_pax58}" y="{oy-28}" width="{w_pax58}" height="24" fill="#0F172A" rx="4"/>
    <text x="{x_pax58 + w_pax58/2}" y="{oy-12}" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">1. ISTNIEJĄCY PAX 58 cm (szer. 270 cm, gł. 58 cm) – PRALNIA, GOSPODARSTWO &amp; GARDEROBA</text>
    
    <line x1="{x_pax58 + 100*sc}" y1="{oy}" x2="{x_pax58 + 100*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_pax58}" y1="{oy + 36*sc}" x2="{x_pax58 + 100*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 50*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Walizka czarna</text>
    
    <!-- Drążek nad suszarką -->
    <rect x="{x_pax58 + 6}" y="{oy + 40*sc}" width="{92*sc}" height="{90*sc}" class="hanging-area"/>
    <line x1="{x_pax58 + 14*sc}" y1="{oy + 55*sc}" x2="{x_pax58 + 90*sc}" y2="{oy + 55*sc}" class="rod"/>
    <text x="{x_pax58 + 50*sc}" y="{oy + 75*sc}" class="item-text" fill="#7E22CE" font-size="10" text-anchor="middle">DRĄŻEK NAD SUSZARKĄ</text>
    <text x="{x_pax58 + 50*sc}" y="{oy + 90*sc}" class="item-sub" font-size="8.5" text-anchor="middle">dosychanie / kurtki codzienne</text>
    <line x1="{x_pax58}" y1="{oy + 132*sc}" x2="{x_pax58 + 100*sc}" y2="{oy + 132*sc}" class="shelf"/>
    
    <!-- Suszarka Beko -->
    <rect x="{x_pax58 + 6}" y="{oy + 136*sc}" width="{60*sc}" height="{h_pax - 140*sc}" class="dryer-bg"/>
    <circle cx="{x_pax58 + 6 + 30*sc}" cy="{oy + 136*sc + (h_pax - 140*sc)/2}" r="45" fill="#BAE6FD" stroke="#0284C7" stroke-width="2"/>
    <text x="{x_pax58 + 6 + 30*sc}" y="{oy + 136*sc + (h_pax - 140*sc)/2 - 5}" class="item-text" fill="#0369A1" text-anchor="middle">SUSZARKA</text>
    <text x="{x_pax58 + 6 + 30*sc}" y="{oy + 136*sc + (h_pax - 140*sc)/2 + 10}" class="item-sub" fill="#0284C7" text-anchor="middle">BEKO 60cm</text>
    
    <!-- Wnęka 31 cm -->
    <rect x="{x_pax58 + 6 + 60*sc + 4}" y="{oy + 136*sc}" width="{31*sc - 6}" height="{h_pax - 140*sc}" class="laundry-niche"/>
    <text x="{x_pax58 + 6 + 60*sc + 15*sc}" y="{oy + 136*sc + 30}" class="item-sub" fill="#15803D" font-weight="700" text-anchor="middle">KIJ MOPA</text>
    <text x="{x_pax58 + 6 + 60*sc + 15*sc}" y="{oy + 136*sc + 45}" class="item-sub" fill="#15803D" font-weight="700" text-anchor="middle">MISKA PION</text>
    <text x="{x_pax58 + 6 + 60*sc + 15*sc}" y="{oy + h_pax - 20}" class="item-sub" fill="#15803D" font-weight="700" text-anchor="middle">WIADRO</text>
    
    <!-- Moduł 2: 100 cm -->
    <line x1="{x_pax58 + 200*sc}" y1="{oy}" x2="{x_pax58 + 200*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_pax58 + 100*sc}" y1="{oy + 36*sc}" x2="{x_pax58 + 200*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Walizka czerwona</text>
    
    <rect x="{x_pax58 + 104*sc}" y="{oy + 40*sc}" width="{92*sc}" height="{110*sc}" class="hanging-area"/>
    <line x1="{x_pax58 + 110*sc}" y1="{oy + 55*sc}" x2="{x_pax58 + 190*sc}" y2="{oy + 55*sc}" class="rod"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 95*sc}" class="item-text" fill="#7E22CE" text-anchor="middle">DRĄŻEK 100 cm (Garnitury / Koszule)</text>
    <line x1="{x_pax58 + 100*sc}" y1="{oy + 152*sc}" x2="{x_pax58 + 200*sc}" y2="{oy + 152*sc}" class="shelf"/>
    
    <rect x="{x_pax58 + 104*sc}" y="{oy + 155*sc}" width="{92*sc}" height="{15*sc}" class="drawer"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 165*sc}" class="item-sub" text-anchor="middle">Szuflada 100cm (bielizna / skarpetki)</text>
    <line x1="{x_pax58 + 100*sc}" y1="{oy + 172*sc}" x2="{x_pax58 + 200*sc}" y2="{oy + 172*sc}" class="shelf"/>
    
    <rect x="{x_pax58 + 104*sc}" y="{oy + 175*sc}" width="{92*sc}" height="{h_pax - 178*sc}" class="vacuum-area"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 198*sc}" class="item-text" fill="#6D28D9" text-anchor="middle">ODKURZACZ AMICA (Z WĘŻEM)</text>
    <text x="{x_pax58 + 150*sc}" y="{oy + 215*sc}" class="item-sub" fill="#7C3AED" text-anchor="middle">+ DUŻE MISKI GOSPODARCZE / KOSZE</text>
    
    <!-- Moduł 3: 50 cm -->
    <line x1="{x_pax58 + 250*sc}" y1="{oy}" x2="{x_pax58 + 250*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_pax58 + 200*sc}" y1="{oy + 36*sc}" x2="{x_pax58 + 250*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Pawlacz</text>
    
    <rect x="{x_pax58 + 203*sc}" y="{oy + 39*sc}" width="{22*sc}" height="{130*sc}" class="guitar-area"/>
    <text x="{x_pax58 + 214*sc}" y="{oy + 95*sc}" class="item-text" font-size="9" fill="#B45309" text-anchor="middle" transform="rotate(-90 {x_pax58 + 214*sc} {oy + 95*sc})">GITARA POKROWIEC</text>
    
    <rect x="{x_pax58 + 226*sc}" y="{oy + 39*sc}" width="{11*sc}" height="{130*sc}" class="ladder-area"/>
    <text x="{x_pax58 + 231.5*sc}" y="{oy + 95*sc}" class="item-sub" font-size="8" text-anchor="middle" transform="rotate(-90 {x_pax58 + 231.5*sc} {oy + 95*sc})">DRABINA</text>
    
    <rect x="{x_pax58 + 238*sc}" y="{oy + 39*sc}" width="{10*sc}" height="{130*sc}" class="dyson-area"/>
    <text x="{x_pax58 + 243*sc}" y="{oy + 95*sc}" class="item-sub" font-size="8" fill="#BE185D" text-anchor="middle" transform="rotate(-90 {x_pax58 + 243*sc} {oy + 95*sc})">DYSON</text>
    
    <line x1="{x_pax58 + 200*sc}" y1="{oy + 172*sc}" x2="{x_pax58 + 250*sc}" y2="{oy + 172*sc}" class="shelf"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 188*sc}" class="item-sub" font-size="8.5" text-anchor="middle">Parkside 1</text>
    <line x1="{x_pax58 + 200*sc}" y1="{oy + 195*sc}" x2="{x_pax58 + 250*sc}" y2="{oy + 195*sc}" class="shelf"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 210*sc}" class="item-sub" font-size="8.5" text-anchor="middle">Parkside 2</text>
    <line x1="{x_pax58 + 200*sc}" y1="{oy + 217*sc}" x2="{x_pax58 + 250*sc}" y2="{oy + 217*sc}" class="shelf"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 230*sc}" class="item-sub" font-size="8.5" text-anchor="middle">Kosz druciany</text>
    
    <!-- Moduł 4: 20 cm -->
    <text x="{x_pax58 + 260*sc}" y="{oy + 22*sc}" class="item-sub" font-size="8" text-anchor="middle">Żelazko</text>
    <line x1="{x_pax58 + 250*sc}" y1="{oy + 36*sc}" x2="{x_pax58 + 270*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 260*sc}" y="{oy + h_pax/2}" class="item-sub" font-size="9" font-weight="700" text-anchor="middle" transform="rotate(-90 {x_pax58 + 260*sc} {oy + h_pax/2})">DESKA DO PRASOWANIA</text>
    
    <!-- 2. NOWY PAX 35 CM (W ŚRODKU) -->
    <rect x="{x_pax35}" y="{oy}" width="{w_pax35}" height="{h_pax}" class="corp-frame" />
    <rect x="{x_pax35}" y="{oy-28}" width="{w_pax35}" height="24" fill="#059669" rx="4"/>
    <text x="{x_pax35 + w_pax35/2}" y="{oy-12}" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">2. NOWY PAX 35 cm – 0% BUTÓW! SZUFLADY, ZAPASY &amp; PLECAKI</text>
    
    <line x1="{x_pax35 + 75*sc}" y1="{oy}" x2="{x_pax35 + 75*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_pax35}" y1="{oy + 36*sc}" x2="{x_pax35 + 75*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Pudła SKUBB</text>
    
    <rect x="{x_pax35 + 4}" y="{oy + 38*sc}" width="{71*sc}" height="{30*sc}" class="paper-towel-area"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 55*sc}" class="item-sub" font-size="8.5" fill="#047857" font-weight="700" text-anchor="middle">RĘCZNIKI PAPIEROWE</text>
    <line x1="{x_pax35}" y1="{oy + 70*sc}" x2="{x_pax35 + 75*sc}" y2="{oy + 70*sc}" class="shelf"/>
    
    <rect x="{x_pax35 + 4}" y="{oy + 72*sc}" width="{71*sc}" height="{34*sc}" class="backpack-area"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 91*sc}" class="item-sub" font-size="8.5" fill="#1D4ED8" font-weight="700" text-anchor="middle">PLECAKI I TORBY</text>
    <line x1="{x_pax35}" y1="{oy + 108*sc}" x2="{x_pax35 + 75*sc}" y2="{oy + 108*sc}" class="shelf"/>
    
    <rect x="{x_pax35 + 4}" y="{oy + 110*sc}" width="{71*sc}" height="{18*sc}" class="drawer"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 122*sc}" class="item-sub" text-anchor="middle">Szuflada 1: Czapki</text>
    <rect x="{x_pax35 + 4}" y="{oy + 130*sc}" width="{71*sc}" height="{18*sc}" class="drawer"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 142*sc}" class="item-sub" text-anchor="middle">Szuflada 2: Rękawiczki</text>
    <rect x="{x_pax35 + 4}" y="{oy + 150*sc}" width="{71*sc}" height="{18*sc}" class="drawer"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 162*sc}" class="item-sub" text-anchor="middle">Szuflada 3: Drobne AGD</text>
    
    <line x1="{x_pax35}" y1="{oy + 170*sc}" x2="{x_pax35 + 75*sc}" y2="{oy + 170*sc}" class="shelf"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 200*sc}" class="item-sub" text-anchor="middle">Dno: Worki / filtry</text>
    
    <!-- Prawy 75 cm -->
    <line x1="{x_pax35 + 75*sc}" y1="{oy + 36*sc}" x2="{x_pax35 + 150*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Pudła SKUBB</text>
    
    <rect x="{x_pax35 + 78*sc}" y="{oy + 40*sc}" width="{70*sc}" height="{80*sc}" class="hanging-area"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 80*sc}" class="item-text" font-size="10" fill="#7E22CE" text-anchor="middle">WIESZAK WYSUWANY</text>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 94*sc}" class="item-sub" text-anchor="middle">5-6 kurtek lekkich</text>
    <line x1="{x_pax35 + 75*sc}" y1="{oy + 122*sc}" x2="{x_pax35 + 150*sc}" y2="{oy + 122*sc}" class="shelf"/>
    
    <rect x="{x_pax35 + 78*sc}" y="{oy + 125*sc}" width="{70*sc}" height="{18*sc}" class="drawer"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 137*sc}" class="item-sub" text-anchor="middle">Szuflada 4: Ściereczki / chemia</text>
    <rect x="{x_pax35 + 78*sc}" y="{oy + 145*sc}" width="{70*sc}" height="{18*sc}" class="drawer"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 157*sc}" class="item-sub" text-anchor="middle">Szuflada 5: Apteczka / baterie</text>
    <line x1="{x_pax35 + 75*sc}" y1="{oy + 165*sc}" x2="{x_pax35 + 150*sc}" y2="{oy + 165*sc}" class="shelf"/>
    
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 185*sc}" class="item-sub" font-size="8.5" text-anchor="middle">Półka: Papier toaletowy</text>
    <line x1="{x_pax35 + 75*sc}" y1="{oy + 195*sc}" x2="{x_pax35 + 150*sc}" y2="{oy + 195*sc}" class="shelf"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 215*sc}" class="item-sub" font-size="8.5" text-anchor="middle">Dno: Zapasy chemii</text>
    
    <!-- 3. SZAFA NA WYMIAR (PO PRAWEJ PRZY WEJŚCIU) -->
    <rect x="{x_wymiar}" y="{oy}" width="{w_wymiar}" height="{h_wymiar}" class="corp-frame" />
    <rect x="{x_wymiar}" y="{oy-28}" width="{w_wymiar}" height="24" fill="#7E22CE" rx="4"/>
    <text x="{x_wymiar + w_wymiar/2}" y="{oy-12}" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">3. SZAFA NA WYMIAR (125 cm) – JEDYNA BAZA BUTÓW</text>
    
    <line x1="{x_wymiar + 12*sc}" y1="{oy}" x2="{x_wymiar + 12*sc}" y2="{oy + h_wymiar}" stroke="#94A3B8" stroke-dasharray="2,2"/>
    <line x1="{x_wymiar + 64*sc}" y1="{oy}" x2="{x_wymiar + 64*sc}" y2="{oy + h_wymiar}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_wymiar + 115*sc}" y1="{oy}" x2="{x_wymiar + 115*sc}" y2="{oy + h_wymiar}" stroke="#94A3B8" stroke-dasharray="2,2"/>
    
    <line x1="{x_wymiar}" y1="{oy + 45*sc}" x2="{x_wymiar + w_wymiar}" y2="{oy + 45*sc}" class="shelf"/>
    <text x="{x_wymiar + 38*sc}" y="{oy + 26*sc}" class="item-sub" text-anchor="middle">Pawlacz 50cm</text>
    <text x="{x_wymiar + 89*sc}" y="{oy + 26*sc}" class="item-sub" text-anchor="middle">Nadstawka 51cm</text>
    
    <rect x="{x_wymiar + 14*sc}" y="{oy + 48*sc}" width="{48*sc}" height="{156*sc}" class="hanging-area"/>
    <line x1="{x_wymiar + 18*sc}" y1="{oy + 65*sc}" x2="{x_wymiar + 60*sc}" y2="{oy + 65*sc}" class="rod"/>
    <text x="{x_wymiar + 38*sc}" y="{oy + 105*sc}" class="item-text" font-size="10" fill="#7E22CE" text-anchor="middle">DRĄŻEK 160 cm</text>
    <text x="{x_wymiar + 38*sc}" y="{oy + 120*sc}" class="item-text" font-size="9" text-anchor="middle">DŁUGIE PŁASZCZE</text>
    <text x="{x_wymiar + 38*sc}" y="{oy + 135*sc}" class="item-sub" font-size="8.5" text-anchor="middle">i trencze zimowe</text>
    
    <line x1="{x_wymiar + 12*sc}" y1="{oy + 205*sc}" x2="{x_wymiar + 64*sc}" y2="{oy + 205*sc}" class="shelf"/>
    <rect x="{x_wymiar + 14*sc}" y="{oy + 208*sc}" width="{48*sc}" height="{30*sc}" class="drawer"/>
    <text x="{x_wymiar + 38*sc}" y="{oy + 224*sc}" class="item-sub" text-anchor="middle">Szuflada 35cm</text>
    
    '''
    sh_step_w = (h_wymiar - 45*sc) / 8.0
    for i in range(8):
        y_w = oy + 45*sc + i * sh_step_w
        if i < 7:
            svg += f'<line x1="{x_wymiar + 64*sc}" y1="{y_w + sh_step_w}" x2="{x_wymiar + 115*sc}" y2="{y_w + sh_step_w}" class="shelf"/>'
        label = "Czapki / szale" if i < 3 else f"BUTY BIEŻĄCE {i-2}"
        color = "#64748B" if i < 3 else "#1E40AF"
        svg += f'<text x="{x_wymiar + 89*sc}" y="{y_w + sh_step_w/2 + 3}" class="item-sub" font-size="8.5" fill="{color}" font-weight="{"700" if i>=3 else "500"}" text-anchor="middle">{label}</text>'
        
    svg += f'''
    <g transform="translate(0, {oy + h_wymiar + 35})">
        {h_dim(x_pax58, x_pax58 + w_pax58, 0, "SZEROKOŚĆ PAX 58: 270 cm", 0)}
        {h_dim(x_pax35, x_pax35 + w_pax35, 0, "NOWY PAX 35: 150 cm", 0)}
        {h_dim(x_wymiar, x_wymiar + w_wymiar, 0, "NA WYMIAR: 125 cm", 0)}
    </g>
    '''
    
    svg += '</svg>'
    
    with open(f"{OUT_DIR}/01_panorama_wersja_2_wariant_1.svg", "w") as f:
        f.write(svg)
    render_svg_to_png(f"{OUT_DIR}/01_panorama_wersja_2_wariant_1.svg", f"{OUT_DIR}/01_panorama_wersja_2_wariant_1.png", svg_w, svg_h)

# ==============================================================================
# 5. NOWY PAX 35 CM – WARIANT 2 (DYSON + MOP W PAX 35)
# ==============================================================================
def gen_nowy_pax_35_w2():
    sc = 3.6
    ox, oy = 175, 145
    w_tot = 150 * sc
    h_tot = 236 * sc
    w_c = 75 * sc
    x_c1, x_c2 = ox, ox + w_c
    h_paw = 36 * sc
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 1120" width="950" height="1120" style="background:#FFFFFF;">
    {COMMON_STYLES}
    <text x="{ox}" y="42" class="title">NOWY PAX 35 cm – WARIANT 2 (PION AGD: DYSON + MOP + SZUFLADY)</text>
    <text x="{ox}" y="66" class="subtitle">Dyson i wiadro mopa przeniesione do szafy 35 cm | W szafie PAX 58 nie ruszamy szuflad w module 100 cm!</text>
    <rect x="{ox}" y="{oy}" width="{w_tot}" height="{h_tot}" class="corp-frame" />
    <line x1="{x_c2}" y1="{oy}" x2="{x_c2}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    
    <rect x="{x_c1+6}" y="{oy+6}" width="{w_c-12}" height="{h_paw-10}" fill="#F8FAFC" rx="4"/>
    <text x="{x_c1 + w_c/2}" y="{oy + h_paw/2 + 5}" class="item-text" text-anchor="middle">PAWLACZ: RZECZY SEZONOWE (36 cm)</text>
    <line x1="{x_c1}" y1="{oy + h_paw}" x2="{x_c2}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_c1+6}" y="{oy + h_paw + 6}" width="{34*sc}" height="{120*sc}" class="dyson-area"/>
    <text x="{x_c1 + 17*sc}" y="{oy + h_paw + 30}" class="item-text" fill="#BE185D" text-anchor="middle">DYSON PIONOWY</text>
    <text x="{x_c1 + 17*sc}" y="{oy + h_paw + 46}" class="item-sub" fill="#9D174D" text-anchor="middle">stacja ścienna</text>
    <line x1="{x_c1 + 8*sc}" y1="{oy + h_paw + 55}" x2="{x_c1 + 8*sc}" y2="{oy + h_paw + 95*sc}" stroke="#16A34A" stroke-width="4" stroke-linecap="round"/>
    <text x="{x_c1 + 22*sc}" y="{oy + h_paw + 75}" class="item-sub" fill="#15803D" font-weight="700">Kij do mopa</text>
    
    <rect x="{x_c1+10}" y="{oy + h_paw + 95*sc}" width="{30*sc}" height="{23*sc}" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5" rx="3"/>
    <text x="{x_c1 + 17*sc}" y="{oy + h_paw + 109*sc}" class="item-sub" fill="#15803D" font-weight="700" text-anchor="middle">WIADRO MOPA</text>
    
    <rect x="{x_c1 + 42*sc}" y="{oy + h_paw + 6}" width="{31*sc}" height="{40*sc}" class="paper-towel-area"/>
    <text x="{x_c1 + 57.5*sc}" y="{oy + h_paw + 25}" class="item-sub" fill="#047857" font-weight="700" text-anchor="middle">Ręczniki</text>
    <text x="{x_c1 + 57.5*sc}" y="{oy + h_paw + 38}" class="item-sub" fill="#047857" font-weight="700" text-anchor="middle">papierowe</text>
    
    <rect x="{x_c1 + 42*sc}" y="{oy + h_paw + 48*sc}" width="{31*sc}" height="{36*sc}" fill="#F8FAFC" rx="3"/>
    <text x="{x_c1 + 57.5*sc}" y="{oy + h_paw + 68*sc}" class="item-sub" text-anchor="middle">Papier toalet.</text>
    
    <rect x="{x_c1 + 42*sc}" y="{oy + h_paw + 86*sc}" width="{31*sc}" height="{38*sc}" fill="#F8FAFC" rx="3"/>
    <text x="{x_c1 + 57.5*sc}" y="{oy + h_paw + 106*sc}" class="item-sub" text-anchor="middle">Zapasy chemii</text>
    
    <line x1="{x_c1}" y1="{oy + h_paw + 128*sc}" x2="{x_c2}" y2="{oy + h_paw + 128*sc}" class="shelf" />
    
    <rect x="{x_c1+6}" y="{oy + h_paw + 132*sc}" width="{w_c-12}" height="{18*sc}" class="drawer"/>
    <text x="{x_c1 + w_c/2}" y="{oy + h_paw + 144*sc}" class="item-text" text-anchor="middle">SZUFLADA 1: Ściereczki, zapasowe mopy, worki, rękawice gumowe</text>
    
    <rect x="{x_c1+6}" y="{oy + h_paw + 152*sc}" width="{w_c-12}" height="{18*sc}" class="drawer"/>
    <text x="{x_c1 + w_c/2}" y="{oy + h_paw + 164*sc}" class="item-text" text-anchor="middle">SZUFLADA 2: Akcesoria czyszczące, filtry, parownica</text>
    
    <rect x="{x_c2+6}" y="{oy+6}" width="{w_c-12}" height="{h_paw-10}" fill="#F8FAFC" rx="4"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw/2 + 5}" class="item-text" text-anchor="middle">PAWLACZ: RZECZY SEZONOWE (36 cm)</text>
    <line x1="{x_c2}" y1="{oy + h_paw}" x2="{ox + w_tot}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_c2+6}" y="{oy + h_paw + 6}" width="{w_c-12}" height="{32*sc}" class="backpack-area"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw + 20*sc}" class="item-text" fill="#1D4ED8" text-anchor="middle">PÓŁKA NA PLECAKI MIEJSKIE I SZKOLNE</text>
    <line x1="{x_c2}" y1="{oy + h_paw + 34*sc}" x2="{ox + w_tot}" y2="{oy + h_paw + 34*sc}" class="shelf" />
    
    <rect x="{x_c2+6}" y="{oy + h_paw + 38*sc}" width="{w_c-12}" height="{32*sc}" class="backpack-area"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw + 56*sc}" class="item-text" fill="#1D4ED8" text-anchor="middle">PÓŁKA NA PLECAKI TURYSTYCZNE I SPORTOWE</text>
    <line x1="{x_c2}" y1="{oy + h_paw + 72*sc}" x2="{ox + w_tot}" y2="{oy + h_paw + 72*sc}" class="shelf" />
    
    <rect x="{x_c2+6}" y="{oy + h_paw + 76*sc}" width="{w_c-12}" height="{18*sc}" class="drawer"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw + 88*sc}" class="item-text" text-anchor="middle">SZUFLADA 3: Czapki zimowe, kapelusze, chusty</text>
    <rect x="{x_c2+6}" y="{oy + h_paw + 96*sc}" width="{w_c-12}" height="{18*sc}" class="drawer"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw + 108*sc}" class="item-text" text-anchor="middle">SZUFLADA 4: Rękawiczki, kominy, szaliki</text>
    <rect x="{x_c2+6}" y="{oy + h_paw + 116*sc}" width="{w_c-12}" height="{18*sc}" class="drawer"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw + 128*sc}" class="item-text" text-anchor="middle">SZUFLADA 5: Okulary, etui, klucze, latarki</text>
    <rect x="{x_c2+6}" y="{oy + h_paw + 136*sc}" width="{w_c-12}" height="{18*sc}" class="drawer"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw + 148*sc}" class="item-text" text-anchor="middle">SZUFLADA 6: Drobne AGD, kable, baterie, ładowarki</text>
    
    <text x="{x_c2 + w_c/2}" y="{oy + h_tot - 20}" class="item-sub" text-anchor="middle">Dno prawe: zapasowe pudełka / organizery</text>
    
    {h_dim(ox, ox + w_tot, oy, "ŁĄCZNA SZEROKOŚĆ ŚCIANY: 150 cm", -45)}
    </svg>'''
    
    with open(f"{OUT_DIR}/szafa_2_nowy_pax_35_wariant_2.svg", "w") as f:
        f.write(svg)
    render_svg_to_png(f"{OUT_DIR}/szafa_2_nowy_pax_35_wariant_2.svg", f"{OUT_DIR}/szafa_2_nowy_pax_35_wariant_2.png", 950, 1120)

# ==============================================================================
# 6. NOWY PAX 35 CM – WARIANT 3 (GITARA W PAX 35)
# ==============================================================================
def gen_nowy_pax_35_w3():
    sc = 3.6
    ox, oy = 175, 145
    w_tot = 150 * sc
    h_tot = 236 * sc
    w_c = 75 * sc
    x_c1, x_c2 = ox, ox + w_c
    h_paw = 36 * sc
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 1120" width="950" height="1120" style="background:#FFFFFF;">
    {COMMON_STYLES}
    <text x="{ox}" y="42" class="title">NOWY PAX 35 cm – WARIANT 3 (STREFA MUZYCZNA: GITARA + DYSON)</text>
    <text x="{ox}" y="66" class="subtitle">Gitara w bezpiecznej wnęce w szafie 35 cm (z dala od metalowych narzędzi) | 6 szuflad + plecaki + ręczniki</text>
    <rect x="{ox}" y="{oy}" width="{w_tot}" height="{h_tot}" class="corp-frame" />
    <line x1="{x_c2}" y1="{oy}" x2="{x_c2}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    
    <rect x="{x_c1+6}" y="{oy+6}" width="{w_c-12}" height="{h_paw-10}" fill="#F8FAFC" rx="4"/>
    <text x="{x_c1 + w_c/2}" y="{oy + h_paw/2 + 5}" class="item-text" text-anchor="middle">PAWLACZ: RZECZY SEZONOWE (36 cm)</text>
    <line x1="{x_c1}" y1="{oy + h_paw}" x2="{x_c2}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_c1+6}" y="{oy + h_paw + 4}" width="{w_c-12}" height="{26*sc}" class="paper-towel-area"/>
    <text x="{x_c1 + w_c/2}" y="{oy + h_paw + 17*sc}" class="item-text" fill="#047857" text-anchor="middle">RĘCZNIKI PAPIEROWE (DUŻA ZGRZEWKA)</text>
    <line x1="{x_c1}" y1="{oy + h_paw + 28*sc}" x2="{x_c2}" y2="{oy + h_paw + 28*sc}" class="shelf" />
    
    <!-- Wnęka Gitara (szer. 42 cm) + Dyson (szer. 28 cm) -->
    <rect x="{x_c1+6}" y="{oy + h_paw + 32*sc}" width="{43*sc}" height="{115*sc}" class="guitar-area"/>
    <text x="{x_c1 + 22*sc}" y="{oy + h_paw + 60*sc}" class="item-text" fill="#B45309" font-size="12" text-anchor="middle">GITARA W POKROWCU</text>
    <text x="{x_c1 + 22*sc}" y="{oy + h_paw + 75*sc}" class="item-sub" fill="#92400E" text-anchor="middle">bezpieczna czysta wnęka</text>
    <text x="{x_c1 + 22*sc}" y="{oy + h_paw + 90*sc}" class="item-sub" fill="#92400E" text-anchor="middle">ochrona przed obiciem</text>
    
    <rect x="{x_c1 + 51*sc}" y="{oy + h_paw + 32*sc}" width="{21*sc}" height="{115*sc}" class="dyson-area"/>
    <text x="{x_c1 + 61.5*sc}" y="{oy + h_paw + 55*sc}" class="item-text" fill="#BE185D" text-anchor="middle">DYSON</text>
    <text x="{x_c1 + 61.5*sc}" y="{oy + h_paw + 70*sc}" class="item-sub" fill="#9D174D" text-anchor="middle">stacja ścienna</text>
    <text x="{x_c1 + 61.5*sc}" y="{oy + h_paw + 85*sc}" class="item-sub" fill="#9D174D" text-anchor="middle">+ kij mopa</text>
    
    <line x1="{x_c1}" y1="{oy + h_paw + 149*sc}" x2="{x_c2}" y2="{oy + h_paw + 149*sc}" class="shelf" />
    
    <rect x="{x_c1+6}" y="{oy + h_paw + 152*sc}" width="{w_c-12}" height="{18*sc}" class="drawer"/>
    <text x="{x_c1 + w_c/2}" y="{oy + h_paw + 164*sc}" class="item-text" text-anchor="middle">SZUFLADA 1: Akcesoria muzyczne, kable, struny, nuty</text>
    <rect x="{x_c1+6}" y="{oy + h_paw + 172*sc}" width="{w_c-12}" height="{18*sc}" class="drawer"/>
    <text x="{x_c1 + w_c/2}" y="{oy + h_paw + 184*sc}" class="item-text" text-anchor="middle">SZUFLADA 2: Ściereczki, worki do odkurzacza, filtry AGD</text>
    
    <rect x="{x_c2+6}" y="{oy+6}" width="{w_c-12}" height="{h_paw-10}" fill="#F8FAFC" rx="4"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw/2 + 5}" class="item-text" text-anchor="middle">PAWLACZ: RZECZY SEZONOWE (36 cm)</text>
    <line x1="{x_c2}" y1="{oy + h_paw}" x2="{ox + w_tot}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_c2+6}" y="{oy + h_paw + 6}" width="{w_c-12}" height="{32*sc}" class="backpack-area"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw + 20*sc}" class="item-text" fill="#1D4ED8" text-anchor="middle">PÓŁKA NA PLECAKI MIEJSKIE I SZKOLNE</text>
    <line x1="{x_c2}" y1="{oy + h_paw + 34*sc}" x2="{ox + w_tot}" y2="{oy + h_paw + 34*sc}" class="shelf" />
    
    <rect x="{x_c2+6}" y="{oy + h_paw + 38*sc}" width="{w_c-12}" height="{32*sc}" class="backpack-area"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw + 56*sc}" class="item-text" fill="#1D4ED8" text-anchor="middle">PÓŁKA NA PLECAKI TURYSTYCZNE I SPORTOWE</text>
    <line x1="{x_c2}" y1="{oy + h_paw + 72*sc}" x2="{ox + w_tot}" y2="{oy + h_paw + 72*sc}" class="shelf" />
    
    <rect x="{x_c2+6}" y="{oy + h_paw + 76*sc}" width="{w_c-12}" height="{18*sc}" class="drawer"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw + 88*sc}" class="item-text" text-anchor="middle">SZUFLADA 3: Czapki zimowe, kapelusze</text>
    <rect x="{x_c2+6}" y="{oy + h_paw + 96*sc}" width="{w_c-12}" height="{18*sc}" class="drawer"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw + 108*sc}" class="item-text" text-anchor="middle">SZUFLADA 4: Rękawiczki, kominy, szaliki</text>
    <rect x="{x_c2+6}" y="{oy + h_paw + 116*sc}" width="{w_c-12}" height="{18*sc}" class="drawer"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw + 128*sc}" class="item-text" text-anchor="middle">SZUFLADA 5: Okulary, etui, klucze, smycze</text>
    <rect x="{x_c2+6}" y="{oy + h_paw + 136*sc}" width="{w_c-12}" height="{18*sc}" class="drawer"/>
    <text x="{x_c2 + w_c/2}" y="{oy + h_paw + 148*sc}" class="item-text" text-anchor="middle">SZUFLADA 6: Drobne AGD, ładowarki, latarki</text>
    
    <text x="{x_c2 + w_c/2}" y="{oy + h_tot - 20}" class="item-sub" text-anchor="middle">Dno prawe: zapasy higieniczne / papier toaletowy</text>
    
    {h_dim(ox, ox + w_tot, oy, "ŁĄCZNA SZEROKOŚĆ ŚCIANY: 150 cm", -45)}
    </svg>'''
    
    with open(f"{OUT_DIR}/szafa_2_nowy_pax_35_wariant_3.svg", "w") as f:
        f.write(svg)
    render_svg_to_png(f"{OUT_DIR}/szafa_2_nowy_pax_35_wariant_3.svg", f"{OUT_DIR}/szafa_2_nowy_pax_35_wariant_3.png", 950, 1120)

# ==============================================================================
# 7. ISTNIEJĄCY PAX 58 CM – WARIANT 2 (MAKSYMALNA GARDEROBA)
# ==============================================================================
def gen_istniejacy_pax_58_w2():
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
    
    <text x="{ox}" y="42" class="title">ISTNIEJĄCY PAX 58 cm (270 cm) – WARIANT 2 (MAKSYMALNA GARDEROBA)</text>
    <text x="{ox}" y="66" class="subtitle">Drążek nad suszarką ZOSTAJE | Wnęka 31 cm: Odkurzacz Amica pionowo | W module 100 cm ZOSTAJĄ 3 SZUFLADY! | W 50 cm: Gitara + Drabina</text>
    
    <rect x="{ox}" y="85" width="710" height="28" fill="#F0FDF4" stroke="#16A34A" rx="4"/>
    <text x="{ox + 355}" y="103" fill="#15803D" font-size="11.5" font-weight="700" text-anchor="middle">ZACHOWANE 100% SZUFLAD NA UBRANIA W PAX 58! DYSON I MOP PRZENIESIONE DO NOWEGO PAX 35</text>
    
    <rect x="{ox}" y="{oy}" width="{w_tot}" height="{h_tot}" class="corp-frame" />
    <line x1="{x_m2}" y1="{oy}" x2="{x_m2}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    <line x1="{x_m3}" y1="{oy}" x2="{x_m3}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    <line x1="{x_m4}" y1="{oy}" x2="{x_m4}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    
    <!-- MODUŁ 1: 100 CM -->
    <rect x="{x_m1+4}" y="{oy+4}" width="{w_m1-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m1 + w_m1/2}" y="{oy + h_paw/2}" class="item-text" text-anchor="middle">PAWLACZ: CZARNA WALIZKA PODRÓŻNA (36 cm)</text>
    <line x1="{x_m1}" y1="{oy + h_paw}" x2="{x_m2}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_m1+6}" y="{oy + h_paw + 6}" width="{w_m1-12}" height="{95*sc - 12}" class="hanging-area" />
    <line x1="{x_m1+16}" y1="{oy + h_paw + 28}" x2="{x_m2-16}" y2="{oy + h_paw + 28}" class="rod" />
    <text x="{x_m1 + w_m1/2}" y="{oy + h_paw + 52}" class="item-text" fill="#7E22CE" font-size="12" text-anchor="middle">DRĄŻEK 100 cm NAD SUSZARKĄ (ZOSTAJE!)</text>
    <text x="{x_m1 + w_m1/2}" y="{oy + h_paw + 72}" class="item-text" text-anchor="middle">Koszule dosychające po suszeniu / kurtki codzienne</text>
    <text x="{x_m1 + w_m1/2}" y="{oy + h_paw + 88}" class="item-sub" text-anchor="middle">Wysokość wiszenia: 95 cm – swobodny zwis nad płytą suszarki</text>
    <line x1="{x_m1}" y1="{oy + h_paw + 95*sc}" x2="{x_m2}" y2="{oy + h_paw + 95*sc}" class="shelf" />
    
    <!-- Dół modułu 1: Suszarka Beko + Wnęka 31 cm (Odkurzacz pionowo + miska) -->
    <rect x="{x_m1+8}" y="{oy + h_paw + 95*sc + 10}" width="{60*sc}" height="{85*sc}" class="dryer-bg" />
    <circle cx="{x_m1 + 8 + 30*sc}" cy="{oy + h_paw + 95*sc + 10 + 42.5*sc}" r="65" fill="#BAE6FD" stroke="#0284C7" stroke-width="2.5" />
    <circle cx="{x_m1 + 8 + 30*sc}" cy="{oy + h_paw + 95*sc + 10 + 42.5*sc}" r="50" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="4,2" />
    <rect x="{x_m1 + 16}" y="{oy + h_paw + 95*sc + 18}" width="{60*sc - 16}" height="28" fill="#0284C7" rx="3" />
    <circle cx="{x_m1 + 8 + 30*sc}" cy="{oy + h_paw + 95*sc + 32}" r="8" fill="#FFFFFF" />
    <text x="{x_m1 + 8 + 30*sc}" y="{oy + h_paw + 95*sc + 10 + 42.5*sc + 5}" class="item-text" fill="#0369A1" font-size="12" text-anchor="middle">SUSZARKA BEKO</text>
    <text x="{x_m1 + 8 + 30*sc}" y="{oy + h_paw + 95*sc + 10 + 42.5*sc + 20}" class="item-sub" fill="#0284C7" text-anchor="middle">szer. 60 cm | wys. 85 cm</text>
    
    <rect x="{x_m1 + 16 + 60*sc}" y="{oy + h_paw + 95*sc + 10}" width="{31*sc}" height="{85*sc}" class="vacuum-area" />
    <rect x="{x_m1 + 20 + 60*sc}" y="{oy + h_tot - 55*sc}" width="{31*sc - 8}" height="{50*sc}" fill="#EDE9FE" stroke="#7C3AED" stroke-width="1.5" rx="4"/>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc}" y="{oy + h_tot - 32*sc}" class="item-text" fill="#6D28D9" font-size="11" text-anchor="middle">ODKURZACZ AMICA</text>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc}" y="{oy + h_tot - 18*sc}" class="item-sub" fill="#7C3AED" text-anchor="middle">postawiony pionowo</text>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc}" y="{oy + h_tot - 6*sc}" class="item-sub" fill="#7C3AED" text-anchor="middle">(szer. 28 cm pasuje idealnie!)</text>
    
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc}" y="{oy + h_paw + 95*sc + 28}" class="item-text" fill="#15803D" text-anchor="middle">MISKA PIONOWO</text>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc}" y="{oy + h_paw + 95*sc + 44}" class="item-sub" fill="#166534" text-anchor="middle">+ proszki / kapsułki</text>
    
    <!-- MODUŁ 2: 100 CM (KOMPLET 3 SZUFLAD NA UBRANIA!) -->
    <rect x="{x_m2+4}" y="{oy+4}" width="{w_m2-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw/2}" class="item-text" text-anchor="middle">PAWLACZ: CZERWONA DUŻA WALIZKA (36 cm)</text>
    <line x1="{x_m2}" y1="{oy + h_paw}" x2="{x_m3}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_m2+6}" y="{oy + h_paw + 6}" width="{w_m2-12}" height="{105*sc - 12}" class="hanging-area" />
    <line x1="{x_m2+16}" y1="{oy + h_paw + 28}" x2="{x_m3-16}" y2="{oy + h_paw + 28}" class="rod" />
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 52}" class="item-text" fill="#7E22CE" font-size="12" text-anchor="middle">DRĄŻEK 100 cm: GŁÓWNA GARDEROBA (ZOSTAJE!)</text>
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 72}" class="item-text" text-anchor="middle">Garnitury w pokrowcach, koszule, marynarki</text>
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 88}" class="item-sub" text-anchor="middle">Wysokość wiszenia 105 cm (głębokość 58 cm)</text>
    <line x1="{x_m2}" y1="{oy + h_paw + 105*sc}" x2="{x_m3}" y2="{oy + h_paw + 105*sc}" class="shelf" />
    
    <!-- 3 SZUFLADY KOMPLEMENT 100 CM -->
    <rect x="{x_m2+6}" y="{oy + h_paw + 105*sc + 3}" width="{w_m2-12}" height="{18*sc - 6}" class="drawer" />
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 105*sc + 9*sc + 4}" class="item-text" text-anchor="middle">SZUFLADA 1 (KOMPLEMENT 100 cm): Bielizna osobista i skarpetki</text>
    <line x1="{x_m2}" y1="{oy + h_paw + 123*sc}" x2="{x_m3}" y2="{oy + h_paw + 123*sc}" class="shelf" />
    
    <rect x="{x_m2+6}" y="{oy + h_paw + 123*sc + 3}" width="{w_m2-12}" height="{18*sc - 6}" class="drawer" />
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 123*sc + 9*sc + 4}" class="item-text" text-anchor="middle">SZUFLADA 2 (KOMPLEMENT 100 cm): T-shirty, koszulki polo, odzież codzienna</text>
    <line x1="{x_m2}" y1="{oy + h_paw + 141*sc}" x2="{x_m3}" y2="{oy + h_paw + 141*sc}" class="shelf" />
    
    <rect x="{x_m2+6}" y="{oy + h_paw + 141*sc + 3}" width="{w_m2-12}" height="{18*sc - 6}" class="drawer" />
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 141*sc + 9*sc + 4}" class="item-text" text-anchor="middle">SZUFLADA 3 (KOMPLEMENT 100 cm): Spodnie, swetry, bluzy, tekstylia</text>
    <line x1="{x_m2}" y1="{oy + h_paw + 159*sc}" x2="{x_m3}" y2="{oy + h_paw + 159*sc}" class="shelf" />
    
    <!-- Półka / dno pod szufladami -->
    <rect x="{x_m2+6}" y="{oy + h_paw + 159*sc + 4}" width="{w_m2-12}" height="{(h_tot - (h_paw + 159*sc)) - 8}" fill="#F8FAFC" rx="4" />
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 159*sc + 25}" class="item-text" fill="#475569" text-anchor="middle">PÓŁKA DOLNA / DNO SZAFY 100 cm</text>
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 159*sc + 42}" class="item-sub" text-anchor="middle">Płaskie pojemniki SKUBB: zapasowe kołdry, poduszki, pościel dla gości</text>
    
    <!-- MODUŁ 3: 50 CM (Gitara + Drabina bez Dysona – pełna swoboda!) -->
    <rect x="{x_m3+4}" y="{oy+4}" width="{w_m3-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m3 + w_m3/2}" y="{oy + h_paw/2 + 5}" class="item-text" text-anchor="middle">PAWLACZ</text>
    <line x1="{x_m3}" y1="{oy + h_paw}" x2="{x_m4}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_m3+6}" y="{oy + h_paw + 6}" width="{w_m3-12}" height="{135*sc - 12}" class="corp-inner" />
    
    <!-- Gitara -->
    <rect x="{x_m3+8}" y="{oy + h_paw + 8}" width="{28*sc}" height="{135*sc - 16}" class="guitar-area" />
    <text x="{x_m3 + 8 + 14*sc}" y="{oy + h_paw + 30}" class="item-text" fill="#B45309" text-anchor="middle">GITARA</text>
    <text x="{x_m3 + 8 + 14*sc}" y="{oy + h_paw + 46}" class="item-sub" fill="#92400E" text-anchor="middle">w pokrowcu</text>
    <text x="{x_m3 + 8 + 14*sc}" y="{oy + h_paw + 62}" class="item-sub" fill="#92400E" text-anchor="middle">szeroka wnęka</text>
    <text x="{x_m3 + 8 + 14*sc}" y="{oy + h_paw + 78}" class="item-sub" fill="#92400E" text-anchor="middle">brak ścisku!</text>
    
    <!-- Drabina -->
    <rect x="{x_m3 + 12 + 28*sc}" y="{oy + h_paw + 8}" width="{w_m3 - 28*sc - 20}" height="{135*sc - 16}" class="ladder-area" />
    <text x="{x_m3 + 12 + 28*sc + (w_m3 - 28*sc - 20)/2}" y="{oy + h_paw + 67.5*sc}" class="item-text" text-anchor="middle" transform="rotate(-90 {x_m3 + 12 + 28*sc + (w_m3 - 28*sc - 20)/2} {oy + h_paw + 67.5*sc})">DRABINA ALUMINIOWA</text>
    
    <line x1="{x_m3}" y1="{oy + h_paw + 135*sc}" x2="{x_m4}" y2="{oy + h_paw + 135*sc}" class="shelf" />
    
    <!-- Półki narzędziowe Parkside -->
    <rect x="{x_m3+6}" y="{oy + h_paw + 135*sc + 4}" width="{w_m3-12}" height="{20*sc}" fill="#F1F5F9" rx="3"/>
    <text x="{x_m3 + w_m3/2}" y="{oy + h_paw + 135*sc + 16}" class="item-text" text-anchor="middle">WALIZKA PARKSIDE 1</text>
    <line x1="{x_m3}" y1="{oy + h_paw + 157*sc}" x2="{x_m4}" y2="{oy + h_paw + 157*sc}" class="shelf" />
    
    <rect x="{x_m3+6}" y="{oy + h_paw + 157*sc + 4}" width="{w_m3-12}" height="{20*sc}" fill="#F1F5F9" rx="3"/>
    <text x="{x_m3 + w_m3/2}" y="{oy + h_paw + 157*sc + 16}" class="item-text" text-anchor="middle">SKRZYNKA PARKSIDE 2</text>
    <line x1="{x_m3}" y1="{oy + h_paw + 179*sc}" x2="{x_m4}" y2="{oy + h_paw + 179*sc}" class="shelf" />
    
    <rect x="{x_m3+6}" y="{oy + h_paw + 179*sc + 4}" width="{w_m3-12}" height="{20*sc}" class="basket"/>
    <text x="{x_m3 + w_m3/2}" y="{oy + h_paw + 179*sc + 16}" class="item-sub" font-weight="700" text-anchor="middle">Kosz druciany KOMPLEMENT</text>
    
    <!-- MODUŁ 4: 20 CM -->
    <rect x="{x_m4+4}" y="{oy+4}" width="{w_m4-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_paw/2 - 4}" class="item-text" font-size="10" text-anchor="middle">ŻELAZ-</text>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_paw/2 + 10}" class="item-text" font-size="10" text-anchor="middle">KO</text>
    <line x1="{x_m4}" y1="{oy + h_paw}" x2="{ox + w_tot}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_m4+4}" y="{oy + h_paw + 6}" width="{w_m4-8}" height="{h_tot - h_paw - 12}" fill="#F8FAFC" stroke="#94A3B8" stroke-dasharray="2,2" rx="3"/>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_tot/2}" class="item-text" font-size="10" text-anchor="middle" transform="rotate(-90 {x_m4 + w_m4/2} {oy + h_tot/2})">DESKA DO PRASOWANIA</text>
    
    {h_dim(ox, ox + w_tot, oy, "ŁĄCZNA SZEROKOŚĆ ZABUDOWY PAX 58: 270 cm", -45)}
    </svg>'''
    
    with open(f"{OUT_DIR}/szafa_3_istniejacy_pax_58_wariant_2.svg", "w") as f:
        f.write(svg)
    render_svg_to_png(f"{OUT_DIR}/szafa_3_istniejacy_pax_58_wariant_2.svg", f"{OUT_DIR}/szafa_3_istniejacy_pax_58_wariant_2.png", 1260, 1080)

# ==============================================================================
# 8. PANORAMA CAŁEGO UKŁADU W JEDNEJ SKALI (WARIANT 2)
# ==============================================================================
def gen_panorama_w2():
    sc = 2.4
    ox, oy = 90, 140
    w_pax58 = 270 * sc
    gap1 = 65
    w_pax35 = 150 * sc
    gap2 = 65
    w_wymiar = 125 * sc
    
    x_pax58 = ox
    x_pax35 = x_pax58 + w_pax58 + gap1
    x_wymiar = x_pax35 + w_pax35 + gap2
    
    h_pax = 236 * sc
    h_wymiar = 240 * sc
    
    svg_w = int(x_wymiar + w_wymiar + 90)
    svg_h = int(oy + h_wymiar + 120)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}" style="background:#FFFFFF;">
    {COMMON_STYLES}
    
    <text x="{ox}" y="42" class="title">PANORAMA UKŁADU SZAF W CAŁYM MIESZKANIU – WERSJA 2 (WARIANT 2)</text>
    <text x="{ox}" y="66" class="subtitle">Wspólna skala (1 cm = 2.4 px) | W PAX 58 zostają 3 szuflady na ubrania! | Dyson + wiadro mopa w PAX 35 | Szafa na wymiar = 100% butów</text>
    
    <!-- 1. PAX 58 CM (WARIANT 2) -->
    <rect x="{x_pax58}" y="{oy}" width="{w_pax58}" height="{h_pax}" class="corp-frame" />
    <rect x="{x_pax58}" y="{oy-28}" width="{w_pax58}" height="24" fill="#0F172A" rx="4"/>
    <text x="{x_pax58 + w_pax58/2}" y="{oy-12}" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">1. ISTNIEJĄCY PAX 58 cm – MAKSYMALNA GARDEROBA (3 SZUFLADY UBRAŃ ZOSTAJĄ!)</text>
    
    <line x1="{x_pax58 + 100*sc}" y1="{oy}" x2="{x_pax58 + 100*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_pax58}" y1="{oy + 36*sc}" x2="{x_pax58 + 100*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 50*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Walizka czarna</text>
    
    <!-- Drążek nad suszarką -->
    <rect x="{x_pax58 + 6}" y="{oy + 40*sc}" width="{92*sc}" height="{90*sc}" class="hanging-area"/>
    <line x1="{x_pax58 + 14*sc}" y1="{oy + 55*sc}" x2="{x_pax58 + 90*sc}" y2="{oy + 55*sc}" class="rod"/>
    <text x="{x_pax58 + 50*sc}" y="{oy + 75*sc}" class="item-text" fill="#7E22CE" font-size="10" text-anchor="middle">DRĄŻEK NAD SUSZARKĄ</text>
    <text x="{x_pax58 + 50*sc}" y="{oy + 90*sc}" class="item-sub" font-size="8.5" text-anchor="middle">dosychanie / kurtki codzienne</text>
    <line x1="{x_pax58}" y1="{oy + 132*sc}" x2="{x_pax58 + 100*sc}" y2="{oy + 132*sc}" class="shelf"/>
    
    <!-- Suszarka Beko -->
    <rect x="{x_pax58 + 6}" y="{oy + 136*sc}" width="{60*sc}" height="{h_pax - 140*sc}" class="dryer-bg"/>
    <circle cx="{x_pax58 + 6 + 30*sc}" cy="{oy + 136*sc + (h_pax - 140*sc)/2}" r="45" fill="#BAE6FD" stroke="#0284C7" stroke-width="2"/>
    <text x="{x_pax58 + 6 + 30*sc}" y="{oy + 136*sc + (h_pax - 140*sc)/2 - 5}" class="item-text" fill="#0369A1" text-anchor="middle">SUSZARKA</text>
    <text x="{x_pax58 + 6 + 30*sc}" y="{oy + 136*sc + (h_pax - 140*sc)/2 + 10}" class="item-sub" fill="#0284C7" text-anchor="middle">BEKO 60cm</text>
    
    <!-- Wnęka 31 cm: Odkurzacz Amica pionowo -->
    <rect x="{x_pax58 + 6 + 60*sc + 4}" y="{oy + 136*sc}" width="{31*sc - 6}" height="{h_pax - 140*sc}" class="vacuum-area"/>
    <text x="{x_pax58 + 6 + 60*sc + 15*sc}" y="{oy + 136*sc + 25}" class="item-sub" fill="#6D28D9" font-weight="700" text-anchor="middle">MISKA PION</text>
    <text x="{x_pax58 + 6 + 60*sc + 15*sc}" y="{oy + h_pax - 30}" class="item-sub" fill="#6D28D9" font-weight="700" text-anchor="middle">ODKURZACZ</text>
    <text x="{x_pax58 + 6 + 60*sc + 15*sc}" y="{oy + h_pax - 18}" class="item-sub" fill="#6D28D9" font-size="8" text-anchor="middle">AMICA PION</text>
    
    <!-- Moduł 2: 100 cm (3 szuflady) -->
    <line x1="{x_pax58 + 200*sc}" y1="{oy}" x2="{x_pax58 + 200*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_pax58 + 100*sc}" y1="{oy + 36*sc}" x2="{x_pax58 + 200*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Walizka czerwona</text>
    
    <rect x="{x_pax58 + 104*sc}" y="{oy + 40*sc}" width="{92*sc}" height="{98*sc}" class="hanging-area"/>
    <line x1="{x_pax58 + 110*sc}" y1="{oy + 55*sc}" x2="{x_pax58 + 190*sc}" y2="{oy + 55*sc}" class="rod"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 90*sc}" class="item-text" fill="#7E22CE" text-anchor="middle">DRĄŻEK 100 cm (Garnitury / Koszule)</text>
    <line x1="{x_pax58 + 100*sc}" y1="{oy + 140*sc}" x2="{x_pax58 + 200*sc}" y2="{oy + 140*sc}" class="shelf"/>
    
    <rect x="{x_pax58 + 104*sc}" y="{oy + 143*sc}" width="{92*sc}" height="{16*sc}" class="drawer"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 154*sc}" class="item-sub" text-anchor="middle">Szuflada 1: Bielizna / skarpetki</text>
    <line x1="{x_pax58 + 100*sc}" y1="{oy + 160*sc}" x2="{x_pax58 + 200*sc}" y2="{oy + 160*sc}" class="shelf"/>
    
    <rect x="{x_pax58 + 104*sc}" y="{oy + 163*sc}" width="{92*sc}" height="{16*sc}" class="drawer"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 174*sc}" class="item-sub" text-anchor="middle">Szuflada 2: T-shirty / polo</text>
    <line x1="{x_pax58 + 100*sc}" y1="{oy + 180*sc}" x2="{x_pax58 + 200*sc}" y2="{oy + 180*sc}" class="shelf"/>
    
    <rect x="{x_pax58 + 104*sc}" y="{oy + 183*sc}" width="{92*sc}" height="{16*sc}" class="drawer"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 194*sc}" class="item-sub" text-anchor="middle">Szuflada 3: Spodnie / swetry</text>
    <line x1="{x_pax58 + 100*sc}" y1="{oy + 200*sc}" x2="{x_pax58 + 200*sc}" y2="{oy + 200*sc}" class="shelf"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 218*sc}" class="item-sub" text-anchor="middle">Dno: Pudełka SKUBB (pościel gościnna)</text>
    
    <!-- Moduł 3: 50 cm (Gitara + Drabina) -->
    <line x1="{x_pax58 + 250*sc}" y1="{oy}" x2="{x_pax58 + 250*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_pax58 + 200*sc}" y1="{oy + 36*sc}" x2="{x_pax58 + 250*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Pawlacz</text>
    
    <rect x="{x_pax58 + 203*sc}" y="{oy + 39*sc}" width="{28*sc}" height="{130*sc}" class="guitar-area"/>
    <text x="{x_pax58 + 217*sc}" y="{oy + 95*sc}" class="item-text" font-size="9" fill="#B45309" text-anchor="middle" transform="rotate(-90 {x_pax58 + 217*sc} {oy + 95*sc})">GITARA POKROWIEC</text>
    
    <rect x="{x_pax58 + 233*sc}" y="{oy + 39*sc}" width="{14*sc}" height="{130*sc}" class="ladder-area"/>
    <text x="{x_pax58 + 240*sc}" y="{oy + 95*sc}" class="item-sub" font-size="8" text-anchor="middle" transform="rotate(-90 {x_pax58 + 240*sc} {oy + 95*sc})">DRABINA</text>
    
    <line x1="{x_pax58 + 200*sc}" y1="{oy + 172*sc}" x2="{x_pax58 + 250*sc}" y2="{oy + 172*sc}" class="shelf"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 188*sc}" class="item-sub" font-size="8.5" text-anchor="middle">Parkside 1</text>
    <line x1="{x_pax58 + 200*sc}" y1="{oy + 195*sc}" x2="{x_pax58 + 250*sc}" y2="{oy + 195*sc}" class="shelf"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 210*sc}" class="item-sub" font-size="8.5" text-anchor="middle">Parkside 2</text>
    <line x1="{x_pax58 + 200*sc}" y1="{oy + 217*sc}" x2="{x_pax58 + 250*sc}" y2="{oy + 217*sc}" class="shelf"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 230*sc}" class="item-sub" font-size="8.5" text-anchor="middle">Kosz druciany</text>
    
    <!-- Moduł 4: 20 cm -->
    <text x="{x_pax58 + 260*sc}" y="{oy + 22*sc}" class="item-sub" font-size="8" text-anchor="middle">Żelazko</text>
    <line x1="{x_pax58 + 250*sc}" y1="{oy + 36*sc}" x2="{x_pax58 + 270*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 260*sc}" y="{oy + h_pax/2}" class="item-sub" font-size="9" font-weight="700" text-anchor="middle" transform="rotate(-90 {x_pax58 + 260*sc} {oy + h_pax/2})">DESKA DO PRASOWANIA</text>
    
    <!-- 2. NOWY PAX 35 CM (WARIANT 2: DYSON + MOP + SZUFLADY) -->
    <rect x="{x_pax35}" y="{oy}" width="{w_pax35}" height="{h_pax}" class="corp-frame" />
    <rect x="{x_pax35}" y="{oy-28}" width="{w_pax35}" height="24" fill="#059669" rx="4"/>
    <text x="{x_pax35 + w_pax35/2}" y="{oy-12}" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">2. NOWY PAX 35 cm – PION DYSON + MOP | 6 SZUFLAD | PLECAKI</text>
    
    <line x1="{x_pax35 + 75*sc}" y1="{oy}" x2="{x_pax35 + 75*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_pax35}" y1="{oy + 36*sc}" x2="{x_pax35 + 75*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Pudła SKUBB</text>
    
    <rect x="{x_pax35 + 4}" y="{oy + 38*sc}" width="{34*sc}" height="{115*sc}" class="dyson-area"/>
    <text x="{x_pax35 + 21*sc}" y="{oy + 65*sc}" class="item-sub" font-size="8.5" fill="#BE185D" font-weight="700" text-anchor="middle">DYSON</text>
    <text x="{x_pax35 + 21*sc}" y="{oy + 80*sc}" class="item-sub" font-size="8" fill="#15803D" font-weight="700" text-anchor="middle">KIJ MOPA</text>
    <text x="{x_pax35 + 21*sc}" y="{oy + 140*sc}" class="item-sub" font-size="8" fill="#15803D" font-weight="700" text-anchor="middle">WIADRO</text>
    
    <rect x="{x_pax35 + 40*sc}" y="{oy + 38*sc}" width="{32*sc}" height="{35*sc}" class="paper-towel-area"/>
    <text x="{x_pax35 + 56*sc}" y="{oy + 55*sc}" class="item-sub" font-size="8" fill="#047857" font-weight="700" text-anchor="middle">Ręczniki pap.</text>
    
    <rect x="{x_pax35 + 40*sc}" y="{oy + 76*sc}" width="{32*sc}" height="{35*sc}" fill="#F8FAFC" rx="3"/>
    <text x="{x_pax35 + 56*sc}" y="{oy + 95*sc}" class="item-sub" font-size="8" text-anchor="middle">Papier toal.</text>
    
    <rect x="{x_pax35 + 40*sc}" y="{oy + 114*sc}" width="{32*sc}" height="{39*sc}" fill="#F8FAFC" rx="3"/>
    <text x="{x_pax35 + 56*sc}" y="{oy + 135*sc}" class="item-sub" font-size="8" text-anchor="middle">Chemia</text>
    
    <line x1="{x_pax35}" y1="{oy + 156*sc}" x2="{x_pax35 + 75*sc}" y2="{oy + 156*sc}" class="shelf"/>
    <rect x="{x_pax35 + 4}" y="{oy + 159*sc}" width="{70*sc}" height="{18*sc}" class="drawer"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 171*sc}" class="item-sub" text-anchor="middle">Szuflada 1: Ściereczki / zapas mopa</text>
    <rect x="{x_pax35 + 4}" y="{oy + 179*sc}" width="{70*sc}" height="{18*sc}" class="drawer"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 191*sc}" class="item-sub" text-anchor="middle">Szuflada 2: Akcesoria AGD</text>
    
    <!-- Prawy 75 cm (PAX 35 W2) -->
    <line x1="{x_pax35 + 75*sc}" y1="{oy + 36*sc}" x2="{x_pax35 + 150*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Pudła SKUBB</text>
    
    <rect x="{x_pax35 + 78*sc}" y="{oy + 40*sc}" width="{70*sc}" height="{32*sc}" class="backpack-area"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 58*sc}" class="item-sub" font-size="8.5" fill="#1D4ED8" font-weight="700" text-anchor="middle">PLECAKI MIEJSKIE</text>
    <line x1="{x_pax35 + 75*sc}" y1="{oy + 74*sc}" x2="{x_pax35 + 150*sc}" y2="{oy + 74*sc}" class="shelf"/>
    
    <rect x="{x_pax35 + 78*sc}" y="{oy + 76*sc}" width="{70*sc}" height="{32*sc}" class="backpack-area"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 94*sc}" class="item-sub" font-size="8.5" fill="#1D4ED8" font-weight="700" text-anchor="middle">PLECAKI TURYSTYCZNE</text>
    <line x1="{x_pax35 + 75*sc}" y1="{oy + 110*sc}" x2="{x_pax35 + 150*sc}" y2="{oy + 110*sc}" class="shelf"/>
    
    <rect x="{x_pax35 + 78*sc}" y="{oy + 113*sc}" width="{70*sc}" height="{17*sc}" class="drawer"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 125*sc}" class="item-sub" text-anchor="middle">Szuflada 3: Czapki zimowe</text>
    <rect x="{x_pax35 + 78*sc}" y="{oy + 132*sc}" width="{70*sc}" height="{17*sc}" class="drawer"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 144*sc}" class="item-sub" text-anchor="middle">Szuflada 4: Rękawiczki / szale</text>
    <rect x="{x_pax35 + 78*sc}" y="{oy + 151*sc}" width="{70*sc}" height="{17*sc}" class="drawer"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 163*sc}" class="item-sub" text-anchor="middle">Szuflada 5: Okulary / klucze</text>
    <rect x="{x_pax35 + 78*sc}" y="{oy + 170*sc}" width="{70*sc}" height="{17*sc}" class="drawer"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 182*sc}" class="item-sub" text-anchor="middle">Szuflada 6: Drobne AGD / ładowarki</text>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 215*sc}" class="item-sub" font-size="8.5" text-anchor="middle">Dno: Koszyki / organizery</text>
    
    <!-- 3. SZAFA NA WYMIAR (PO PRAWEJ) -->
    <rect x="{x_wymiar}" y="{oy}" width="{w_wymiar}" height="{h_wymiar}" class="corp-frame" />
    <rect x="{x_wymiar}" y="{oy-28}" width="{w_wymiar}" height="24" fill="#7E22CE" rx="4"/>
    <text x="{x_wymiar + w_wymiar/2}" y="{oy-12}" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">3. SZAFA NA WYMIAR (125 cm) – JEDYNA BAZA BUTÓW</text>
    
    <line x1="{x_wymiar + 12*sc}" y1="{oy}" x2="{x_wymiar + 12*sc}" y2="{oy + h_wymiar}" stroke="#94A3B8" stroke-dasharray="2,2"/>
    <line x1="{x_wymiar + 64*sc}" y1="{oy}" x2="{x_wymiar + 64*sc}" y2="{oy + h_wymiar}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_wymiar + 115*sc}" y1="{oy}" x2="{x_wymiar + 115*sc}" y2="{oy + h_wymiar}" stroke="#94A3B8" stroke-dasharray="2,2"/>
    
    <line x1="{x_wymiar}" y1="{oy + 45*sc}" x2="{x_wymiar + w_wymiar}" y2="{oy + 45*sc}" class="shelf"/>
    <text x="{x_wymiar + 38*sc}" y="{oy + 26*sc}" class="item-sub" text-anchor="middle">Pawlacz 50cm</text>
    <text x="{x_wymiar + 89*sc}" y="{oy + 26*sc}" class="item-sub" text-anchor="middle">Nadstawka 51cm</text>
    
    <rect x="{x_wymiar + 14*sc}" y="{oy + 48*sc}" width="{48*sc}" height="{156*sc}" class="hanging-area"/>
    <line x1="{x_wymiar + 18*sc}" y1="{oy + 65*sc}" x2="{x_wymiar + 60*sc}" y2="{oy + 65*sc}" class="rod"/>
    <text x="{x_wymiar + 38*sc}" y="{oy + 105*sc}" class="item-text" font-size="10" fill="#7E22CE" text-anchor="middle">DRĄŻEK 160 cm</text>
    <text x="{x_wymiar + 38*sc}" y="{oy + 120*sc}" class="item-text" font-size="9" text-anchor="middle">DŁUGIE PŁASZCZE</text>
    <line x1="{x_wymiar + 12*sc}" y1="{oy + 205*sc}" x2="{x_wymiar + 64*sc}" y2="{oy + 205*sc}" class="shelf"/>
    <rect x="{x_wymiar + 14*sc}" y="{oy + 208*sc}" width="{48*sc}" height="{30*sc}" class="drawer"/>
    <text x="{x_wymiar + 38*sc}" y="{oy + 224*sc}" class="item-sub" text-anchor="middle">Szuflada 35cm</text>
    
    '''
    sh_step_w = (h_wymiar - 45*sc) / 8.0
    for i in range(8):
        y_w = oy + 45*sc + i * sh_step_w
        if i < 7:
            svg += f'<line x1="{x_wymiar + 64*sc}" y1="{y_w + sh_step_w}" x2="{x_wymiar + 115*sc}" y2="{y_w + sh_step_w}" class="shelf"/>'
        label = "Czapki / szale" if i < 3 else f"BUTY BIEŻĄCE {i-2}"
        color = "#64748B" if i < 3 else "#1E40AF"
        svg += f'<text x="{x_wymiar + 89*sc}" y="{y_w + sh_step_w/2 + 3}" class="item-sub" font-size="8.5" fill="{color}" font-weight="{"700" if i>=3 else "500"}" text-anchor="middle">{label}</text>'
        
    svg += f'''
    <g transform="translate(0, {oy + h_wymiar + 35})">
        {h_dim(x_pax58, x_pax58 + w_pax58, 0, "SZEROKOŚĆ PAX 58: 270 cm", 0)}
        {h_dim(x_pax35, x_pax35 + w_pax35, 0, "NOWY PAX 35: 150 cm", 0)}
        {h_dim(x_wymiar, x_wymiar + w_wymiar, 0, "NA WYMIAR: 125 cm", 0)}
    </g>
    </svg>'''
    
    with open(f"{OUT_DIR}/02_panorama_wersja_2_wariant_2.svg", "w") as f:
        f.write(svg)
    render_svg_to_png(f"{OUT_DIR}/02_panorama_wersja_2_wariant_2.svg", f"{OUT_DIR}/02_panorama_wersja_2_wariant_2.png", svg_w, svg_h)

# ==============================================================================
# 9. ISTNIEJĄCY PAX 58 CM – WARIANT 3 (WARSZTAT TECHNICZNY)
# ==============================================================================
def gen_istniejacy_pax_58_w3():
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
    
    <text x="{ox}" y="42" class="title">ISTNIEJĄCY PAX 58 cm (270 cm) – WARIANT 3 (WARSZTAT TECHNICZNY)</text>
    <text x="{ox}" y="66" class="subtitle">Gitara bezpieczna w PAX 35! | Moduł 50 cm to pełny schowek techniczny: Drabina + Odkurzacz Amica + Narzędzia Parkside</text>
    
    <rect x="{ox}" y="85" width="700" height="28" fill="#FEF3C7" stroke="#F59E0B" rx="4"/>
    <text x="{ox + 350}" y="103" fill="#B45309" font-size="11.5" font-weight="700" text-anchor="middle">PEŁNE BEZPIECZEŃSTWO GITARY (W PAX 35) + BEZKOMPROMISOWY WARSZTAT GOSPODARCZY W PAX 58</text>
    
    <rect x="{ox}" y="{oy}" width="{w_tot}" height="{h_tot}" class="corp-frame" />
    <line x1="{x_m2}" y1="{oy}" x2="{x_m2}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    <line x1="{x_m3}" y1="{oy}" x2="{x_m3}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    <line x1="{x_m4}" y1="{oy}" x2="{x_m4}" y2="{oy + h_tot}" stroke="#0F172A" stroke-width="3" />
    
    <!-- MODUŁ 1: 100 CM -->
    <rect x="{x_m1+4}" y="{oy+4}" width="{w_m1-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m1 + w_m1/2}" y="{oy + h_paw/2}" class="item-text" text-anchor="middle">PAWLACZ: CZARNA WALIZKA PODRÓŻNA (36 cm)</text>
    <line x1="{x_m1}" y1="{oy + h_paw}" x2="{x_m2}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_m1+6}" y="{oy + h_paw + 6}" width="{w_m1-12}" height="{95*sc - 12}" class="hanging-area" />
    <line x1="{x_m1+16}" y1="{oy + h_paw + 28}" x2="{x_m2-16}" y2="{oy + h_paw + 28}" class="rod" />
    <text x="{x_m1 + w_m1/2}" y="{oy + h_paw + 52}" class="item-text" fill="#7E22CE" font-size="12" text-anchor="middle">DRĄŻEK 100 cm NAD SUSZARKĄ (ZOSTAJE!)</text>
    <text x="{x_m1 + w_m1/2}" y="{oy + h_paw + 72}" class="item-text" text-anchor="middle">Koszule dosychające po suszeniu / kurtki codzienne</text>
    <line x1="{x_m1}" y1="{oy + h_paw + 95*sc}" x2="{x_m2}" y2="{oy + h_paw + 95*sc}" class="shelf" />
    
    <!-- Dół modułu 1: Suszarka Beko + Wnęka 31 cm (Wiadro + Kij mopa + Miski) -->
    <rect x="{x_m1+8}" y="{oy + h_paw + 95*sc + 10}" width="{60*sc}" height="{85*sc}" class="dryer-bg" />
    <circle cx="{x_m1 + 8 + 30*sc}" cy="{oy + h_paw + 95*sc + 10 + 42.5*sc}" r="65" fill="#BAE6FD" stroke="#0284C7" stroke-width="2.5" />
    <circle cx="{x_m1 + 8 + 30*sc}" cy="{oy + h_paw + 95*sc + 10 + 42.5*sc}" r="50" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="4,2" />
    <rect x="{x_m1 + 16}" y="{oy + h_paw + 95*sc + 18}" width="{60*sc - 16}" height="28" fill="#0284C7" rx="3" />
    <circle cx="{x_m1 + 8 + 30*sc}" cy="{oy + h_paw + 95*sc + 32}" r="8" fill="#FFFFFF" />
    <text x="{x_m1 + 8 + 30*sc}" y="{oy + h_paw + 95*sc + 10 + 42.5*sc + 5}" class="item-text" fill="#0369A1" font-size="12" text-anchor="middle">SUSZARKA BEKO</text>
    <text x="{x_m1 + 8 + 30*sc}" y="{oy + h_paw + 95*sc + 10 + 42.5*sc + 20}" class="item-sub" fill="#0284C7" text-anchor="middle">szer. 60 cm | wys. 85 cm</text>
    
    <rect x="{x_m1 + 16 + 60*sc}" y="{oy + h_paw + 95*sc + 10}" width="{31*sc}" height="{85*sc}" class="laundry-niche" />
    <rect x="{x_m1 + 20 + 60*sc}" y="{oy + h_tot - 32*sc}" width="{31*sc - 8}" height="{26*sc}" fill="#DCFCE7" stroke="#16A34A" stroke-width="1.5" rx="3"/>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc}" y="{oy + h_tot - 18*sc}" class="item-text" fill="#15803D" text-anchor="middle">WIADRO NA MOPA</text>
    
    <line x1="{x_m1 + 22 + 60*sc}" y1="{oy + h_paw + 95*sc + 15}" x2="{x_m1 + 22 + 60*sc}" y2="{oy + h_tot - 34*sc}" stroke="#16A34A" stroke-width="4" stroke-linecap="round"/>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc + 8}" y="{oy + h_paw + 95*sc + 35}" class="item-text" fill="#15803D" text-anchor="middle">KIJ DO MOPA</text>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc + 8}" y="{oy + h_paw + 95*sc + 50}" class="item-sub" fill="#166534" text-anchor="middle">uchwyt ścienny</text>
    <text x="{x_m1 + 16 + 60*sc + 15.5*sc + 8}" y="{oy + h_paw + 95*sc + 75}" class="item-text" fill="#15803D" text-anchor="middle">MISKA PIONOWO</text>
    
    <!-- MODUŁ 2: 100 CM (Drążek + 2 Szuflady + Dno gospodarcze) -->
    <rect x="{x_m2+4}" y="{oy+4}" width="{w_m2-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw/2}" class="item-text" text-anchor="middle">PAWLACZ: CZERWONA DUŻA WALIZKA (36 cm)</text>
    <line x1="{x_m2}" y1="{oy + h_paw}" x2="{x_m3}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_m2+6}" y="{oy + h_paw + 6}" width="{w_m2-12}" height="{110*sc - 12}" class="hanging-area" />
    <line x1="{x_m2+16}" y1="{oy + h_paw + 28}" x2="{x_m3-16}" y2="{oy + h_paw + 28}" class="rod" />
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 52}" class="item-text" fill="#7E22CE" font-size="12" text-anchor="middle">DRĄŻEK 100 cm: GŁÓWNA GARDEROBA (ZOSTAJE!)</text>
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 72}" class="item-text" text-anchor="middle">Garnitury w pokrowcach, koszule, marynarki, spodnie</text>
    <line x1="{x_m2}" y1="{oy + h_paw + 110*sc}" x2="{x_m3}" y2="{oy + h_paw + 110*sc}" class="shelf" />
    
    <rect x="{x_m2+6}" y="{oy + h_paw + 110*sc + 3}" width="{w_m2-12}" height="{18*sc - 6}" class="drawer" />
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 110*sc + 9*sc + 4}" class="item-text" text-anchor="middle">SZUFLADA 1 (KOMPLEMENT 100 cm): Bielizna osobista i skarpetki</text>
    <line x1="{x_m2}" y1="{oy + h_paw + 128*sc}" x2="{x_m3}" y2="{oy + h_paw + 128*sc}" class="shelf" />
    
    <rect x="{x_m2+6}" y="{oy + h_paw + 128*sc + 3}" width="{w_m2-12}" height="{18*sc - 6}" class="drawer" />
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 128*sc + 9*sc + 4}" class="item-text" text-anchor="middle">SZUFLADA 2 (KOMPLEMENT 100 cm): T-shirty, koszulki polo, odzież sportowa</text>
    <line x1="{x_m2}" y1="{oy + h_paw + 146*sc}" x2="{x_m3}" y2="{oy + h_paw + 146*sc}" class="shelf" />
    
    <!-- Dno modułu 2: kosze z praniem / duże tekstylia -->
    <rect x="{x_m2+6}" y="{oy + h_paw + 146*sc + 4}" width="{w_m2-12}" height="{(h_tot - (h_paw + 146*sc)) - 8}" fill="#F8FAFC" rx="4" />
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 146*sc + 28}" class="item-text" fill="#475569" text-anchor="middle">STREFA KOSZY NA PRANIE I POŚCIELI GOŚCINNEJ</text>
    <text x="{x_m2 + w_m2/2}" y="{oy + h_paw + 146*sc + 46}" class="item-sub" text-anchor="middle">Szeroka, otwarta przestrzeń 100 cm x 58 cm x 54 cm</text>
    
    <!-- MODUŁ 3: 50 CM (WARSZTAT TECHNICZNY: AMICA + DRABINA + PARKSIDE) -->
    <rect x="{x_m3+4}" y="{oy+4}" width="{w_m3-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m3 + w_m3/2}" y="{oy + h_paw/2 + 5}" class="item-text" text-anchor="middle">PAWLACZ</text>
    <line x1="{x_m3}" y1="{oy + h_paw}" x2="{x_m4}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_m3+6}" y="{oy + h_paw + 6}" width="{w_m3-12}" height="{120*sc - 12}" class="corp-inner" />
    
    <!-- Odkurzacz Amica -->
    <rect x="{x_m3+8}" y="{oy + h_paw + 8}" width="{28*sc}" height="{120*sc - 16}" class="vacuum-area" />
    <text x="{x_m3 + 8 + 14*sc}" y="{oy + h_paw + 30}" class="item-text" fill="#6D28D9" text-anchor="middle">ODKURZACZ</text>
    <text x="{x_m3 + 8 + 14*sc}" y="{oy + h_paw + 46}" class="item-text" fill="#6D28D9" text-anchor="middle">AMICA</text>
    <text x="{x_m3 + 8 + 14*sc}" y="{oy + h_paw + 62}" class="item-sub" fill="#7C3AED" text-anchor="middle">z wężem</text>
    <text x="{x_m3 + 8 + 14*sc}" y="{oy + h_paw + 78}" class="item-sub" fill="#7C3AED" text-anchor="middle">+ akcesoria</text>
    
    <!-- Drabina -->
    <rect x="{x_m3 + 12 + 28*sc}" y="{oy + h_paw + 8}" width="{w_m3 - 28*sc - 20}" height="{120*sc - 16}" class="ladder-area" />
    <text x="{x_m3 + 12 + 28*sc + (w_m3 - 28*sc - 20)/2}" y="{oy + h_paw + 60*sc}" class="item-text" text-anchor="middle" transform="rotate(-90 {x_m3 + 12 + 28*sc + (w_m3 - 28*sc - 20)/2} {oy + h_paw + 60*sc})">DRABINA ALUMINIOWA</text>
    
    <line x1="{x_m3}" y1="{oy + h_paw + 120*sc}" x2="{x_m4}" y2="{oy + h_paw + 120*sc}" class="shelf" />
    
    <!-- TRZY PÓŁKI WARSZTATOWE PARKSIDE -->
    <rect x="{x_m3+6}" y="{oy + h_paw + 120*sc + 4}" width="{w_m3-12}" height="{23*sc}" fill="#F1F5F9" rx="3"/>
    <text x="{x_m3 + w_m3/2}" y="{oy + h_paw + 120*sc + 18}" class="item-text" text-anchor="middle">PÓŁKA 1: Wkrętarka Parkside + Akumulatory</text>
    <line x1="{x_m3}" y1="{oy + h_paw + 147*sc}" x2="{x_m4}" y2="{oy + h_paw + 147*sc}" class="shelf" />
    
    <rect x="{x_m3+6}" y="{oy + h_paw + 147*sc + 4}" width="{w_m3-12}" height="{23*sc}" fill="#F1F5F9" rx="3"/>
    <text x="{x_m3 + w_m3/2}" y="{oy + h_paw + 147*sc + 18}" class="item-text" text-anchor="middle">PÓŁKA 2: Skrzynka z narzędziami / wkręty</text>
    <line x1="{x_m3}" y1="{oy + h_paw + 174*sc}" x2="{x_m4}" y2="{oy + h_paw + 174*sc}" class="shelf" />
    
    <rect x="{x_m3+6}" y="{oy + h_paw + 174*sc + 4}" width="{w_m3-12}" height="{23*sc}" class="basket"/>
    <text x="{x_m3 + w_m3/2}" y="{oy + h_paw + 174*sc + 18}" class="item-sub" font-weight="700" text-anchor="middle">PÓŁKA 3 / KOSZ: Chemia techniczna, taśmy, kleje</text>
    
    <!-- MODUŁ 4: 20 CM -->
    <rect x="{x_m4+4}" y="{oy+4}" width="{w_m4-8}" height="{h_paw-8}" fill="#F8FAFC" rx="4"/>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_paw/2 - 4}" class="item-text" font-size="10" text-anchor="middle">ŻELAZ-</text>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_paw/2 + 10}" class="item-text" font-size="10" text-anchor="middle">KO</text>
    <line x1="{x_m4}" y1="{oy + h_paw}" x2="{ox + w_tot}" y2="{oy + h_paw}" class="shelf" />
    
    <rect x="{x_m4+4}" y="{oy + h_paw + 6}" width="{w_m4-8}" height="{h_tot - h_paw - 12}" fill="#F8FAFC" stroke="#94A3B8" stroke-dasharray="2,2" rx="3"/>
    <text x="{x_m4 + w_m4/2}" y="{oy + h_tot/2}" class="item-text" font-size="10" text-anchor="middle" transform="rotate(-90 {x_m4 + w_m4/2} {oy + h_tot/2})">DESKA DO PRASOWANIA</text>
    
    {h_dim(ox, ox + w_tot, oy, "ŁĄCZNA SZEROKOŚĆ ZABUDOWY PAX 58: 270 cm", -45)}
    </svg>'''
    
    with open(f"{OUT_DIR}/szafa_3_istniejacy_pax_58_wariant_3.svg", "w") as f:
        f.write(svg)
    render_svg_to_png(f"{OUT_DIR}/szafa_3_istniejacy_pax_58_wariant_3.svg", f"{OUT_DIR}/szafa_3_istniejacy_pax_58_wariant_3.png", 1260, 1080)

# ==============================================================================
# 10. PANORAMA CAŁEGO UKŁADU W JEDNEJ SKALI (WARIANT 3)
# ==============================================================================
def gen_panorama_w3():
    sc = 2.4
    ox, oy = 90, 140
    w_pax58 = 270 * sc
    gap1 = 65
    w_pax35 = 150 * sc
    gap2 = 65
    w_wymiar = 125 * sc
    
    x_pax58 = ox
    x_pax35 = x_pax58 + w_pax58 + gap1
    x_wymiar = x_pax35 + w_pax35 + gap2
    
    h_pax = 236 * sc
    h_wymiar = 240 * sc
    
    svg_w = int(x_wymiar + w_wymiar + 90)
    svg_h = int(oy + h_wymiar + 120)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}" style="background:#FFFFFF;">
    {COMMON_STYLES}
    
    <text x="{ox}" y="42" class="title">PANORAMA UKŁADU SZAF W CAŁYM MIESZKANIU – WERSJA 2 (WARIANT 3)</text>
    <text x="{ox}" y="66" class="subtitle">Wspólna skala (1 cm = 2.4 px) | Gitara bezpieczna w PAX 35 | PAX 58 moduł 50cm to warsztat | Szafa na wymiar = 100% butów</text>
    
    <!-- 1. PAX 58 CM (WARIANT 3) -->
    <rect x="{x_pax58}" y="{oy}" width="{w_pax58}" height="{h_pax}" class="corp-frame" />
    <rect x="{x_pax58}" y="{oy-28}" width="{w_pax58}" height="24" fill="#0F172A" rx="4"/>
    <text x="{x_pax58 + w_pax58/2}" y="{oy-12}" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">1. ISTNIEJĄCY PAX 58 cm – WARSZTAT TECHNICZNY, PRALNIA &amp; GARDEROBA</text>
    
    <line x1="{x_pax58 + 100*sc}" y1="{oy}" x2="{x_pax58 + 100*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_pax58}" y1="{oy + 36*sc}" x2="{x_pax58 + 100*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 50*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Walizka czarna</text>
    
    <!-- Drążek nad suszarką -->
    <rect x="{x_pax58 + 6}" y="{oy + 40*sc}" width="{92*sc}" height="{90*sc}" class="hanging-area"/>
    <line x1="{x_pax58 + 14*sc}" y1="{oy + 55*sc}" x2="{x_pax58 + 90*sc}" y2="{oy + 55*sc}" class="rod"/>
    <text x="{x_pax58 + 50*sc}" y="{oy + 75*sc}" class="item-text" fill="#7E22CE" font-size="10" text-anchor="middle">DRĄŻEK NAD SUSZARKĄ</text>
    <text x="{x_pax58 + 50*sc}" y="{oy + 90*sc}" class="item-sub" font-size="8.5" text-anchor="middle">dosychanie / kurtki codzienne</text>
    <line x1="{x_pax58}" y1="{oy + 132*sc}" x2="{x_pax58 + 100*sc}" y2="{oy + 132*sc}" class="shelf"/>
    
    <!-- Suszarka Beko -->
    <rect x="{x_pax58 + 6}" y="{oy + 136*sc}" width="{60*sc}" height="{h_pax - 140*sc}" class="dryer-bg"/>
    <circle cx="{x_pax58 + 6 + 30*sc}" cy="{oy + 136*sc + (h_pax - 140*sc)/2}" r="45" fill="#BAE6FD" stroke="#0284C7" stroke-width="2"/>
    <text x="{x_pax58 + 6 + 30*sc}" y="{oy + 136*sc + (h_pax - 140*sc)/2 - 5}" class="item-text" fill="#0369A1" text-anchor="middle">SUSZARKA</text>
    <text x="{x_pax58 + 6 + 30*sc}" y="{oy + 136*sc + (h_pax - 140*sc)/2 + 10}" class="item-sub" fill="#0284C7" text-anchor="middle">BEKO 60cm</text>
    
    <!-- Wnęka 31 cm: Wiadro + Kij mopa -->
    <rect x="{x_pax58 + 6 + 60*sc + 4}" y="{oy + 136*sc}" width="{31*sc - 6}" height="{h_pax - 140*sc}" class="laundry-niche"/>
    <text x="{x_pax58 + 6 + 60*sc + 15*sc}" y="{oy + 136*sc + 30}" class="item-sub" fill="#15803D" font-weight="700" text-anchor="middle">KIJ MOPA</text>
    <text x="{x_pax58 + 6 + 60*sc + 15*sc}" y="{oy + 136*sc + 45}" class="item-sub" fill="#15803D" font-weight="700" text-anchor="middle">MISKA PION</text>
    <text x="{x_pax58 + 6 + 60*sc + 15*sc}" y="{oy + h_pax - 20}" class="item-sub" fill="#15803D" font-weight="700" text-anchor="middle">WIADRO</text>
    
    <!-- Moduł 2: 100 cm (2 szuflady) -->
    <line x1="{x_pax58 + 200*sc}" y1="{oy}" x2="{x_pax58 + 200*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_pax58 + 100*sc}" y1="{oy + 36*sc}" x2="{x_pax58 + 200*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Walizka czerwona</text>
    
    <rect x="{x_pax58 + 104*sc}" y="{oy + 40*sc}" width="{92*sc}" height="{105*sc}" class="hanging-area"/>
    <line x1="{x_pax58 + 110*sc}" y1="{oy + 55*sc}" x2="{x_pax58 + 190*sc}" y2="{oy + 55*sc}" class="rod"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 92*sc}" class="item-text" fill="#7E22CE" text-anchor="middle">DRĄŻEK 100 cm (Garnitury / Koszule)</text>
    <line x1="{x_pax58 + 100*sc}" y1="{oy + 147*sc}" x2="{x_pax58 + 200*sc}" y2="{oy + 147*sc}" class="shelf"/>
    
    <rect x="{x_pax58 + 104*sc}" y="{oy + 150*sc}" width="{92*sc}" height="{16*sc}" class="drawer"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 161*sc}" class="item-sub" text-anchor="middle">Szuflada 1: Bielizna / skarpetki</text>
    <line x1="{x_pax58 + 100*sc}" y1="{oy + 167*sc}" x2="{x_pax58 + 200*sc}" y2="{oy + 167*sc}" class="shelf"/>
    
    <rect x="{x_pax58 + 104*sc}" y="{oy + 170*sc}" width="{92*sc}" height="{16*sc}" class="drawer"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 181*sc}" class="item-sub" text-anchor="middle">Szuflada 2: Odzież codzienna</text>
    <line x1="{x_pax58 + 100*sc}" y1="{oy + 188*sc}" x2="{x_pax58 + 200*sc}" y2="{oy + 188*sc}" class="shelf"/>
    <text x="{x_pax58 + 150*sc}" y="{oy + 212*sc}" class="item-sub" text-anchor="middle">Dno: Kosze na pranie / pościel</text>
    
    <!-- Moduł 3: 50 cm (WARSZTAT: DRABINA + AMICA + PARKSIDE) -->
    <line x1="{x_pax58 + 250*sc}" y1="{oy}" x2="{x_pax58 + 250*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_pax58 + 200*sc}" y1="{oy + 36*sc}" x2="{x_pax58 + 250*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Pawlacz</text>
    
    <rect x="{x_pax58 + 203*sc}" y="{oy + 39*sc}" width="{28*sc}" height="{115*sc}" class="vacuum-area"/>
    <text x="{x_pax58 + 217*sc}" y="{oy + 95*sc}" class="item-text" font-size="9" fill="#6D28D9" text-anchor="middle" transform="rotate(-90 {x_pax58 + 217*sc} {oy + 95*sc})">ODKURZACZ AMICA</text>
    
    <rect x="{x_pax58 + 233*sc}" y="{oy + 39*sc}" width="{14*sc}" height="{115*sc}" class="ladder-area"/>
    <text x="{x_pax58 + 240*sc}" y="{oy + 95*sc}" class="item-sub" font-size="8" text-anchor="middle" transform="rotate(-90 {x_pax58 + 240*sc} {oy + 95*sc})">DRABINA</text>
    
    <line x1="{x_pax58 + 200*sc}" y1="{oy + 156*sc}" x2="{x_pax58 + 250*sc}" y2="{oy + 156*sc}" class="shelf"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 172*sc}" class="item-sub" font-size="8.5" text-anchor="middle">Parkside 1</text>
    <line x1="{x_pax58 + 200*sc}" y1="{oy + 180*sc}" x2="{x_pax58 + 250*sc}" y2="{oy + 180*sc}" class="shelf"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 196*sc}" class="item-sub" font-size="8.5" text-anchor="middle">Parkside 2</text>
    <line x1="{x_pax58 + 200*sc}" y1="{oy + 204*sc}" x2="{x_pax58 + 250*sc}" y2="{oy + 204*sc}" class="shelf"/>
    <text x="{x_pax58 + 225*sc}" y="{oy + 222*sc}" class="item-sub" font-size="8.5" text-anchor="middle">Chemia / Narzędzia</text>
    
    <!-- Moduł 4: 20 cm -->
    <text x="{x_pax58 + 260*sc}" y="{oy + 22*sc}" class="item-sub" font-size="8" text-anchor="middle">Żelazko</text>
    <line x1="{x_pax58 + 250*sc}" y1="{oy + 36*sc}" x2="{x_pax58 + 270*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax58 + 260*sc}" y="{oy + h_pax/2}" class="item-sub" font-size="9" font-weight="700" text-anchor="middle" transform="rotate(-90 {x_pax58 + 260*sc} {oy + h_pax/2})">DESKA DO PRASOWANIA</text>
    
    <!-- 2. NOWY PAX 35 CM (WARIANT 3: GITARA + DYSON + SZUFLADY) -->
    <rect x="{x_pax35}" y="{oy}" width="{w_pax35}" height="{h_pax}" class="corp-frame" />
    <rect x="{x_pax35}" y="{oy-28}" width="{w_pax35}" height="24" fill="#059669" rx="4"/>
    <text x="{x_pax35 + w_pax35/2}" y="{oy-12}" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">2. NOWY PAX 35 cm – BEZPIECZNA GITARA + DYSON | 6 SZUFLAD</text>
    
    <line x1="{x_pax35 + 75*sc}" y1="{oy}" x2="{x_pax35 + 75*sc}" y2="{oy + h_pax}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_pax35}" y1="{oy + 36*sc}" x2="{x_pax35 + 75*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Pudła SKUBB</text>
    
    <rect x="{x_pax35 + 4}" y="{oy + 38*sc}" width="{71*sc}" height="{26*sc}" class="paper-towel-area"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 54*sc}" class="item-sub" font-size="8.5" fill="#047857" font-weight="700" text-anchor="middle">RĘCZNIKI PAPIEROWE (DUŻA PACZKA)</text>
    <line x1="{x_pax35}" y1="{oy + 66*sc}" x2="{x_pax35 + 75*sc}" y2="{oy + 66*sc}" class="shelf"/>
    
    <!-- Gitara + Dyson w lewym module 35 cm -->
    <rect x="{x_pax35 + 4}" y="{oy + 68*sc}" width="{45*sc}" height="{105*sc}" class="guitar-area"/>
    <text x="{x_pax35 + 26.5*sc}" y="{oy + 120*sc}" class="item-text" font-size="9" fill="#B45309" text-anchor="middle" transform="rotate(-90 {x_pax35 + 26.5*sc} {oy + 120*sc})">GITARA W POKROWCU</text>
    
    <rect x="{x_pax35 + 51*sc}" y="{oy + 68*sc}" width="{22*sc}" height="{105*sc}" class="dyson-area"/>
    <text x="{x_pax35 + 62*sc}" y="{oy + 120*sc}" class="item-sub" font-size="8" fill="#BE185D" text-anchor="middle" transform="rotate(-90 {x_pax35 + 62*sc} {oy + 120*sc})">DYSON ŚCIENNY</text>
    
    <line x1="{x_pax35}" y1="{oy + 175*sc}" x2="{x_pax35 + 75*sc}" y2="{oy + 175*sc}" class="shelf"/>
    <rect x="{x_pax35 + 4}" y="{oy + 178*sc}" width="{70*sc}" height="{17*sc}" class="drawer"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 190*sc}" class="item-sub" text-anchor="middle">Szuflada 1: Akcesoria muzyczne</text>
    <rect x="{x_pax35 + 4}" y="{oy + 197*sc}" width="{70*sc}" height="{17*sc}" class="drawer"/>
    <text x="{x_pax35 + 37.5*sc}" y="{oy + 209*sc}" class="item-sub" text-anchor="middle">Szuflada 2: Ściereczki / filtry AGD</text>
    
    <!-- Prawy 75 cm (PAX 35 W3) -->
    <line x1="{x_pax35 + 75*sc}" y1="{oy + 36*sc}" x2="{x_pax35 + 150*sc}" y2="{oy + 36*sc}" class="shelf"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 22*sc}" class="item-sub" text-anchor="middle">Pudła SKUBB</text>
    
    <rect x="{x_pax35 + 78*sc}" y="{oy + 40*sc}" width="{70*sc}" height="{32*sc}" class="backpack-area"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 58*sc}" class="item-sub" font-size="8.5" fill="#1D4ED8" font-weight="700" text-anchor="middle">PLECAKI MIEJSKIE</text>
    <line x1="{x_pax35 + 75*sc}" y1="{oy + 74*sc}" x2="{x_pax35 + 150*sc}" y2="{oy + 74*sc}" class="shelf"/>
    
    <rect x="{x_pax35 + 78*sc}" y="{oy + 76*sc}" width="{70*sc}" height="{32*sc}" class="backpack-area"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 94*sc}" class="item-sub" font-size="8.5" fill="#1D4ED8" font-weight="700" text-anchor="middle">PLECAKI TURYSTYCZNE</text>
    <line x1="{x_pax35 + 75*sc}" y1="{oy + 110*sc}" x2="{x_pax35 + 150*sc}" y2="{oy + 110*sc}" class="shelf"/>
    
    <rect x="{x_pax35 + 78*sc}" y="{oy + 113*sc}" width="{70*sc}" height="{17*sc}" class="drawer"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 125*sc}" class="item-sub" text-anchor="middle">Szuflada 3: Czapki zimowe</text>
    <rect x="{x_pax35 + 78*sc}" y="{oy + 132*sc}" width="{70*sc}" height="{17*sc}" class="drawer"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 144*sc}" class="item-sub" text-anchor="middle">Szuflada 4: Rękawiczki / szale</text>
    <rect x="{x_pax35 + 78*sc}" y="{oy + 151*sc}" width="{70*sc}" height="{17*sc}" class="drawer"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 163*sc}" class="item-sub" text-anchor="middle">Szuflada 5: Okulary / etui / klucze</text>
    <rect x="{x_pax35 + 78*sc}" y="{oy + 170*sc}" width="{70*sc}" height="{17*sc}" class="drawer"/>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 182*sc}" class="item-sub" text-anchor="middle">Szuflada 6: Drobne AGD / latarki</text>
    <text x="{x_pax35 + 112.5*sc}" y="{oy + 215*sc}" class="item-sub" font-size="8.5" text-anchor="middle">Dno: Zapasy higieniczne</text>
    
    <!-- 3. SZAFA NA WYMIAR (PO PRAWEJ) -->
    <rect x="{x_wymiar}" y="{oy}" width="{w_wymiar}" height="{h_wymiar}" class="corp-frame" />
    <rect x="{x_wymiar}" y="{oy-28}" width="{w_wymiar}" height="24" fill="#7E22CE" rx="4"/>
    <text x="{x_wymiar + w_wymiar/2}" y="{oy-12}" fill="#FFFFFF" font-size="12" font-weight="700" text-anchor="middle">3. SZAFA NA WYMIAR (125 cm) – JEDYNA BAZA BUTÓW</text>
    
    <line x1="{x_wymiar + 12*sc}" y1="{oy}" x2="{x_wymiar + 12*sc}" y2="{oy + h_wymiar}" stroke="#94A3B8" stroke-dasharray="2,2"/>
    <line x1="{x_wymiar + 64*sc}" y1="{oy}" x2="{x_wymiar + 64*sc}" y2="{oy + h_wymiar}" stroke="#0F172A" stroke-width="2"/>
    <line x1="{x_wymiar + 115*sc}" y1="{oy}" x2="{x_wymiar + 115*sc}" y2="{oy + h_wymiar}" stroke="#94A3B8" stroke-dasharray="2,2"/>
    
    <line x1="{x_wymiar}" y1="{oy + 45*sc}" x2="{x_wymiar + w_wymiar}" y2="{oy + 45*sc}" class="shelf"/>
    <text x="{x_wymiar + 38*sc}" y="{oy + 26*sc}" class="item-sub" text-anchor="middle">Pawlacz 50cm</text>
    <text x="{x_wymiar + 89*sc}" y="{oy + 26*sc}" class="item-sub" text-anchor="middle">Nadstawka 51cm</text>
    
    <rect x="{x_wymiar + 14*sc}" y="{oy + 48*sc}" width="{48*sc}" height="{156*sc}" class="hanging-area"/>
    <line x1="{x_wymiar + 18*sc}" y1="{oy + 65*sc}" x2="{x_wymiar + 60*sc}" y2="{oy + 65*sc}" class="rod"/>
    <text x="{x_wymiar + 38*sc}" y="{oy + 105*sc}" class="item-text" font-size="10" fill="#7E22CE" text-anchor="middle">DRĄŻEK 160 cm</text>
    <text x="{x_wymiar + 38*sc}" y="{oy + 120*sc}" class="item-text" font-size="9" text-anchor="middle">DŁUGIE PŁASZCZE</text>
    <line x1="{x_wymiar + 12*sc}" y1="{oy + 205*sc}" x2="{x_wymiar + 64*sc}" y2="{oy + 205*sc}" class="shelf"/>
    <rect x="{x_wymiar + 14*sc}" y="{oy + 208*sc}" width="{48*sc}" height="{30*sc}" class="drawer"/>
    <text x="{x_wymiar + 38*sc}" y="{oy + 224*sc}" class="item-sub" text-anchor="middle">Szuflada 35cm</text>
    
    '''
    sh_step_w = (h_wymiar - 45*sc) / 8.0
    for i in range(8):
        y_w = oy + 45*sc + i * sh_step_w
        if i < 7:
            svg += f'<line x1="{x_wymiar + 64*sc}" y1="{y_w + sh_step_w}" x2="{x_wymiar + 115*sc}" y2="{y_w + sh_step_w}" class="shelf"/>'
        label = "Czapki / szale" if i < 3 else f"BUTY BIEŻĄCE {i-2}"
        color = "#64748B" if i < 3 else "#1E40AF"
        svg += f'<text x="{x_wymiar + 89*sc}" y="{y_w + sh_step_w/2 + 3}" class="item-sub" font-size="8.5" fill="{color}" font-weight="{"700" if i>=3 else "500"}" text-anchor="middle">{label}</text>'
        
    svg += f'''
    <g transform="translate(0, {oy + h_wymiar + 35})">
        {h_dim(x_pax58, x_pax58 + w_pax58, 0, "SZEROKOŚĆ PAX 58: 270 cm", 0)}
        {h_dim(x_pax35, x_pax35 + w_pax35, 0, "NOWY PAX 35: 150 cm", 0)}
        {h_dim(x_wymiar, x_wymiar + w_wymiar, 0, "NA WYMIAR: 125 cm", 0)}
    </g>
    </svg>'''
    
    with open(f"{OUT_DIR}/03_panorama_wersja_2_wariant_3.svg", "w") as f:
        f.write(svg)
    render_svg_to_png(f"{OUT_DIR}/03_panorama_wersja_2_wariant_3.svg", f"{OUT_DIR}/03_panorama_wersja_2_wariant_3.png", svg_w, svg_h)

# Execute all generators
print("Generating all Wersja 2 drawings...")
gen_szafa_wejscie()

# Wariant 1
gen_nowy_pax_35_w1()
gen_istniejacy_pax_58_w1()
gen_panorama_w1()

# Wariant 2
gen_nowy_pax_35_w2()
gen_istniejacy_pax_58_w2()
gen_panorama_w2()

# Wariant 3
gen_nowy_pax_35_w3()
gen_istniejacy_pax_58_w3()
gen_panorama_w3()

print("All Wersja 2 drawings (3 complete wardrobe variants + 3 panoramas) successfully built and rendered!")

