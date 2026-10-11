# -*- coding: utf-8 -*-
"""مولّد شعارات جولدن فيل: ثلاثة اتجاهات × (ألوان / معكوس / أحادي) × (كامل / أيقونة)."""
import os, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.varLib.instancer import instantiateVariableFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
BUILD = os.path.join(HERE, "build")
os.makedirs(BUILD, exist_ok=True)

PAL = dict(olive="#8C7F3E", olive_light="#B8A95E", char="#1B1A18", cream="#EDE6D8", stone="#CFC6B2", deep="#4A4526")

def _jost(w):
    p = os.path.join(BUILD, f"Jost-{w}.ttf")
    if not os.path.exists(p):
        f = TTFont(os.path.join(FONTS, "Jost.ttf"))
        instantiateVariableFont(f, {"wght": w}, inplace=True)
        f.save(p)
    return p
JOST_L = _jost(300)
JOST_R = _jost(400)
PLEX_L = os.path.join(FONTS, "IBMPlexSansArabic-Light.ttf")
PLEX_R = os.path.join(FONTS, "IBMPlexSansArabic-Regular.ttf")

_cache = {}
def text_path(fontfile, text, size, tracking=0.0):
    """نص مشكّل (HarfBuzz) إلى مسار SVG، الأصل: يسار-خط الأساس. يرجع (d, width)."""
    if fontfile not in _cache:
        blob = hb.Blob.from_file_path(fontfile); face = hb.Face(blob)
        _cache[fontfile] = (hb.Font(face), face.upem, TTFont(fontfile))
    font, upem, tt = _cache[fontfile]
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    gs = tt.getGlyphSet(); order = tt.getGlyphOrder(); s = size / upem
    x = 0.0; out = []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}")
        tp = TransformPen(pen, (s, 0, 0, -s, x + pos.x_offset * s, -pos.y_offset * s))
        gs[order[info.codepoint]].draw(tp)
        out.append(pen.getCommands())
        x += pos.x_advance * s + tracking * size
    return " ".join(out), x - tracking * size

# ---- حروف هندسية أحادية الوزن (ارتفاع 100) ----
GL = {
 "G": (100, "M86 19.8 A47 47 0 1 0 97 50 H52"),
 "O": (100, "M3 50 A47 47 0 1 0 97 50 A47 47 0 1 0 3 50 Z"),
 "L": (62,  "M3 0 V97 H58"),
 "D": (96,  "M3 3 H46 A47 47 0 0 1 46 97 H3 Z"),
 "E": (62,  "M58 3 H3 V97 H58 M3 50 H50"),
 "N": (80,  "M3 100 V0 L77 100 V0"),
 "V": (86,  "M3 0 L43 100 L83 0"),
 "A": (86,  "M3 100 L43 0 L83 100 M14.5 70 H71.5"),
}
def mono_word(word, x0, y0, s, gap, sw):
    """يرسم كلمة بالحروف الهندسية. يرجع (svg, عرض، [x لكل حرف])."""
    x = 0; parts = []; xs = []
    for ch in word:
        w, d = GL[ch]; xs.append(x)
        parts.append(f'<path d="{d}" transform="translate({x0 + x*s:.2f} {y0}) scale({s})" stroke-width="{sw/s:.3f}"/>')
        x += w + gap
    return "".join(parts), (x - gap) * s, xs

def _wrap(body, vb, c, a, title, pad=0):
    x, y, w, h = vb
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x-pad:.1f} {y-pad:.1f} {w+2*pad:.1f} {h+2*pad:.1f}" '
            f'width="{w+2*pad:.0f}" height="{h+2*pad:.0f}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>')

STROKE = 'fill="none" stroke-linejoin="bevel" stroke-linecap="butt"'
LAT_TAG = "ADVERTISING & EVENTS MANAGEMENT"
AR_TAG = "دعاية وإعلان وتنظيم فعاليات"

def _tag(cx, y_lat, y_ar, c, lat_size=18, ar_size=25, with_ar=True):
    d1, w1 = text_path(JOST_L, LAT_TAG, lat_size, 0.32)
    s = f'<path d="{d1}" fill="{c}" transform="translate({cx-w1/2:.2f} {y_lat})"/>'
    if with_ar:
        d2, w2 = text_path(PLEX_L, AR_TAG, ar_size)
        s += f'<path d="{d2}" fill="{c}" transform="translate({cx-w2/2:.2f} {y_ar})"/>'
    return s

# ---------- الاتجاه أ: الوادي المفتوح ----------
def icon_A(c, a):
    return (f'<g {STROKE}><path d="M42 74 L100 176 L158 74" stroke="{c}" stroke-width="9"/>'
            f'<path d="M24 42 H176" stroke="{a}" stroke-width="9"/></g>'), (0, 0, 200, 200)

def logo_A(c, a, tagline=True):
    sw = 6
    g, W, xs = mono_word("GOLDEN", 0, 0, 1, 30, sw)
    ox = xs[1]  # موضع حرف O
    horizon = f'<path d="M{ox-22} -30 H{ox+122}" stroke="{a}" stroke-width="{sw}"/>'
    s2 = 0.36
    v, w2, _ = mono_word("VALE", 0, 0, s2, 110, 3.2)
    v = v.replace('translate(', f'translate(').replace('translate(0 0)', 'translate(0 0)')
    vx = (W - w2) / 2
    vale = f'<g transform="translate({vx:.2f} 138)">{v}</g>'
    body = f'<g {STROKE} stroke="{c}">{g}{vale}</g><g {STROKE}>{horizon}</g>'
    top = -33; bottom = 176
    if tagline:
        body += _tag(W/2, 216, 262, c)
        bottom = 272
    return body, (0, top, W, bottom - top)

# ---------- الاتجاه ب: استمرارية المثلث ----------
def icon_B(c, a):
    ax, ay, lx, rx, by = 100, 20, 20, 180, 160
    mL = ((ax+lx)/2, (ay+by)/2); mR = ((ax+rx)/2, (ay+by)/2); mB = (100, by)
    tL = ((ax+mL[0])/2, (ay+mL[1])/2); tR = ((ax+mR[0])/2, (ay+mR[1])/2); tB = (100, mL[1])
    sw = 3.2
    body = (f'<g fill="none" stroke="{c}" stroke-width="{sw}" stroke-linejoin="miter">'
            f'<path d="M{ax} {ay} L{lx} {by} H{rx} Z"/>'
            f'<path d="M{mL[0]} {mL[1]} L{mR[0]} {mR[1]} L{mB[0]} {mB[1]} Z"/>'
            f'<path d="M{tL[0]} {tL[1]} L{tR[0]} {tR[1]} L{tB[0]} {tB[1]} Z"/></g>'
            f'<path d="M{lx} {by} L{mL[0]} {mL[1]} L{mB[0]} {mB[1]} Z" fill="{a}"/>')
    return body, (0, 0, 200, 180)

def logo_B(c, a, tagline=True):
    ib, _ = icon_B(c, a)
    sw = 5; s = 0.52
    g, W1, _ = mono_word("GOLDEN", 0, 0, s, 34, sw)
    v, W2, _ = mono_word("VALE", 0, 0, s, 34, sw)
    gapw = 70 * s * 1.6
    total = W1 + gapw + W2
    isz = 0.62
    body = f'<g transform="translate({(total-200*isz)/2:.2f} 0) scale({isz})">{ib}</g>'
    y0 = 180 * isz + 36
    body += (f'<g {STROKE} stroke="{c}"><g transform="translate(0 {y0:.1f})">{g}</g>'
             f'<g transform="translate({W1+gapw:.2f} {y0:.1f})">{v}</g></g>')
    bottom = y0 + 100 * s
    if tagline:
        body += _tag(total/2, bottom + 36, bottom + 70, c, 13, 18)
        bottom += 80
    return body, (0, 0, total, bottom)

# ---------- الاتجاه ج: العربية أولًا ----------
def icon_C(c, a):
    return (f'<g {STROKE}><circle cx="100" cy="100" r="92" stroke="{c}" stroke-width="3"/>'
            f'<path d="M58 78 L100 150 L142 78" stroke="{c}" stroke-width="7"/>'
            f'<path d="M44 52 H156" stroke="{a}" stroke-width="7"/></g>'), (0, 0, 200, 200)

def logo_C(c, a, tagline=True):
    d, w = text_path(PLEX_L, "جولدن فيل", 150)
    W = max(w, 520)
    body = f'<path d="{d}" fill="{c}" transform="translate({(W-w)/2:.2f} 0)"/>'
    # خط الأفق فوق الكلمة
    body += f'<path d="M{(W-w)/2+10:.1f} -130 H{(W+w)/2-10:.1f}" stroke="{a}" stroke-width="5" fill="none"/>'
    g, Wl, _ = mono_word("GOLDEN", 0, 0, 0.2, 30, 3.4)
    v, Wv, _ = mono_word("VALE", 0, 0, 0.2, 30, 3.4)
    tot = Wl + 40 + Wv
    y = 60
    body += (f'<g {STROKE} stroke="{c}"><g transform="translate({(W-tot)/2:.1f} {y})">{g}</g>'
             f'<g transform="translate({(W-tot)/2+Wl+40:.1f} {y})">{v}</g></g>')
    bottom = y + 20
    if tagline:
        d2, w2 = text_path(PLEX_L, AR_TAG, 24)
        body += f'<path d="{d2}" fill="{c}" transform="translate({(W-w2)/2:.1f} {bottom+40})"/>'
        bottom += 52
    return body, (0, -135, W, bottom + 135)

DIRS = {"A": (logo_A, icon_A), "B": (logo_B, icon_B), "C": (logo_C, icon_C)}
NAMES = {"A": "A-open-valley", "B": "B-triangle-heritage", "C": "C-arabic-first"}
MODES = {
    "color":   (PAL["char"],  PAL["olive"]),
    "reverse": (PAL["cream"], PAL["olive_light"]),
    "mono":    ("#000000",    "#000000"),
    "white":   ("#FFFFFF",    "#FFFFFF"),
    "ink":     (PAL["char"],  PAL["char"]),
    "paper":   (PAL["cream"], PAL["cream"]),
}

def get(direction, kind="logo", mode="color", pad=0, tagline=True):
    c, a = MODES[mode]
    if kind == "logo":
        body, vb = DIRS[direction][0](c, a, tagline)
    else:
        body, vb = DIRS[direction][1](c, a)
    return _wrap(body, vb, c, a, f"Golden Vale — {NAMES[direction]} — {kind}", pad), vb

def write_all(outdir):
    os.makedirs(outdir, exist_ok=True)
    n = 0
    for d in "ABC":
        for kind in ("logo", "icon"):
            for mode in MODES:
                svg, _ = get(d, kind, mode)
                open(os.path.join(outdir, f"golden-vale_{NAMES[d]}_{kind}_{mode}.svg"), "w", encoding="utf-8").write(svg)
                n += 1
    return n

if __name__ == "__main__":
    print(write_all(os.path.join(HERE, "logos")), "svg")
