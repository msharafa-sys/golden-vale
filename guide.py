# -*- coding: utf-8 -*-
from common import *
import logos

def hdr(n, section, left=120):
    return f'<div class="hdr" style="left:{left}px"><span class="lat">Golden Vale · Brand Guidelines · {n:02d}</span><span>{section}</span></div>'
def ftr(n):
    return f'<div class="ftr"><span class="lat" style="font-size:14px">Brand Guidelines · v1.0 · 2026</span><span class="num" style="font-size:20px">{n:02d}</span></div>'

def cmyk(h):
    h = h.lstrip('#'); r,g,b = [int(h[i:i+2],16)/255 for i in (0,2,4)]; k = 1-max(r,g,b)
    return (0,0,0,100) if k >= 1 else tuple(round(100*x) for x in ((1-r-k)/(1-k),(1-g-k)/(1-k),(1-b-k)/(1-k),k))
def rgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))

pages = []
# ---- 1 غلاف ----
pages.append(f'''<div class="page dark"><div style="position:absolute;inset:0">{art("valley",1920,1080,"#B8A95E",op=.15)}</div>
 <div style="position:absolute;left:0;right:0;top:220px;display:flex;justify-content:center"><div style="width:720px">{logo("A","logo","reverse")}</div></div>
 <div style="position:absolute;left:0;right:0;top:760px;text-align:center"><div class="rule" style="margin:0 auto 32px"></div>
 <h2 style="font-weight:300;font-size:60px">دليل الهوية البصرية</h2><div class="lat" style="margin-top:22px;font-size:19px;color:var(--olive-l)">Brand Identity Guidelines · v1.0 · 2026</div></div></div>''')

# ---- 2 المبدأ ----
take = ["خط أحادي الوزن رفيع وهندسي","حروف كبيرة بتباعد واسع","لوحة زيتونية وفحمية وكريمية","هدوء بصري وفخامة غير متكلّفة"]
leave = ["علامة الماكرون فوق الحرف A","الشريط الكريمي للوصف الفرعي","شكل حرف A المفتوح بلا عارضة","أي حرف أو تركيب من شعار ĀIKA"]
li = lambda a,c: "".join(f'<div style="display:flex;gap:16px;align-items:baseline;padding:13px 0;border-top:1px solid rgba(140,127,62,.35);font-size:25px"><span style="color:{c};font-weight:700">{"+" if c=="var(--olive)" else "×"}</span>{x}</div>' for x in a)
pages.append(f'''<div class="page">{hdr(2,"فكرة الهوية")}
 <div style="position:absolute;right:120px;top:180px;width:1020px"><div class="lat olive" style="font-size:18px;margin-bottom:18px">Concept</div><h1>خطّ واحد، وأفق، وهدوء</h1><div class="rule" style="margin:30px 0"></div>
 <p>الهوية القديمة اعتمدت خطًا Serif عالي التباين ومثلثًا مفتّتًا، وهذا يوحي بالعقار والضيافة أكثر مما يوحي بوكالة إبداعية. الهوية الجديدة تنتقل إلى خط واحد منضبط، وعنصر وحيد مميّز هو <b style="font-weight:600">خط الأفق</b>: السطر الرفيع الذي يمثل حافة المسرح وحدّ الوادي معًا.</p>
 <p class="small deepc" style="margin-top:16px">المرجع الذي أُرسل (ĀIKA) هوية لاستوديو عمارة وتصميم داخلي؛ أُخذت منه المبادئ فقط، وأُضيف عنصر الأفق ليُعطي الحركة التي تحتاجها وكالة فعاليات.</p></div>
 <div style="position:absolute;left:120px;top:200px;width:560px;display:flex;flex-direction:column;gap:46px">
   <div><div class="deepc" style="font-size:20px;font-weight:600;margin-bottom:6px">ما أُخذ من المرجع (أسلوبًا)</div>{li(take,"var(--olive)")}</div>
   <div><div class="deepc" style="font-size:20px;font-weight:600;margin-bottom:6px">ما لا يُنسخ</div>{li(leave,"#A33")}</div></div>{ftr(2)}</div>''')

# ---- صفحات الاتجاهات ----
INFO = {
 "A": ("أ","الوادي المفتوح","Open Valley","الأساسي المقترح",
       "حرف V مفتوح القمة السفلية كأنه وادٍ، وفوقه خط أفقي منفصل هو الأفق وحدّ المسرح. في الشعار الكامل يعلو الخطُّ حرف O. حروف الاسم مرسومة هندسيًا بسُمك واحد، فلا تعتمد على أي خط.",
       "تحافظ على «الذهبي» عبر الزيتوني الذهبي، وهي الأقرب لمرجعك وتصلح للأيقونة المصغّرة.",50),
 "B": ("ب","استمرارية المثلث","Triangle Heritage","الأقل مخاطرة",
       "المثلث الحالي نفسه بعد تحويله إلى خطوط رفيعة وتقسيم داخلي، مع مثلث واحد مصمت بالزيتوني كنقطة ارتكاز. يحفظ رصيد العلامة القائمة ولا يقطع معها.",
       "مناسب إن كانت هناك مطبوعات أو لوحات منفذة بالهوية القديمة.",26),
 "C": ("ج","العربية أولًا","Arabic First","للجهات الحكومية والرسمية",
       "الاسم العربي «جولدن فيل» هو البطل، بخط IBM Plex Sans Arabic خفيف، والاسم اللاتيني بحروف هندسية متباعدة تحته. الأيقونة دائرة رفيعة بداخلها الوادي والأفق، تصلح كختم.",
       "الأنسب للمخاطبات الرسمية والعروض الحكومية، والأقل تميزًا لاتينيًا.",40)}

def clear_space(d):
    c, a = logos.MODES["color"]
    body, vb = logos.DIRS[d][0](c, a, True)
    x, y, w, h = vb; px = INFO[d][6]
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x-px*1.5} {y-px*1.5} {w+px*3} {h+px*3}" style="width:100%;height:auto;display:block">'
           f'<rect x="{x-px}" y="{y-px}" width="{w+2*px}" height="{h+2*px}" fill="none" stroke="#A33" stroke-width="1.6" stroke-dasharray="7 6"/>'
           f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#A33" stroke-width="1" opacity=".5"/>'
           f'{body}'
           f'<text x="{x-px/2}" y="{y+h/2}" fill="#A33" font-size="{px*.55}" text-anchor="middle" font-family="Jost">x</text>'
           f'<text x="{x+w+px/2}" y="{y+h/2}" fill="#A33" font-size="{px*.55}" text-anchor="middle" font-family="Jost">x</text>'
           f'<text x="{x+w/2}" y="{y-px/2+px*.2}" fill="#A33" font-size="{px*.55}" text-anchor="middle" font-family="Jost">x</text>'
           f'<text x="{x+w/2}" y="{y+h+px*.75}" fill="#A33" font-size="{px*.55}" text-anchor="middle" font-family="Jost">x</text></svg>')
    return svg

def tile(d, kind, mode, bg, label, w="100%", fg="var(--char)"):
    return (f'<div style="background:{bg};height:100%;position:relative;display:flex;align-items:center;justify-content:center;padding:34px">'
            f'<div style="width:{w}">{logo(d,kind,mode)}</div>'
            f'<span style="position:absolute;bottom:12px;right:16px;font-size:15px;color:{fg};opacity:.8">{label}</span></div>')

pg = 3
for d in "ABC":
    L, nm, en, badge, concept, why, px = INFO[d]
    # صفحة المفهوم
    pages.append(f'''<div class="page {"dark" if d=="B" and False else ""}">{hdr(pg,f"الاتجاه {L} — {nm}")}
 <div style="position:absolute;right:120px;top:180px;width:760px"><div class="lat olive" style="font-size:18px;margin-bottom:18px">Direction {d} · {en}</div>
   <div style="display:flex;gap:20px;align-items:center"><h1>{nm}</h1><span style="background:var(--olive);color:#fff;padding:5px 18px;font-size:19px;font-weight:500">{badge}</span></div>
   <div class="rule" style="margin:30px 0"></div><p style="font-size:26px">{concept}</p><p class="deepc" style="margin-top:20px;font-size:23px;font-weight:400">{why}</p>
   <div style="margin-top:44px;display:flex;gap:26px;align-items:center"><div style="width:170px;background:var(--cream);padding:24px">{logo(d,"icon","color")}</div><div class="small deepc" style="font-size:20px;line-height:1.8">الأيقونة المختصرة<br>للتطبيقات والأختام والصور الرمزية<br>والحد الأدنى للحجم 12 مم / 32 بكسل</div></div></div>
 <div style="position:absolute;left:120px;top:170px;width:880px;height:800px;background:var(--cream);display:flex;align-items:center;justify-content:center"><div style="width:640px">{logo(d,"logo","color")}</div></div>{ftr(pg)}</div>''')
    pg += 1
    # صفحة النسخ ومساحة الأمان
    pages.append(f'''<div class="page">{hdr(pg,f"الاتجاه {L} — النسخ ومساحة الأمان")}
 <div style="position:absolute;left:120px;right:120px;top:170px;height:760px;display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:14px">
   <div style="grid-row:span 2;background:#fff;padding:34px;display:flex;flex-direction:column;justify-content:center;gap:14px"><div style="font-size:19px;font-weight:600;color:var(--deep)">مساحة الأمان</div>{clear_space(d)}<div class="small deepc" style="font-size:18px;line-height:1.7">x = {"نصف ارتفاع حرف O" if d=="A" else "نصف ارتفاع حرف O" if d=="B" else "ثلث ارتفاع الكلمة العربية"}. لا يدخل أي عنصر داخل الإطار المنقّط.</div></div>
   {tile(d,"logo","color","var(--cream)","نسخة فاتحة (ملوّنة)","78%")}
   {tile(d,"logo","reverse","var(--char)","نسخة داكنة (معكوسة)","78%","var(--cream)")}
   {tile(d,"logo","mono","#fff","أحادي — أسود","78%")}
   <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;grid-column:span 1">
     <div style="background:var(--cream);display:flex;align-items:center;justify-content:center;padding:26px">{logo(d,"icon","color","100%")}</div>
     <div style="background:var(--char);display:flex;align-items:center;justify-content:center;padding:26px">{logo(d,"icon","reverse","100%")}</div>
     <div style="background:var(--olive);display:flex;align-items:center;justify-content:center;padding:26px">{logo(d,"icon","white","100%")}</div></div>
 </div>
 <div class="small deepc" style="position:absolute;left:120px;bottom:90px;font-size:18px">الأيقونة: ملوّنة · معكوسة · أبيض على الزيتوني. الشعار الأبيض الأحادي على خلفيات داكنة أو صور متوسطة التعتيم.</div>{ftr(pg)}</div>''')
    pg += 1

# ---- لوحة الألوان ----
cols = [("زيتوني ذهبي","Olive Gold",P["olive"],"لون العلامة والأفق · للعناصر الكبيرة والخطوط فقط على الفاتح (تباين 3.2:1)","#fff"),
        ("فحمي","Charcoal",P["char"],"النص والخلفيات الداكنة","var(--cream)"),
        ("كريمي","Cream",P["cream"],"الخلفية الأساسية للمطبوعات","var(--char)"),
        ("زيتوني فاتح","Olive Light",P["olive_light"],"الأفق على الخلفيات الداكنة (7.4:1 على الفحمي)","var(--char)"),
        ("زيتوني عميق","Deep Olive",P["deep"],"نصوص زيتونية صغيرة على الفاتح (7.8:1)","#fff"),
        ("حجر","Stone",P["stone"],"خلفيات ثانوية وخطوط","var(--char)")]
cc = "".join(f'<div style="background:{h};color:{fg};padding:30px 30px;height:300px;display:flex;flex-direction:column;justify-content:space-between{";border:1px solid rgba(0,0,0,.12)" if h==P["cream"] else ""}"><div><div style="font-size:30px;font-weight:600">{a}</div><div class="lat" style="font-size:13px;margin-top:6px">{b}</div></div><div style="font-size:17px;line-height:1.7;font-weight:400"><div class="ltr" style="font-family:Jost;font-size:19px;letter-spacing:.06em">HEX {h.upper()}<br>RGB {" · ".join(map(str,rgb(h)))}<br>CMYK {" · ".join(map(str,cmyk(h)))}</div><div style="margin-top:10px;font-weight:300">{n}</div></div></div>' for a,b,h,n,fg in cols)
pages.append(f'''<div class="page">{hdr(pg,"لوحة الألوان")}
 <div style="position:absolute;right:120px;top:160px"><h1 style="font-size:60px">لوحة الألوان</h1></div>
 <div style="position:absolute;left:120px;right:120px;top:320px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px">{cc}</div>
 <div class="small deepc" style="position:absolute;left:120px;right:120px;bottom:90px;font-size:18px;line-height:1.7">قيم CMYK محسوبة تحويلًا رياضيًا من RGB للإرشاد فقط، ولا تُعتمد للطباعة قبل مطابقتها بعينة طباعة ومرجع Pantone مع المطبعة. لون الورق في الملف التعريفي: <span class="ltr">#F6F2E9</span>.</div>{ftr(pg)}</div>''')
pg += 1

# ---- الخطوط ----
scale = [("Display","عرض","96 / 120","ExtraLight 200"),("H1","عنوان رئيسي","64 / 80","Medium 500"),("H2","عنوان فرعي","40 / 56","Medium 500"),("Body","نص","24 / 46","Light 300"),("Caption","تعليق","16 / 26","Regular 400")]
sr = "".join(f'<div style="display:flex;align-items:baseline;gap:30px;border-top:1px solid rgba(140,127,62,.4);padding:7px 0"><span class="lat" style="width:150px;font-size:14px">{a}</span><span style="flex:1;font-size:{[64,50,38,27,20][i]}px;font-weight:{[200,500,500,300,400][i]}">{b} — جولدن فيل</span><span class="ltr" style="font-family:Jost;font-size:17px;color:var(--deep)">{c} px · {d}</span></div>' for i,(a,b,c,d) in enumerate(scale))
pages.append(f'''<div class="page">{hdr(pg,"الخطوط")}
 <div style="position:absolute;right:120px;top:160px;width:1000px"><h1 style="font-size:56px;margin-bottom:20px">الخطوط</h1>
  <div style="display:flex;gap:30px;margin-bottom:22px">
   <div style="flex:1;background:var(--cream);padding:30px"><div class="lat" style="font-size:13px;color:var(--deep)">Latin</div><div style="font-family:Jost;font-weight:200;font-size:80px;line-height:1.1;margin:4px 0">Aa</div><div style="font-family:Jost;font-size:26px;font-weight:300">Jost — ExtraLight · Light · Regular</div><div class="small deepc" style="margin-top:8px;font-size:17px">خط مفتوح المصدر (OFL) من Google Fonts</div></div>
   <div style="flex:1;background:var(--char);color:var(--cream);padding:30px"><div class="lat" style="font-size:13px;color:var(--olive-l)">Arabic</div><div style="font-weight:200;font-size:80px;line-height:1.3;margin:0 0 4px">أب</div><div style="font-size:26px;font-weight:300">IBM Plex Sans Arabic — خفيف · عادي · متوسط</div><div class="small" style="margin-top:8px;font-size:17px;color:var(--olive-l)">خط مفتوح المصدر (OFL) من Google Fonts</div></div></div>
  {sr}</div>
 <div style="position:absolute;left:120px;top:160px;width:520px;font-size:23px;line-height:1.9;font-weight:300"><div style="font-weight:600;margin-bottom:8px">قواعد</div>
   • العناوين اللاتينية بحروف كبيرة بتباعد 0.3em.<br>• لا يُستخدم الوزن الأسود أو العريض في الشعارات.<br>• الأرقام بالخط اللاتيني الخفيف في العناوين الرقمية.<br>• النص العربي محاذى لليمين دائمًا مع تباعد أسطر 1.9.<br>• الحد الأدنى لنص الطباعة 9 نقاط.</div>{ftr(pg)}</div>''')
pg += 1

# ---- الاستخدام الصحيح والخاطئ ----
def bad(label, inner, bg="var(--cream)"):
    return f'<div style="height:100%;background:{bg};position:relative;display:flex;align-items:center;justify-content:center;padding:30px;overflow:hidden">{inner}<span style="position:absolute;bottom:10px;right:14px;font-size:15px;color:#A33;font-weight:600">× {label}</span></div>'
def good(label, inner, bg):
    return f'<div style="height:100%;background:{bg};position:relative;display:flex;align-items:center;justify-content:center;padding:30px">{inner}<span style="position:absolute;bottom:10px;right:14px;font-size:15px;color:#2d7a3d;font-weight:600">✓ {label}</span></div>'
red = logos.get("A","logo","color")[0].replace(P["olive"],"#D33")
shadow = logo("A","logo","color",extra="filter:drop-shadow(4px 6px 3px rgba(0,0,0,.5));")
g1 = [good("على الكريمي", f'<div style="width:78%">{logo("A")}</div>', "var(--cream)"),
      good("على الفحمي", f'<div style="width:78%">{logo("A","logo","reverse")}</div>', "var(--char)"),
      good("على الزيتوني (أبيض)", f'<div style="width:78%">{logo("A","logo","white")}</div>', "var(--olive)"),
      good("على صورة بتعتيم", f'<div style="width:78%">{logo("A","logo","white")}</div>', "linear-gradient(135deg,#3a3a37,#161513)")]
b1 = [bad("تمديد النسب", f'<div style="width:90%;transform:scaleX(1.35)">{logo("A")}</div>'),
      bad("تغيير الألوان", f'<div style="width:78%">{sv(red)}</div>'),
      bad("تدوير", f'<div style="width:70%;transform:rotate(-14deg)">{logo("A")}</div>'),
      bad("ظلال وتأثيرات", f'<div style="width:78%">{shadow}</div>'),
      bad("تباين ضعيف", f'<div style="width:78%">{logo("A","logo","color")}</div>', "var(--olive)"),
      bad("تحريك الأفق", f'<div style="width:78%">{sv(logos.get("A","logo","color")[0].replace("M-22 -30","M-22 20").replace("H122 -30","H122 20") if False else logos.get("A","logo","color")[0].replace("-30 H","10 H",1))}</div>'),
      bad("خلفية مزدحمة", f'<div style="width:78%">{logo("A","logo","color")}</div><div style="position:absolute;inset:0;opacity:.9;mix-blend-mode:multiply">{art("grid",600,400,"#1B1A18",op=.9)}</div>'),
      bad("حذف الاسم/إضافة إطار", f'<div style="width:50%;border:4px solid var(--char);padding:22px;border-radius:50%">{logo("A","icon","color")}</div>')]
pages.append(f'''<div class="page">{hdr(pg,"الاستخدام الصحيح والخاطئ (الاتجاه أ)")}
 <div style="position:absolute;left:120px;right:120px;top:140px;height:300px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px">{"".join(g1)}</div>
 <div style="position:absolute;left:120px;right:120px;top:460px;height:490px;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;gap:12px">{"".join(b1)}</div>{ftr(pg)}</div>''')
pg += 1

# ---- التطبيقات ----
def card():
    front = f'<div style="width:420px;height:240px;background:var(--char);display:flex;align-items:center;justify-content:center;box-shadow:0 18px 30px rgba(0,0,0,.35)"><div style="width:240px">{logo("A","logo","reverse",tagline=False)}</div></div>'
    back = f'''<div style="width:420px;height:240px;background:var(--cream);padding:28px 30px;box-shadow:0 18px 30px rgba(0,0,0,.25);position:relative"><div style="width:44px;position:absolute;left:28px;top:26px">{logo("A","icon","color")}</div>
     <div style="margin-top:96px;font-weight:600;font-size:21px">فهد سعد العجمي</div><div style="font-size:14px;color:var(--deep)">المؤسس ورئيس مجلس الإدارة</div>
     <div class="ltr" style="font-family:Jost;font-size:13px;margin-top:12px;letter-spacing:.06em">0506221548 · fd-0@hotmail.com</div><div style="font-size:12px;color:var(--deep);margin-top:2px">الرياض، المملكة العربية السعودية</div></div>'''
    return front, back
cf, cb = card()
letter = f'''<div style="width:340px;height:480px;background:#fff;box-shadow:0 18px 30px rgba(0,0,0,.28);padding:32px;position:relative"><div style="width:130px">{logo("A","logo","color",tagline=False)}</div>
  <div style="margin-top:60px">{"".join('<div style="height:7px;background:#ddd;margin:13px 0;width:%d%%"></div>'%w for w in (96,88,92,70,94,85,60))}</div>
  <div style="position:absolute;left:32px;right:32px;bottom:26px;border-top:1px solid var(--olive);padding-top:8px;font-size:11px;color:var(--deep);display:flex;justify-content:space-between"><span>الرياض · المملكة العربية السعودية</span><span class="ltr" style="font-family:Jost">fd-0@hotmail.com</span></div></div>'''
envelope = f'''<div style="width:520px;height:250px;background:var(--cream);box-shadow:0 14px 26px rgba(0,0,0,.28);position:relative"><div style="width:50px;position:absolute;right:26px;top:22px">{logo("A","icon","color")}</div>
  <div style="position:absolute;left:34px;bottom:30px;font-size:13px;color:var(--deep);line-height:1.9">اسم المستلم<br>العنوان — الرياض</div><div style="position:absolute;left:0;right:0;top:0;height:95px;border-bottom:1px solid rgba(140,127,62,.5);clip-path:polygon(0 0,100% 0,50% 100%)"></div></div>'''
folder = f'''<div style="width:330px;height:440px;background:var(--char);box-shadow:0 18px 30px rgba(0,0,0,.4);position:relative;display:flex;align-items:center;justify-content:center"><div style="position:absolute;inset:0;opacity:.8">{art("valley",330,440,"#B8A95E",op=.3)}</div><div style="width:200px;position:relative">{logo("A","logo","reverse")}</div></div>'''
fascia = f'''<div style="width:760px;height:260px;background:linear-gradient(160deg,#8d8472,#6f6858);box-shadow:0 18px 34px rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center;position:relative"><div style="width:60%;padding:28px;background:var(--char);box-shadow:0 0 60px 8px rgba(184,169,94,.45)">{logo("A","logo","reverse")}</div></div>'''
polo = f'''<svg viewBox="0 0 300 300" style="width:330px"><path d="M95 20 L55 38 L12 100 L52 122 L72 96 L72 280 H228 V96 L248 122 L288 100 L245 38 L205 20 Q150 62 95 20Z" fill="#1B1A18"/><path d="M120 22 L150 70 L180 22" fill="none" stroke="#2d2c29" stroke-width="3"/><g transform="translate(176 104) scale(.2)">{logos.get("A","icon","reverse")[0].split(">",1)[1].rsplit("</svg>",1)[0]}</g></svg>'''
banner = f'''<div style="width:240px;height:480px;background:var(--char);box-shadow:0 18px 30px rgba(0,0,0,.4);position:relative;overflow:hidden"><div style="position:absolute;inset:0">{art("beams",240,480,"#B8A95E",op=.4)}</div><div style="position:absolute;left:30px;right:30px;top:40px">{logo("A","logo","reverse")}</div><div style="position:absolute;left:24px;right:24px;bottom:70px;text-align:center;color:var(--cream);font-size:26px;font-weight:300">[اسم الفعالية]</div></div>'''
def lab(t): return f'<div style="position:absolute;font-size:16px;background:var(--olive);color:#fff;padding:2px 12px;font-weight:500">{t}</div>'
wall = "linear-gradient(180deg,#d9d2c1,#cfc6b2)"
pages.append(f'''<div class="page" style="background:{wall}">{hdr(pg,"التطبيقات (1/2) — تصوّر")}
 <div style="position:absolute;left:120px;top:170px;display:flex;flex-direction:column;gap:30px">{cf}{cb}</div>
 <div style="position:absolute;left:640px;top:170px">{letter}</div>
 <div style="position:absolute;right:120px;top:170px;display:flex;flex-direction:column;gap:30px;align-items:flex-end">{envelope}{folder}</div>
 <div class="tag" style="left:120px;bottom:100px">تصوّر — بطاقة العمل</div><div class="tag" style="left:640px;bottom:100px">تصوّر — الورق الرسمي</div><div class="tag" style="right:120px;bottom:100px">تصوّر — المظروف والمجلد</div>{ftr(pg).replace("color:var(--deep)","")}</div>''')
pg += 1
pages.append(f'''<div class="page" style="background:{wall}">{hdr(pg,"التطبيقات (2/2) — تصوّر")}
 <div style="position:absolute;left:120px;top:180px">{fascia}</div>
 <div style="position:absolute;left:120px;top:520px;display:flex;gap:70px;align-items:flex-start">{polo}<div style="width:200px;height:290px;background:var(--cream);box-shadow:0 14px 24px rgba(0,0,0,.3);margin-top:20px;position:relative;padding:20px"><div style="width:120px">{logo("A","logo","color",tagline=False)}</div><div style="margin-top:90px;font-size:18px;font-weight:600">[الاسم]</div><div style="font-size:12px;color:var(--deep)">منظّم · فريق العمليات</div></div></div>
 <div style="position:absolute;right:300px;top:180px">{banner}</div>
 <div style="position:absolute;right:120px;top:210px;width:140px;writing-mode:vertical-rl"></div>
 <div class="tag" style="left:120px;top:150px;display:none"></div>
 <div class="tag" style="left:120px;bottom:100px">تصوّر — لوحة واجهة مضيئة</div><div class="tag" style="left:560px;bottom:100px">تصوّر — الزي والبطاقة</div><div class="tag" style="right:300px;bottom:100px">تصوّر — بنر فعاليات</div>{ftr(pg)}</div>''')
pg += 1

# ---- الخطوات التالية ----
nx = [("اختيار الاتجاه","أ أو ب أو ج، واعتماده كتابيًا."),("فحص التسجيل","التحقق من توفر «Golden Vale / جولدن فيل» والشعار لدى الهيئة السعودية للملكية الفكرية قبل أي طباعة."),("الملفات النهائية","تسليم SVG وPDF وPNG بعد الاعتماد، وفحص القراءة على الأحجام الصغيرة."),("عينات الطباعة","مطابقة CMYK/Pantone مع المطبعة قبل الإنتاج الكامل."),("استبدال المحتوى المؤقت","إضافة السجل التجاري وصور المشاريع وشعارات العملاء الموثّقة.")]
nr = "".join(f'<div style="display:flex;gap:34px;align-items:baseline;border-top:1px solid rgba(140,127,62,.4);padding:22px 0"><span class="num olive" style="font-size:44px;width:80px">{i+1:02d}</span><div><h3 style="font-size:32px">{a}</h3><p class="small" style="font-size:22px;line-height:1.7">{b}</p></div></div>' for i,(a,b) in enumerate(nx))
pages.append(f'''<div class="page cream">{hdr(pg,"الخطوات التالية")}<div style="position:absolute;right:120px;top:170px;width:1250px"><h1 style="font-size:60px;margin-bottom:24px">الخطوات التالية</h1>{nr}</div>{ftr(pg)}</div>''')

open("build/guide.html","w",encoding="utf-8").write(html("جولدن فيل — دليل الهوية البصرية", pages))
print(len(pages), "pages")
