# -*- coding: utf-8 -*-
"""عرض سعر جولدن فيل بالهوية (الاتجاه أ). الاستعمال: python3 quote.py [quote.json] ثم render."""
import sys, json, html as H
from common import logo, P
D = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "quote.json", encoding="utf-8"))
OUT = sys.argv[2] if len(sys.argv) > 2 else "build/quote.html"
qfmt = lambda v: f"{v:,.2f}".rstrip("0").rstrip(".")
E = H.escape
money = lambda v: f"{v:,.2f}"
def cell(v, fmt=str): return fmt(v) if v is not None else "—"

rows = ""; sub = 0.0; priced = False
for i, it in enumerate(D["items"], 1):
    q, p = it.get("qty"), it.get("price")
    tot = q * p if (q is not None and p is not None) else None
    if tot is not None: sub += tot; priced = True
    rows += (f'<tr><td class="c">{i:02d}</td><td><b>{E(it["desc"])}</b>{"".join(f'<div class="ln">{E(l)}</div>' for l in it.get("lines", []))}</td><td class="c">{E(it["unit"])}</td>'
             f'<td class="c num">{cell(q, qfmt)}</td><td class="n num">{cell(p, money)}</td><td class="n num">{cell(tot, money)}</td></tr>')
disc = D.get("discount", 0) or 0
net = sub - disc; vat = net * D.get("vat_rate", .15); grand = net + vat
T = lambda v: money(v) if priced else "—"
NUM = lambda s: f'<span class="ltr num">{E(s)}</span>'
cl = D["client"]
CL = "<br>".join(f"<b>{k}:</b> {E(cl[f])}" for k, f in (("المسؤول","contact"),("الجوال","phone"),("البريد","email"),("المشروع","project")) if cl.get(f))
terms = "".join(f"<li>{E(t)}</li>" for t in D["terms"])

CSS = """
@font-face{font-family:'Jost';src:url('../fonts/Jost.ttf');font-weight:100 900}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-Light.ttf');font-weight:300}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-Regular.ttf');font-weight:400}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-Medium.ttf');font-weight:500}
@font-face{font-family:'Plex';src:url('../fonts/IBMPlexSansArabic-SemiBold.ttf');font-weight:600}
@page{size:794px 1123px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
:root{--olive:#8C7F3E;--olive-l:#B8A95E;--char:#1B1A18;--cream:#EDE6D8;--deep:#4A4526;--paper:#F6F2E9}
html,body{background:#777;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'Plex','Jost',sans-serif;color:var(--char);font-size:14px}
.page{width:794px;height:1123px;background:#fff;position:relative;overflow:hidden;padding:52px 56px}
.top{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:1px solid #ddd5c3;padding-bottom:22px}
.title{text-align:right}.title h1{font-size:38px;font-weight:600;line-height:1.2}
.title .lat{font-family:Jost;font-weight:300;letter-spacing:.32em;font-size:12px;color:var(--olive);text-transform:uppercase}
.meta{display:grid;grid-template-columns:auto auto;gap:4px 16px;margin-top:12px;font-size:13px;color:var(--deep);justify-content:start}
.meta b{font-weight:500;color:var(--char)}
.num{font-family:'Jost',sans-serif;font-weight:400;letter-spacing:.02em}
.ltr{direction:ltr;unicode-bidi:isolate;display:inline-block}
.parties{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:26px}
.box{background:var(--paper);padding:16px 18px}
.box h3{font-size:12px;font-weight:600;color:var(--deep);letter-spacing:.04em;margin-bottom:8px}
.box .nm{font-size:16px;font-weight:600;margin-bottom:6px}
.box div{font-size:12.5px;line-height:1.85;font-weight:300}
.box b{font-weight:500}
table{width:100%;border-collapse:collapse;margin-top:24px}
th{background:var(--char);color:var(--cream);font-weight:500;font-size:12.5px;padding:10px 10px;text-align:right}
th.c,td.c{text-align:center}th.n,td.n{text-align:left}
td{padding:11px 10px;border-bottom:1px solid #ddd5c3;font-size:13px;font-weight:300}
tr:nth-child(even) td{background:#fbf9f4}
.row{display:flex;gap:26px;align-items:flex-start;margin-top:22px}
.totals{width:300px;flex:none}
.totals div{display:flex;justify-content:space-between;padding:8px 10px;font-size:13.5px;border-bottom:1px solid #e6dfcd}
.totals .g{background:var(--char);color:var(--cream);font-weight:600;font-size:16px;border:none;padding:11px 10px}
.terms{flex:1}.terms h3{font-size:14px;font-weight:600;margin-bottom:6px;color:var(--deep)}
.terms ol{padding-right:18px;font-size:12px;line-height:1.85;font-weight:300}
.sign{position:absolute;right:56px;left:56px;bottom:100px;display:flex;justify-content:space-between;font-size:13px}
.sign .l{width:230px;border-top:1px solid var(--char);padding-top:8px}
.sign small{display:block;color:var(--deep);font-size:11.5px;font-weight:300}
.foot{position:absolute;right:0;left:0;bottom:0;height:70px;background:var(--char);color:var(--cream);display:flex;align-items:center;justify-content:space-between;padding:0 56px;font-size:11.5px;font-weight:300}
.foot .lat{font-family:Jost;letter-spacing:.3em;font-size:10.5px;color:var(--olive-l);text-transform:uppercase}
.ph{color:var(--deep)}
td b{font-weight:600;font-size:13.5px}.ln{font-size:11.5px;line-height:1.75;color:var(--deep);font-weight:300;margin-top:3px}
"""
body = f'''<div class="page">
 <div class="top">
  <div class="title"><div class="lat">Quotation</div><h1>عرض سعر</h1>
   <div class="meta"><b>رقم العرض</b><span>{NUM(D["number"])}</span><b>التاريخ</b><span>{E(D["date"])}</span><b>سريان العرض</b><span>{E(D["valid_days"])} يومًا من تاريخه</span></div></div>
  <div style="width:215px">{logo("A","logo","ink",tagline=True)}</div></div>
 <div class="parties">
  <div class="box"><h3>مقدَّم إلى</h3><div class="nm">{E(cl["name"])}</div>
   <div>{CL}</div></div>
  <div class="box"><h3>مقدَّم من</h3><div class="nm">شركة جولدن فيل</div>
   <div>شركة ذات مسؤولية محدودة (شخص واحد)<br><b>الرقم الوطني الموحد:</b> {NUM("7055194109")}<br>{("<b>الرقم الضريبي:</b> " + NUM(D["vat_number"]) + "<br>") if D.get("vat_number") else ""}<b>الرياض،</b> المملكة العربية السعودية</div></div>
 </div>
 <table><thead><tr><th class="c" style="width:42px">#</th><th>البند والوصف</th><th class="c" style="width:70px">الوحدة</th><th class="c" style="width:58px">الكمية</th><th class="n" style="width:104px">سعر الوحدة</th><th class="n" style="width:110px">الإجمالي</th></tr></thead><tbody>{rows}</tbody></table>
 <div class="row"><div class="terms"><h3>الشروط والأحكام</h3><ol>{terms}</ol></div>
 <div class="totals"><div><span>{"المجموع" if disc else "الإجمالي قبل الضريبة"}</span><span class="num">{T(sub)}</span></div>
  {('<div><span>الخصم</span><span class="num">'+money(disc)+'</span></div><div><span>الإجمالي قبل الضريبة</span><span class="num">'+T(net)+'</span></div>') if disc else ""}
  <div><span>ضريبة القيمة المضافة ({D.get("vat_rate",.15)*100:g}%)</span><span class="num">{T(vat)}</span></div>
  <div class="g"><span>الإجمالي (ر.س)</span><span class="num">{T(grand)}</span></div></div></div>
 <div class="sign"><div class="l">شركة جولدن فيل — فهد سعد العجمي<small>التوقيع / الختم</small></div><div class="l">اعتماد العميل<small>الاسم / التوقيع / الختم</small></div></div>
 <div class="foot"><span class="lat">Golden Vale</span><span>الرياض · <span class="ltr num">0506221548</span> · <span class="ltr" style="font-family:Jost">fd-0@hotmail.com</span></span></div>
</div>'''
open(OUT, "w", encoding="utf-8").write(f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><title>عرض سعر — جولدن فيل</title><style>{CSS}</style></head><body>{body}</body></html>')
print("ok", "priced" if priced else "template")
