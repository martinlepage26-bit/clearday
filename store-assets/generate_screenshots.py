#!/usr/bin/env python3
"""Generate App Store screenshots for Clearday (1242×2688px, 6.5" iPhone)."""

from PIL import Image, ImageDraw, ImageFont
import os, math

W, H = 1242, 2688
OUT = os.path.dirname(os.path.abspath(__file__)) + "/screenshots"
os.makedirs(OUT, exist_ok=True)

# ─── Brand colours ────────────────────────────────────────────────────────────
BG          = "#F7F8F5"
PRIMARY     = "#2D6A4F"
PRIMARY_L   = "#52B788"
PRIMARY_MUT = "#D8F3DC"
WHITE       = "#FFFFFF"
CARD        = "#FFFFFF"
FG          = "#1A2E24"
MUTED       = "#6B7280"
BORDER      = "#E5E7E3"
DANGER      = "#F87171"
WARN        = "#FCA5A5"
AMBER       = "#FDE68A"

# ─── Font helpers ─────────────────────────────────────────────────────────────
def font(size, bold=False):
    candidates = [
        f"/usr/share/fonts/truetype/dejavu/DejaVuSans{'-Bold' if bold else ''}.ttf",
        f"/usr/share/fonts/truetype/liberation/LiberationSans{'-Bold' if bold else '-Regular'}.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def fnt(size): return font(size, False)
def fntb(size): return font(size, True)

# ─── Drawing primitives ───────────────────────────────────────────────────────
def rounded_rect(draw, xy, radius, fill, outline=None, outline_width=2):
    x0, y0, x1, y1 = xy
    r = radius
    draw.rectangle([x0+r, y0, x1-r, y1], fill=fill)
    draw.rectangle([x0, y0+r, x1, y1-r], fill=fill)
    draw.ellipse([x0, y0, x0+2*r, y0+2*r], fill=fill)
    draw.ellipse([x1-2*r, y0, x1, y0+2*r], fill=fill)
    draw.ellipse([x0, y1-2*r, x0+2*r, y1], fill=fill)
    draw.ellipse([x1-2*r, y1-2*r, x1, y1], fill=fill)
    if outline:
        draw.arc([x0, y0, x0+2*r, y0+2*r], 180, 270, fill=outline, width=outline_width)
        draw.arc([x1-2*r, y0, x1, y0+2*r], 270, 360, fill=outline, width=outline_width)
        draw.arc([x0, y1-2*r, x0+2*r, y1], 90, 180, fill=outline, width=outline_width)
        draw.arc([x1-2*r, y1-2*r, x1, y1], 0, 90, fill=outline, width=outline_width)
        draw.line([x0+r, y0, x1-r, y0], fill=outline, width=outline_width)
        draw.line([x0+r, y1, x1-r, y1], fill=outline, width=outline_width)
        draw.line([x0, y0+r, x0, y1-r], fill=outline, width=outline_width)
        draw.line([x1, y0+r, x1, y1-r], fill=outline, width=outline_width)

def card(draw, x, y, w, h, shadow=True):
    if shadow:
        rounded_rect(draw, [x+4, y+4, x+w+4, y+h+4], 20, "#00000015")
    rounded_rect(draw, [x, y, x+w, y+h], 20, CARD, BORDER, 2)

def status_bar(draw, light=False):
    col = WHITE if not light else FG
    draw.text((80, 68), "9:41", font=fntb(40), fill=col, anchor="lm")
    # battery icon
    draw.rectangle([1100, 54, 1162, 82], outline=col, width=3)
    draw.rectangle([1162, 62, 1168, 74], fill=col)
    draw.rectangle([1103, 57, 1143, 79], fill=col)
    # signal bars
    for i, bh in enumerate([14, 22, 30, 38]):
        bx = 1060 - i*18
        draw.rectangle([bx, 82-bh, bx+10, 82], fill=col)

def tab_bar(draw, img, active=0):
    # tab bar background
    draw.rectangle([0, H-160, W, H], fill=WHITE)
    draw.line([0, H-160, W, H-160], fill=BORDER, width=2)
    tabs = [("🏠", "Home"), ("📋", "Log"), ("💬", "Ask"), ("📊", "Patterns"), ("⚙️", "More")]
    tw = W // len(tabs)
    for i, (icon, label) in enumerate(tabs):
        cx = i * tw + tw // 2
        cy = H - 100
        col = PRIMARY if i == active else MUTED
        draw.text((cx, cy - 20), icon, font=fnt(44), fill=col, anchor="mm")
        draw.text((cx, cy + 30), label, font=fnt(28), fill=col, anchor="mm")
    return img

def new_screen():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    return img, draw

def save(img, name):
    path = f"{OUT}/{name}.png"
    img.save(path, "PNG")
    print(f"  ✓ {name}.png")
    return path

# ─── Screen 1 — Onboarding splash ─────────────────────────────────────────────
def screen_01():
    img = Image.new("RGB", (W, H), PRIMARY)
    draw = ImageDraw.Draw(img)

    # subtle pattern — circles
    for r in [300, 500, 700, 900]:
        draw.ellipse([W//2-r, H//2-r-200, W//2+r, H//2+r-200], outline="#FFFFFF18", width=3)

    # logo leaf shape
    cx, cy = W//2, 820
    draw.ellipse([cx-120, cy-160, cx+120, cy+160], fill="#52B788")
    draw.ellipse([cx-80, cy-200, cx+200, cy+80], fill="#74C69D")

    draw.text((W//2, 1060), "Clearday", font=fntb(96), fill=WHITE, anchor="mm")
    draw.text((W//2, 1180), "Your perimenopause companion", font=fnt(52), fill="#B7E4C7", anchor="mm")

    # 3 value props
    props = [
        ("📋", "Track what's changing"),
        ("💬", "Get answers, not dismissal"),
        ("📊", "See your patterns"),
    ]
    y = 1400
    for icon, text in props:
        rounded_rect(draw, [W//2-380, y, W//2+380, y+110], 22, "#FFFFFF18")
        draw.text((W//2-320, y+55), icon, font=fnt(54), fill=WHITE, anchor="lm")
        draw.text((W//2-240, y+55), text, font=fnt(46), fill=WHITE, anchor="lm")
        y += 140

    # CTA button
    rounded_rect(draw, [W//2-320, 2100, W//2+320, 2220], 32, WHITE)
    draw.text((W//2, 2160), "Get started", font=fntb(56), fill=PRIMARY, anchor="mm")

    draw.text((W//2, 2400), "Free • Private • Science-backed", font=fnt(38), fill="#B7E4C7", anchor="mm")
    return save(img, "01_welcome")

# ─── Screen 2 — Dashboard ─────────────────────────────────────────────────────
def screen_02():
    img, draw = new_screen()
    status_bar(draw)

    draw.text((80, 200), "Good morning, Sarah 👋", font=fntb(58), fill=FG)
    draw.text((80, 278), "Your dashboard", font=fnt(40), fill=MUTED)

    # Quick action cards
    card(draw, 72, 340, 500, 170)
    draw.text((132, 410), "📋", font=fnt(56), fill=FG, anchor="lm")
    draw.text((210, 398), "Log Symptoms", font=fntb(42), fill=FG)
    draw.text((210, 452), "Tap to track today", font=fnt(34), fill=MUTED)

    card(draw, 608, 340, 500, 170)
    draw.text((668, 410), "📅", font=fnt(56), fill=FG, anchor="lm")
    draw.text((746, 398), "Log Cycle", font=fntb(42), fill=FG)
    draw.text((746, 452), "Day 14 today", font=fnt(34), fill=MUTED)

    # Streak banner
    rounded_rect(draw, [72, 548, W-72, 664], 20, PRIMARY_MUT)
    draw.text((152, 606), "🔥", font=fnt(60), fill=FG, anchor="lm")
    draw.text((232, 606), "7-day streak — keep going!", font=fntb(46), fill=PRIMARY, anchor="lm")

    # Recent patterns card
    card(draw, 72, 700, W-144, 320)
    draw.text((132, 750), "Recent pattern", font=fntb(48), fill=FG)
    symptoms = [("Hot flashes", 3, "#FCA5A5"), ("Night sweats", 2, "#FDE68A"), ("Mood changes", 1, "#D8F3DC")]
    sy = 820
    for name, level, col in symptoms:
        rounded_rect(draw, [132, sy, 132+W-280, sy+60], 10, col)
        draw.text((152, sy+30), name, font=fnt(36), fill=FG, anchor="lm")
        bar_w = int((W-400) * level / 4)
        rounded_rect(draw, [W-380, sy+10, W-380+bar_w, sy+50], 8, PRIMARY_L)
        draw.text((W-120, sy+30), f"Mild", font=fnt(34), fill=MUTED, anchor="rm")
        sy += 80

    # Clinician summary CTA
    card(draw, 72, 1058, W-144, 180)
    draw.text((132, 1128), "📄  Generate clinician summary", font=fntb(44), fill=PRIMARY)
    draw.text((132, 1188), "Share with your doctor", font=fnt(36), fill=MUTED)

    # Recent logs
    draw.text((80, 1278), "Recent logs", font=fntb(48), fill=FG)
    logs = [("Today", "Hot flashes · Night sweats", "Moderate"), ("Yesterday", "Mood · Fatigue", "Mild"), ("Jun 3", "Sleep · Hot flashes", "Severe")]
    ly = 1340
    for date, syms, sev in logs:
        card(draw, 72, ly, W-144, 130)
        draw.text((132, ly+45), date, font=fntb(38), fill=FG)
        draw.text((132, ly+95), syms, font=fnt(34), fill=MUTED)
        sev_col = {"Mild": "#D8F3DC", "Moderate": "#FDE68A", "Severe": "#FCA5A5"}[sev]
        rounded_rect(draw, [W-230, ly+35, W-100, ly+85], 10, sev_col)
        draw.text((W-165, ly+60), sev, font=fnt(30), fill=FG, anchor="mm")
        ly += 152

    tab_bar(draw, img, active=0)
    return save(img, "02_dashboard")

# ─── Screen 3 — Symptom logging ───────────────────────────────────────────────
def screen_03():
    img, draw = new_screen()
    status_bar(draw)

    draw.text((80, 200), "Log Symptoms", font=fntb(64), fill=FG)
    draw.text((80, 284), "Thursday, June 5", font=fnt(42), fill=MUTED)

    # Tab switcher
    rounded_rect(draw, [72, 340, W-72, 420], 20, BORDER)
    rounded_rect(draw, [76, 344, W//2-4, 416], 18, PRIMARY)
    draw.text((W//4, 382), "Symptoms", font=fntb(40), fill=WHITE, anchor="mm")
    draw.text((3*W//4, 382), "Cycle", font=fntb(40), fill=MUTED, anchor="mm")

    # Vasomotor section
    draw.text((80, 464), "Vasomotor", font=fntb(44), fill=FG)
    sections = [
        ("Hot Flashes", 3),
        ("Night Sweats", 1),
    ]
    y = 520
    for label, val in sections:
        draw.text((80, y), label, font=fnt(40), fill=FG)
        y += 54
        colors = ["#E5E7E3", "#D8F3DC", "#FDE68A", "#FCA5A5", "#C4B5FD"]
        labels = ["None", "Mild", "Mod", "Sev", "V.Sev"]
        bw = (W-160-48) // 5
        for i in range(5):
            bx = 80 + i*(bw+12)
            bg = colors[i] if i == val else "#F3F4F1"
            bord = PRIMARY if i == val else BORDER
            rounded_rect(draw, [bx, y, bx+bw, y+80], 12, bg, bord, 3)
            draw.text((bx+bw//2, y+40), labels[i], font=fnt(30), fill=FG, anchor="mm")
        y += 108

    # Mood section
    draw.line([80, y, W-80, y], fill=BORDER, width=2); y += 24
    draw.text((80, y), "Mood", font=fntb(44), fill=FG); y += 56
    mood_items = [("Mood changes", 2), ("Anxiety", 1), ("Brain fog", 0), ("Irritability", 1)]
    for label, val in mood_items:
        draw.text((80, y), label, font=fnt(40), fill=FG)
        y += 52
        colors = ["#E5E7E3", "#D8F3DC", "#FDE68A", "#FCA5A5", "#C4B5FD"]
        bw = (W-160-48) // 5
        for i in range(5):
            bx = 80 + i*(bw+12)
            bg = colors[i] if i == val else "#F3F4F1"
            bord = PRIMARY if i == val else BORDER
            rounded_rect(draw, [bx, y, bx+bw, y+70], 10, bg, bord, 3)
            draw.text((bx+bw//2, y+35), str(i), font=fnt(28), fill=FG, anchor="mm")
        y += 98

    # Save button
    rounded_rect(draw, [80, H-220, W-80, H-120], 28, PRIMARY)
    draw.text((W//2, H-170), "Save today's log", font=fntb(52), fill=WHITE, anchor="mm")

    tab_bar(draw, img, active=1)
    return save(img, "03_log_symptoms")

# ─── Screen 4 — Cycle logging ─────────────────────────────────────────────────
def screen_04():
    img, draw = new_screen()
    status_bar(draw)

    draw.text((80, 200), "Log Cycle", font=fntb(64), fill=FG)
    draw.text((80, 284), "Track your changing cycle", font=fnt(42), fill=MUTED)

    # Tab switcher
    rounded_rect(draw, [72, 340, W-72, 420], 20, BORDER)
    rounded_rect(draw, [W//2+4, 344, W-76, 416], 18, PRIMARY)
    draw.text((W//4, 382), "Symptoms", font=fntb(40), fill=MUTED, anchor="mm")
    draw.text((3*W//4, 382), "Cycle", font=fntb(40), fill=WHITE, anchor="mm")

    # Bleeding field
    card(draw, 72, 460, W-144, 220)
    draw.text((132, 520), "Bleeding", font=fntb(44), fill=FG)
    draw.text((132, 574), "Flow level today", font=fnt(36), fill=MUTED)
    flows = ["None", "Spotting", "Light", "Medium", "Heavy"]
    cols =  ["#E5E7E3","#FDE68A","#FCA5A5","#F87171","#DC2626"]
    bw = (W-200) // 5
    for i, (fl, fc) in enumerate(zip(flows, cols)):
        bx = 100 + i*bw
        bg = fc if i == 2 else "#F3F4F1"
        rounded_rect(draw, [bx, 628, bx+bw-12, 688], 10, bg, BORDER, 2)
        draw.text((bx+bw//2-6, 658), fl, font=fnt(27), fill=FG, anchor="mm")

    # Cycle notes
    card(draw, 72, 718, W-144, 260)
    draw.text((132, 778), "Cycle notes", font=fntb(44), fill=FG)
    draw.text((132, 834), "Any cramps, spotting, or changes?", font=fnt(36), fill=MUTED)
    rounded_rect(draw, [112, 892, W-112, 972], 12, "#F7F8F5", BORDER, 2)
    draw.text((140, 932), "Mild cramps this morning…", font=fnt(36), fill=MUTED, anchor="lm")

    # Cycle stats
    card(draw, 72, 1016, W-144, 360)
    draw.text((132, 1066), "Your cycle at a glance", font=fntb(44), fill=FG)
    stats = [("Average cycle length", "28 days"), ("Last period start", "May 22"), ("Current day", "Day 14"), ("Phase", "Ovulatory")]
    sy = 1130
    for label, val in stats:
        draw.text((132, sy), label, font=fnt(36), fill=MUTED)
        draw.text((W-132, sy), val, font=fntb(36), fill=PRIMARY, anchor="rm")
        sy += 68

    # Perimenopause info banner
    rounded_rect(draw, [72, 1420, W-72, 1560], 20, PRIMARY_MUT)
    draw.text((132, 1472), "💡  Perimenopause & cycles", font=fntb(38), fill=PRIMARY)
    draw.text((132, 1524), "Irregular cycles are a hallmark of perimenopause.\nClearday helps you spot what's changing and why.", font=fnt(34), fill=PRIMARY)

    # Save button
    rounded_rect(draw, [80, H-220, W-80, H-120], 28, PRIMARY)
    draw.text((W//2, H-170), "Save today's log", font=fntb(52), fill=WHITE, anchor="mm")

    tab_bar(draw, img, active=1)
    return save(img, "04_log_cycle")

# ─── Screen 5 — Ask AI ────────────────────────────────────────────────────────
def screen_05():
    img, draw = new_screen()
    status_bar(draw)

    draw.text((W//2, 200), "Ask Clearday", font=fntb(58), fill=FG, anchor="mm")
    draw.text((W//2, 270), "Evidence-based • Private • Always available", font=fnt(36), fill=MUTED, anchor="mm")

    # Info banner
    rounded_rect(draw, [60, 316, W-60, 428], 20, PRIMARY_MUT)
    draw.text((W//2, 372), "💡  Educational guidance — not medical advice", font=fnt(38), fill=PRIMARY, anchor="mm")

    # Chat messages
    msgs = [
        ("user", "Why are my hot flashes worse at night?"),
        ("assistant", "Hot flashes — including night sweats — are often triggered by fluctuating estrogen levels. During sleep, your body temperature regulation changes, making you more sensitive to these hormonal shifts.\n\nCommon evidence-based strategies include keeping your bedroom cool (65–68°F), wearing moisture-wicking fabrics, and avoiding alcohol or spicy foods in the evening."),
        ("user", "Should I ask my doctor about HRT?"),
        ("assistant", "HRT (hormone replacement therapy) is an effective option for many people and worth discussing with your healthcare provider. ✅"),
    ]

    y = 460
    for role, text in msgs:
        if role == "user":
            # right-aligned bubble
            lines = [text[i:i+34] for i in range(0, len(text), 34)]
            bh = 32 + len(lines) * 52
            bw = min(900, max(300, len(text)*18))
            rounded_rect(draw, [W-80-bw, y, W-80, y+bh], 22, PRIMARY)
            ty = y + 20
            for line in lines:
                draw.text((W-100, ty), line, font=fnt(36), fill=WHITE, anchor="rm")
                ty += 52
            y += bh + 24
        else:
            lines = []
            for part in text.split("\n"):
                chunk = [part[i:i+38] for i in range(0, len(part), 38)] if part else [""]
                lines.extend(chunk)
            bh = 40 + len(lines) * 50
            rounded_rect(draw, [60, y, 60+min(1060, W-80), y+bh], 22, CARD, BORDER, 2)
            ty = y + 20
            for line in lines:
                draw.text((90, ty), line, font=fnt(36), fill=FG, anchor="lm")
                ty += 50
            y += bh + 24

    # Input bar
    rounded_rect(draw, [60, H-240, W-60, H-140], 28, CARD, BORDER, 3)
    draw.text((120, H-190), "Ask a question…", font=fnt(42), fill=MUTED, anchor="lm")
    rounded_rect(draw, [W-180, H-228, W-72, H-152], 20, PRIMARY)
    draw.text((W-126, H-190), "↑", font=fntb(52), fill=WHITE, anchor="mm")

    tab_bar(draw, img, active=2)
    return save(img, "05_ask_ai")

# ─── Screen 6 — Patterns ──────────────────────────────────────────────────────
def screen_06():
    img, draw = new_screen()
    status_bar(draw)

    draw.text((80, 200), "Patterns", font=fntb(64), fill=FG)
    draw.text((80, 284), "Your symptom insights", font=fnt(42), fill=MUTED)

    # Symptom frequency card
    card(draw, 72, 344, W-144, 480)
    draw.text((132, 400), "Symptom frequency — last 30 days", font=fntb(42), fill=FG)
    symptom_freq = [
        ("Hot flashes", 22, "#FCA5A5"),
        ("Night sweats", 18, "#FDE68A"),
        ("Sleep disruption", 15, "#C4B5FD"),
        ("Brain fog", 11, "#A7F3D0"),
        ("Mood changes", 9, "#FCA5A5"),
        ("Fatigue", 8, "#FDE68A"),
    ]
    sy = 468
    max_days = 30
    for sym, days, col in symptom_freq:
        draw.text((132, sy), sym, font=fnt(36), fill=FG)
        bar_full = W - 144 - 200 - 80
        bar_w = int(bar_full * days / max_days)
        rounded_rect(draw, [132, sy+46, 132+bar_w, sy+76], 8, col)
        draw.text((W-112-80, sy+61), f"{days}d", font=fntb(34), fill=MUTED, anchor="rm")
        sy += 88

    # Impact trend
    card(draw, 72, 860, W-144, 300)
    draw.text((132, 918), "Functional impact trend", font=fntb(42), fill=FG)
    draw.text((132, 972), "How symptoms affect daily life", font=fnt(36), fill=MUTED)
    # Simple sparkline
    points = [4, 6, 5, 7, 8, 6, 4, 3, 5, 4, 3, 2, 4, 3]
    cx0, cy0, cw, ch = 132, 1020, W-280, 100
    for i in range(1, len(points)):
        x1 = cx0 + (i-1) * cw // (len(points)-1)
        x2 = cx0 + i * cw // (len(points)-1)
        y1 = cy0 + ch - int(points[i-1]/10*ch)
        y2 = cy0 + ch - int(points[i]/10*ch)
        draw.line([x1, y1, x2, y2], fill=PRIMARY_L, width=6)
        draw.ellipse([x2-8, y2-8, x2+8, y2+8], fill=PRIMARY)
    draw.text((132, 1140), "▼ Improving", font=fntb(38), fill=PRIMARY_L)

    # Cycle length card
    card(draw, 72, 1200, W-144, 260)
    draw.text((132, 1258), "Recent cycle lengths", font=fntb(42), fill=FG)
    cycles = [26, 31, 28, 29, 25, 32]
    bar_w = (W-280) // len(cycles)
    for i, length in enumerate(cycles):
        bx = 132 + i*bar_w
        bh = int(80 * length / 35)
        col = PRIMARY if i == len(cycles)-1 else PRIMARY_L
        rounded_rect(draw, [bx+10, 1380-bh, bx+bar_w-10, 1380], 6, col)
        draw.text((bx+bar_w//2, 1408), str(length), font=fnt(30), fill=MUTED, anchor="mm")
    draw.text((132, 1436), "Days per cycle", font=fnt(34), fill=MUTED)

    # Stats row
    card(draw, 72, 1500, W-144, 200)
    draw.text((132, 1560), "Quick stats", font=fntb(44), fill=FG)
    stats = [("Total logs", "47"), ("Best streak", "12 days"), ("Top symptom", "Hot flashes")]
    sw = (W-200)//3
    for i, (label, val) in enumerate(stats):
        cx = 120 + i*sw + sw//2
        draw.text((cx, 1640), val, font=fntb(44), fill=PRIMARY, anchor="mm")
        draw.text((cx, 1690), label, font=fnt(30), fill=MUTED, anchor="mm")

    tab_bar(draw, img, active=3)
    return save(img, "06_patterns")

# ─── Screen 7 — Learn / Articles ──────────────────────────────────────────────
def screen_07():
    img, draw = new_screen()
    status_bar(draw)

    draw.text((80, 200), "Learn", font=fntb(64), fill=FG)
    draw.text((80, 284), "Evidence-based articles", font=fnt(42), fill=MUTED)

    articles = [
        ("Understanding HRT", "Hormone therapy explained: benefits, risks, and who it helps.", "5 min read", PRIMARY_MUT),
        ("Managing hot flashes naturally", "Lifestyle changes that can reduce frequency and intensity.", "7 min read", "#FDE68A"),
        ("Sleep & perimenopause", "Why sleep disrupts during the transition and how to improve it.", "4 min read", "#C4B5FD"),
        ("Bone health after 40", "How estrogen fluctuation affects bone density and what to do.", "6 min read", "#FCA5A5"),
        ("Brain fog: what's normal?", "Cognitive changes in perimenopause and evidence-based tips.", "5 min read", PRIMARY_MUT),
        ("Talking to your doctor", "How to advocate for yourself when symptoms get dismissed.", "3 min read", "#A7F3D0"),
    ]
    y = 348
    for title, desc, time, col in articles:
        card(draw, 72, y, W-144, 200)
        rounded_rect(draw, [112, y+30, 112+60, y+90], 10, col)
        draw.text((142, y+60), "📖", font=fnt(36), fill=FG, anchor="mm")
        draw.text((196, y+58), title, font=fntb(40), fill=FG)
        # wrap description
        words = desc.split()
        line, lines = [], []
        for w in words:
            if len(" ".join(line + [w])) > 40:
                lines.append(" ".join(line)); line = [w]
            else:
                line.append(w)
        if line: lines.append(" ".join(line))
        for j, l in enumerate(lines[:2]):
            draw.text((196, y+112+j*42), l, font=fnt(32), fill=MUTED)
        draw.text((196, y+168), time, font=fnt(30), fill=PRIMARY)
        y += 224

    tab_bar(draw, img, active=0)
    return save(img, "07_learn")

# ─── Screen 8 — Clinician summary ─────────────────────────────────────────────
def screen_08():
    img, draw = new_screen()
    status_bar(draw)

    draw.text((80, 200), "Clinician Summary", font=fntb(60), fill=FG)
    draw.text((80, 284), "Share with your healthcare provider", font=fnt(40), fill=MUTED)

    # Generate button
    rounded_rect(draw, [72, 340, W-72, 456], 24, PRIMARY)
    draw.text((W//2, 398), "✨  Generate new summary", font=fntb(50), fill=WHITE, anchor="mm")

    # Questions input
    card(draw, 72, 494, W-144, 200)
    draw.text((132, 550), "Questions for your doctor (optional)", font=fntb(40), fill=FG)
    rounded_rect(draw, [112, 610, W-112, 686], 12, "#F7F8F5", BORDER, 2)
    draw.text((140, 648), "e.g. Should I try HRT?", font=fnt(36), fill=MUTED, anchor="lm")

    # Summary card
    card(draw, 72, 732, W-144, 980)
    draw.text((132, 792), "Summary — June 5, 2026", font=fntb(44), fill=FG)
    draw.text((132, 848), "Generated for Dr. Tremblay", font=fnt(36), fill=MUTED)
    draw.line([112, 894, W-112, 894], fill=BORDER, width=2)
    summary_lines = [
        "SYMPTOM OVERVIEW (last 30 days)",
        "",
        "Vasomotor: Hot flashes reported on 22/30",
        "days, rated moderate–severe. Night sweats",
        "on 18/30 days.",
        "",
        "Sleep: Disrupted sleep on 15/30 days,",
        "correlated with night sweat episodes.",
        "",
        "Mood: Mood changes (9/30), anxiety (6/30),",
        "brain fog (11/30 days).",
        "",
        "CYCLE DATA",
        "Last 6 cycles: 26, 31, 28, 29, 25, 32 days.",
        "Irregular pattern consistent with",
        "perimenopause.",
        "",
        "PATIENT QUESTIONS",
        "• Should I consider HRT options?",
        "• Are these changes normal for my age?",
    ]
    ty = 920
    for line in summary_lines:
        col = PRIMARY if line.isupper() else FG if line else BG
        f = fntb(32) if line.isupper() else fnt(32)
        draw.text((132, ty), line, font=f, fill=col)
        ty += 44

    # Share button
    rounded_rect(draw, [72, 1752, W-72, 1862], 24, WHITE, PRIMARY, 3)
    draw.text((W//2, 1807), "Share with doctor  ↑", font=fntb(48), fill=PRIMARY, anchor="mm")

    tab_bar(draw, img, active=0)
    return save(img, "08_summary")

# ─── Screen 9 — Settings ──────────────────────────────────────────────────────
def screen_09():
    img, draw = new_screen()
    status_bar(draw)

    draw.text((80, 200), "Settings", font=fntb(64), fill=FG)

    # Profile card
    card(draw, 72, 284, W-144, 200)
    draw.ellipse([112, 304, 232, 424], fill=PRIMARY_MUT)
    draw.text((172, 364), "SL", font=fntb(52), fill=PRIMARY, anchor="mm")
    draw.text((264, 354), "Sarah Lévesque", font=fntb(46), fill=FG)
    draw.text((264, 410), "sarah.l@email.com", font=fnt(36), fill=MUTED)

    sections = [
        ("Preferences", [("Language", "English", None), ("Notifications", "Daily reminder 8am", None), ("Theme", "Light", None)]),
        ("Privacy", [("Data export", "Download your data", None), ("Delete account", "Remove all data", DANGER)]),
        ("About", [("Version", "1.0.0", None), ("Privacy policy", "", None), ("Terms of service", "", None)]),
    ]
    y = 524
    for section_title, items in sections:
        draw.text((80, y), section_title, font=fntb(40), fill=MUTED); y += 54
        card(draw, 72, y, W-144, len(items)*108)
        for i, (label, value, col) in enumerate(items):
            iy = y + i*108 + 54
            draw.text((132, iy), label, font=fntb(38), fill=col or FG, anchor="lm")
            draw.text((W-132, iy), value + "  ›", font=fnt(36), fill=col or MUTED, anchor="rm")
            if i < len(items)-1:
                draw.line([132, y+(i+1)*108, W-132, y+(i+1)*108], fill=BORDER, width=1)
        y += len(items)*108 + 36

    tab_bar(draw, img, active=0)
    return save(img, "09_settings")

# ─── Screen 10 — Feature highlight (promo) ────────────────────────────────────
def screen_10():
    img = Image.new("RGB", (W, H), PRIMARY)
    draw = ImageDraw.Draw(img)

    # Gradient-like top
    for i in range(400):
        alpha = int(255 * (1 - i/400) * 0.3)
        draw.line([0, i, W, i], fill=f"#{alpha:02x}ff{alpha:02x}")

    draw.text((W//2, 180), "Perimenopause is real.", font=fntb(72), fill=WHITE, anchor="mm")
    draw.text((W//2, 270), "Now you have answers.", font=fnt(68), fill="#B7E4C7", anchor="mm")

    features = [
        ("📋", "Daily symptom tracker", "Log hot flashes, mood, sleep & more"),
        ("💬", "AI health companion", "Ask anything — no dismissal, no judgment"),
        ("📊", "Pattern insights", "Understand what's triggering your symptoms"),
        ("📄", "Doctor-ready summaries", "Go into appointments prepared"),
        ("🔒", "Private & secure", "Your data stays yours, always"),
    ]
    y = 400
    for icon, title, desc in features:
        rounded_rect(draw, [72, y, W-72, y+160], 24, "#FFFFFF14")
        draw.text((136, y+80), icon, font=fnt(64), fill=WHITE, anchor="mm")
        draw.text((220, y+44), title, font=fntb(46), fill=WHITE)
        draw.text((220, y+104), desc, font=fnt(36), fill="#B7E4C7")
        y += 184

    rounded_rect(draw, [W//2-360, H-360, W//2+360, H-220], 36, WHITE)
    draw.text((W//2, H-290), "Download Clearday", font=fntb(56), fill=PRIMARY, anchor="mm")
    draw.text((W//2, H-220+30), "Free · Built for perimenopause", font=fnt(40), fill="#B7E4C7", anchor="mm")

    return save(img, "10_feature_highlight")

# ─── App Previews (3 frames, landscape-friendly tall cards) ───────────────────
def preview(n, title, subtitle, color, icon):
    img = Image.new("RGB", (W, H), color)
    draw = ImageDraw.Draw(img)
    # Large icon area
    cx, cy = W//2, 700
    draw.ellipse([cx-240, cy-240, cx+240, cy+240], fill="#FFFFFF30")
    draw.text((cx, cy), icon, font=fnt(200), fill=WHITE, anchor="mm")
    draw.text((W//2, 1060), title, font=fntb(80), fill=WHITE, anchor="mm")
    draw.text((W//2, 1170), subtitle, font=fnt(52), fill="#FFFFFF99", anchor="mm")
    # mini phone mockup
    rounded_rect(draw, [W//2-260, 1280, W//2+260, 1980], 40, "#FFFFFF20", "#FFFFFF40", 4)
    rounded_rect(draw, [W//2-240, 1300, W//2+240, 1960], 36, "#FFFFFF10")
    draw.text((W//2, 1620), "Clearday", font=fntb(56), fill=WHITE, anchor="mm")
    draw.text((W//2, 2200), f"Preview {n}/3", font=fnt(40), fill="#FFFFFF60", anchor="mm")
    return save(img, f"preview_{n:02d}")

print("Generating Clearday App Store assets…")
screen_01()
screen_02()
screen_03()
screen_04()
screen_05()
screen_06()
screen_07()
screen_08()
screen_09()
screen_10()
preview(1, "Track your symptoms", "Daily logging in under a minute", "#2D6A4F", "📋")
preview(2, "Ask anything", "AI guidance, evidence-based", "#1B4332", "💬")
preview(3, "See your patterns", "Understand your body better", "#081C15", "📊")
print(f"\nAll assets saved to {OUT}/")
