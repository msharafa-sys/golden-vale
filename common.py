# -*- coding: utf-8 -*-
import re, logos
P = logos.PAL
P["paper"] = "#F6F2E9"

def sv(svg, width=None, extra=""):
    s = re.sub(r'(<svg[^>]*?) width="[^"]*" height="[^"]*"', r'\1', svg, count=1)
    st = f'width:{width};' if width else 'width:100%;'
    return s.replace("<svg ", f'<svg style="{st}height:auto;display:block;{extra}" ', 1)

def logo(d="A", kind="logo", mode="color", width="100%", pad=0, tagline=True, extra=""):
    return sv(logos.get(d, kind, mode, pad, tagline)[0], width, extra)

CSS = """
@font-face{font-family:'Jost';src:url('../fonts/Jost.ttf');font-weight:100 900}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-ExtraLight.ttf');font-weight:200}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-Light.ttf');font-weight:300}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-Regular.ttf');font-weight:400}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-Medium.ttf');font-weight:500}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-SemiBold.ttf');font-weight:600}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-Bold.ttf');font-weight:700}
@page{size:1920px 1080px;margin:0}
:root{--olive:#8C7F3E;--olive-l:#B8A95E;--char:#1B1A18;--cream:#EDE6D8;--stone:#CFC6B2;--deep:#4A4526;--paper:#F6F2E9}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#777}
body{font-family:'Plex','Jost',sans-serif;color:var(--char);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;break-after:page;background:var(--paper)}
.dark{background:var(--char);color:var(--cream)}
.cream{background:var(--cream)}
.lat{font-family:'Jost',sans-serif;letter-spacing:.32em;text-transform:uppercase;font-weight:300}
.num{font-family:'Jost',sans-serif;font-weight:200;letter-spacing:.02em}
.hdr{position:absolute;top:56px;left:120px;right:120px;display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid rgba(140,127,62,.45);padding-bottom:22px;font-size:22px;color:var(--deep)}
.dark .hdr{color:var(--olive-l);border-color:rgba(184,169,94,.4)}
.hdr .lat{font-size:17px;color:inherit}
.ftr{position:absolute;bottom:44px;left:120px;right:120px;display:flex;justify-content:space-between;font-size:16px;color:var(--deep);opacity:.8}
.dark .ftr{color:var(--olive-l)}
h1{font-weight:600;font-size:76px;line-height:1.25}
h2{font-weight:600;font-size:56px;line-height:1.3}
h3{font-weight:500;font-size:34px;line-height:1.4}
p{font-weight:300;font-size:27px;line-height:1.95}
.small{font-size:20px}
.olive{color:var(--olive)}.deepc{color:var(--deep)}
.rule{height:3px;width:120px;background:var(--olive)}
.ph{border:2px dashed rgba(140,127,62,.7);color:var(--deep);display:flex;align-items:center;justify-content:center;text-align:center;font-size:20px;font-weight:400;background:rgba(237,230,216,.5)}
.dark .ph{color:var(--olive-l);background:rgba(255,255,255,.04);border-color:rgba(184,169,94,.6)}
.tag{position:absolute;font-size:15px;background:var(--olive);color:#fff;padding:3px 12px;font-weight:500;letter-spacing:.04em}
.ltr{direction:ltr;unicode-bidi:isolate;display:inline-block}
"""

def art(kind, w, h, fg="#B8A95E", bg="transparent", op=.5):
    """رسوم تجريدية بديلة عن الصور (لا صور مسروقة ولا ادعاءات)."""
    if kind == "valley":
        lines = ""
        for i in range(-2, 14):
            y = i * 70
            lines += f'<path d="M-40 {y} L{w/2} {y+h*0.55} L{w+40} {y}" fill="none" stroke="{fg}" stroke-width="{1.5 if i%3 else 3}" opacity="{op}"/>'
        lines += f'<path d="M0 {h*0.2} H{w}" stroke="{fg}" stroke-width="3" opacity="{op+.2}"/>'
    elif kind == "beams":
        lines = ""
        n = 15
        for i in range(n):
            x = w * (i + .5) / n
            lines += f'<path d="M{x:.0f} 0 L{w/2 + (x-w/2)*2.6:.0f} {h}" stroke="{fg}" stroke-width="1.4" opacity="{op}"/>'
        lines += f'<path d="M0 {h*0.78} H{w}" stroke="{fg}" stroke-width="3" opacity="{op+.2}"/>'
    elif kind == "tri":
        lines = ""
        for i in range(9):
            s = 80 + i * 60
            cx, cy = w / 2, h * .62
            lines += f'<path d="M{cx} {cy-s*.75:.0f} L{cx-s:.0f} {cy+s*.5:.0f} H{cx+s:.0f} Z" fill="none" stroke="{fg}" stroke-width="1.5" opacity="{op}"/>'
        lines += f'<path d="M0 {h*.18} H{w}" stroke="{fg}" stroke-width="3" opacity="{op+.2}"/>'
    else:  # grid
        lines = ""
        for i in range(0, int(w), 60): lines += f'<path d="M{i} 0 V{h}" stroke="{fg}" stroke-width="1" opacity="{op*.6}"/>'
        for j in range(0, int(h), 60): lines += f'<path d="M0 {j} H{w}" stroke="{fg}" stroke-width="1" opacity="{op*.6}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" style="width:100%;height:100%;display:block;background:{bg}" preserveAspectRatio="xMidYMid slice">{lines}</svg>'

def html(title, pages):
    return f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><title>{title}</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
