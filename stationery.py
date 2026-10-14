# -*- coding: utf-8 -*-
"""مقتنيات هوية Golden Vale للطباعة: بطاقة، ورق رسمي، مظروف، ورقة تعريف، بطاقة موظف، غلاف مجلد، صورة رمزية، توقيع بريد.
المقاسات بالمليمتر؛ ما فيه قص (bleed) 3 مم. اللون RGB هنا ويُحوَّل إلى CMYK بعدها."""
import json, os
from common import logo, P
BUILD = "build"
PHONE, MAIL, CR = "0506221548", "fd-0@hotmail.com", "7055194109"
ADDR = "الرياض، المملكة العربية السعودية"
N = lambda s: f'<span class="ltr">{s}</span>'

BASE = """
@font-face{font-family:'Jost';src:url('../fonts/Jost.ttf');font-weight:100 900}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-Light.ttf');font-weight:300}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-Regular.ttf');font-weight:400}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-Medium.ttf');font-weight:500}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-SemiBold.ttf');font-weight:600}
*{box-sizing:border-box;margin:0;padding:0}
:root{--olive:#8C7F3E;--olive-l:#B8A95E;--char:#1B1A18;--cream:#EDE6D8;--deep:#4A4526;--paper:#F6F2E9}
html,body{-webkit-print-color-adjust:exact;print-color-adjust:exact;background:#fff}
body{font-family:'Plex','Jost',sans-serif;color:var(--char)}
.pg{position:relative;overflow:hidden;page-break-after:always;break-after:page}
.ltr{direction:ltr;unicode-bidi:isolate;display:inline-block;font-family:'Jost',sans-serif;font-weight:400;letter-spacing:.02em}
.abs{position:absolute}
.lat{font-family:'Jost';letter-spacing:.3em;text-transform:uppercase;font-weight:300}
"""
def doc(name, w, h, pages, extra=""):
    css = BASE + f"@page{{size:{w}mm {h}mm;margin:0}}.pg{{width:{w}mm;height:{h}mm}}" + extra
    html = f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><title>Golden Vale — {name}</title><style>{css}</style></head><body>{"".join(pages)}</body></html>'
    open(f"{BUILD}/st_{name}.html", "w", encoding="utf-8").write(html)

# ---- بطاقات العمل: 90×50 + قص 3 مم = 96×56 ----
people = json.load(open("cards.json", encoding="utf-8"))
pgs = []
for p in people:
    pgs.append(f'<div class="pg" style="background:var(--char)"><div class="abs" style="left:0;right:0;top:0;bottom:0;display:flex;align-items:center;justify-content:center"><div style="width:54mm">{logo("A","logo","paper",tagline=False)}</div></div></div>')
    pgs.append(f'''<div class="pg" style="background:var(--cream)">
 <div class="abs" style="right:9mm;top:9mm;width:60mm"><div style="font-size:12pt;font-weight:600;line-height:1.3">{p["name"]}</div><div style="font-size:7.5pt;color:var(--deep);margin-top:1mm;font-weight:400">{p["title"]}</div></div>
 <div class="abs" style="left:9mm;top:9mm;width:11mm">{logo("A","icon","ink")}</div>
 <div class="abs" style="right:9mm;bottom:9mm;font-size:7.5pt;line-height:1.9;font-weight:400">
   <div>{N(p["phone"])}</div><div>{N(p["email"])}</div><div style="font-weight:300">{ADDR}</div></div>
 <div class="abs" style="left:9mm;bottom:9mm;font-size:6pt;color:var(--deep)" ><span class="lat" style="font-size:6pt">Golden Vale</span></div></div>''')
doc("business-card", 96, 56, pgs)

# ---- ورق رسمي A4 (للطباعة المكتبية: بلا قص ولا خلفيات) ----
foot = f'<div class="abs" style="left:18mm;right:18mm;bottom:11mm;border-top:0.2mm solid #d9d4c7;padding-top:3mm;display:flex;justify-content:space-between;font-size:8pt;color:var(--deep);font-weight:400"><span>{ADDR}</span><span>{N(PHONE)} · {N(MAIL)}</span><span>السجل التجاري {N(CR)}</span></div>'
doc("letterhead", 210, 297, [f'<div class="pg" style="background:#fff"><div class="abs" style="left:18mm;top:16mm;width:54mm">{logo("A","logo","ink")}</div>{foot}</div>'])

# ---- ورقة تعريف DL 210×99 ----
doc("compliments-slip", 210, 99, [f'<div class="pg" style="background:#fff"><div class="abs" style="left:14mm;top:10mm;width:40mm">{logo("A","logo","ink")}</div><div class="abs" style="right:14mm;top:12mm;font-size:12pt;color:var(--deep);font-weight:300">مع تحياتنا</div><div class="abs" style="left:14mm;right:14mm;bottom:8mm;display:flex;justify-content:space-between;font-size:7.5pt;color:var(--deep)"><span>{ADDR}</span><span>{N(PHONE)} · {N(MAIL)}</span></div></div>'])

# ---- مظروف DL 220×110 + قص = 226×116 (وجه + ظهر) ----
env_front = f'<div class="pg" style="background:#fff"><div class="abs" style="left:13mm;top:13mm;width:42mm">{logo("A","logo","ink",tagline=False)}</div><div class="abs" style="right:13mm;bottom:13mm;font-size:7.5pt;color:var(--deep);line-height:1.8;text-align:right"><div style="font-weight:500">Golden Vale</div><div>{ADDR}</div><div>{N(PHONE)}</div></div></div>'
env_back = f'<div class="pg" style="background:var(--char)"><div class="abs" style="left:0;right:0;top:0;bottom:0;display:flex;align-items:center;justify-content:center"><div style="width:58mm">{logo("A","logo","paper",tagline=False)}</div></div></div>'
doc("envelope-DL", 226, 116, [env_front, env_back])

# ---- بطاقة موظف CR80: 54×86 + قص = 60×92 ----
idf = f'''<div class="pg" style="background:var(--char);color:var(--cream)"><div class="abs" style="left:0;right:0;top:9mm;display:flex;justify-content:center"><div style="width:36mm">{logo("A","logo","paper",tagline=False)}</div></div>
 <div class="abs" style="left:17mm;top:30mm;width:26mm;height:32mm;background:rgba(237,230,216,.1);border:0.3mm dashed rgba(237,230,216,.4);display:flex;align-items:center;justify-content:center;font-size:6pt;text-align:center">[صورة]</div>
 <div class="abs" style="left:0;right:0;top:66mm;text-align:center"><div style="font-size:11pt;font-weight:600">[الاسم]</div><div style="font-size:7pt;margin-top:1mm;font-weight:300">[المسمى الوظيفي]</div></div></div>'''
idb = f'''<div class="pg" style="background:var(--cream)"><div class="abs" style="left:0;right:0;top:12mm;display:flex;justify-content:center"><div style="width:14mm">{logo("A","icon","ink")}</div></div>
 <div class="abs" style="left:8mm;right:8mm;top:34mm;text-align:center;font-size:7pt;line-height:2;font-weight:400"><div style="font-weight:600">Golden Vale</div><div>{ADDR}</div><div>{N(PHONE)}</div><div>{N(MAIL)}</div><div style="color:var(--deep);margin-top:3mm;font-size:6pt">السجل التجاري {N(CR)}</div></div>
 <div class="abs" style="left:8mm;right:8mm;bottom:8mm;text-align:center;font-size:5.5pt;color:var(--deep);line-height:1.7;font-weight:300">هذه البطاقة ملك للشركة وتُعاد عند انتهاء العمل. إن وجدتها فنرجو الاتصال بالرقم أعلاه.</div></div>'''
doc("id-card", 60, 92, [idf, idb])

# ---- غلاف مجلد (فنّي بلا قالب قص): واجهة يمين + ظهر يسار، 446×311 ----
fold = f'''<div class="pg" style="background:var(--char);color:var(--cream)">
 <div class="abs" style="right:0;top:0;bottom:0;width:223mm;display:flex;align-items:center;justify-content:center"><div style="width:110mm">{logo("A","logo","paper")}</div></div>
 <div class="abs" style="left:0;top:0;bottom:0;width:223mm"><div class="abs" style="left:0;right:0;top:120mm;display:flex;justify-content:center"><div style="width:22mm">{logo("A","icon","paper")}</div></div>
   <div class="abs" style="left:0;right:0;bottom:22mm;text-align:center;font-size:10pt;line-height:2;font-weight:300"><div>{ADDR}</div><div>{N(PHONE)} · {N(MAIL)}</div></div></div></div>'''
doc("folder-cover-artwork", 446, 311, [fold])

# ---- صورة رمزية 1080 (PNG) ----
av = lambda bg, mode: f'<div style="width:1080px;height:1080px;background:{bg};display:flex;align-items:center;justify-content:center"><div style="width:560px">{logo("A","icon",mode)}</div></div>'
open(f"{BUILD}/st_avatar_dark.html", "w", encoding="utf-8").write(f'<!doctype html><meta charset="utf-8"><style>body{{margin:0}}</style>{av("#1B1A18","paper")}')
open(f"{BUILD}/st_avatar_light.html", "w", encoding="utf-8").write(f'<!doctype html><meta charset="utf-8"><style>body{{margin:0}}</style>{av("#EDE6D8","ink")}')
open(f"{BUILD}/st_logo_white.html", "w", encoding="utf-8").write(f'<!doctype html><meta charset="utf-8"><style>body{{margin:0;background:#fff}}</style><div style="width:640px;padding:30px;background:#fff">{logo("A","logo","ink")}</div>')
print("ok")
