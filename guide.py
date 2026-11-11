# -*- coding: utf-8 -*-
from common import *
import logos

def hdr(n, section, left=120):
    return f'<div class="hdr" style="left:{left}px"><span class="lat">Golden Vale · Brand Guidelines · {n:02d}</span><span>{section}</span></div>'
def ftr(n):
    return f'<div class="ftr"><span class="lat" style="font-size:14px">Brand Guidelines · v2.0 · 2026</span><span class="num" style="font-size:20px">{n:02d}</span></div>'

def cmyk(h):
    h = h.lstrip('#'); r,g,b = [int(h[i:i+2],16)/255 for i in (0,2,4)]; k = 1-max(r,g,b)
    return (0,0,0,100) if k >= 1 else tuple(round(100*x) for x in ((1-r-k)/(1-k),(1-g-k)/(1-k),(1-b-k)/(1-k),k))
def rgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))


def lum(h):
    r,g,b=[c/255 for c in rgb(h)]
    f=lambda c: c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
def contrast(a,b):
    la,lb=sorted((lum(a),lum(b)),reverse=True); return (la+0.05)/(lb+0.05)

INK,CREAM,CLIGHT,STONE,GOLD,NAVY2,GLIGHT="#14213D","#F7F4EC","#FBF9F3","#D9D3C3","#7A5F1E","#1F3158","#D4A94E"

def logo_c(kind, text, tile, width="100%"):
    body, vb = logos.DIRS["A"][0 if kind=="logo" else 1](text, tile, False)
    return sv(logos._wrap(body, vb, text, tile, "Golden Vale"), width)

pages = []
H = lambda n, s: hdr(n, s)
# 1 غلاف
pages.append(f"""<div class="page dark">
 <div style="position:absolute;left:0;right:0;top:300px;display:flex;justify-content:center"><div style="width:760px">{logo("A","logo","reverse")}</div></div>
 <div style="position:absolute;left:0;right:0;top:640px;text-align:center"><h2 style="font-weight:600;font-size:68px">دليل الهوية البصرية</h2>
 <div class="lat" style="margin-top:26px;font-size:20px;color:var(--olive-l)">Brand Identity Guidelines · v2.0 · 2026</div></div></div>""")

# 2 الاستراتيجية
aud=[("المطورون العقاريون","حضور ميداني يليق بمشروع قيد التسويق: لوحات موقع، تغليف سياجات، ومكعبات إعلانية."),
     ("الجهات الحكومية والمؤسسات","التزام حرفي بدليل الهوية، وتوثيق لكل خطوة، وسلامة في الموقع لا تُختصر."),
     ("الوجهات الترفيهية والتجزئة","مواسم مواعيدها قاسية، وتجربة تُصوَّر وتُنتشر: بوابة، مجسم، تفعيل، ومنطقة تصوير.")]
ar="".join(f'<div style="padding:26px 0;border-top:1px solid rgba(122,95,30,.4)"><h3 style="font-size:32px">{t}</h3><p style="font-size:23px;line-height:1.8;margin-top:6px">{d}</p></div>' for t,d in aud)
pages.append(f"""<div class="page">{H(2,"الاستراتيجية")}
 <div style="position:absolute;right:120px;top:170px;width:1000px"><div class="lat olive" style="font-size:18px;margin-bottom:16px">Brand Strategy</div>
  <h1 style="font-size:64px">ما تقوله العلامة قبل أن تُصمَّم</h1>
  <p style="margin-top:28px;font-size:28px">للمطوّرين العقاريين والجهات الحكومية والوجهات الترفيهية وقطاع التجزئة في المملكة، Golden Vale هي الجهة التي تُسلِّم الحضور كاملاً: فكرةً وتصميماً وإنتاجاً وتشغيلاً، تحت إدارة واحدة.</p>
  <div style="margin-top:44px;background:var(--char);color:var(--cream);padding:34px 40px"><div class="lat" style="font-size:15px;color:var(--olive-l)">Promise</div><div style="font-size:44px;font-weight:600;font-family:Messiri;margin-top:8px">موعد معلن، وسعر مكتوب، ومسؤول واحد.</div></div></div>
 <div style="position:absolute;left:120px;top:200px;width:640px">{ar}</div>{ftr(2)}</div>""")

# 3 الشخصية والركائز
pers=[("رصين","نتحدث بما نعمل، ولا نرفع الصوت. الوقار من الانضباط لا من الزخرفة."),("دقيق","مقاسات وخامات ومواعيد بالأرقام، لا بالوعود العامة."),("دافئ","قريبون من فريق العميل، بلا حواجز ولا مراسم."),("مباشر","جملة واحدة واضحة أفضل من ثلاثة سطور غامضة.")]
pil=[("إدارة واحدة","لا نُقسّم المشروع على ثلاثة مورّدين. جهة واحدة تحمل الفكرة والجودة والموعد.","نقطة اتصال واحدة من العرض حتى التقرير الختامي."),
     ("موعد نلتزم به","الجدول يُعتمد قبل بدء الإنتاج، ويُتابَع بمراحل موثّقة.","تصميم، تصنيع، فحص، تركيب، تشغيل: معالم معلنة."),
     ("تفاصيل تُلمس","الجودة تُقاس من مسافة قريبة: تشطيب، لحام، وخطوط نظيفة على الحافة.","فحص في الورشة قبل النقل إلى الموقع.")]
pe="".join(f'<div style="background:var(--cream);padding:26px 28px"><h3 style="font-size:34px;color:var(--char)">{t}</h3><p style="font-size:21px;line-height:1.75;margin-top:6px">{d}</p></div>' for t,d in pers)
pp="".join(f'<div style="border-top:3px solid var(--olive);padding:22px 0"><h3 style="font-size:36px">{t}</h3><p style="font-size:22px;line-height:1.8;margin-top:8px">{d}</p><p class="small deepc" style="margin-top:10px;font-size:19px">{p}</p></div>' for t,d,p in pil)
pages.append(f"""<div class="page">{H(3,"الشخصية وركائز الرسائل")}
 <div style="position:absolute;right:120px;top:170px"><div class="lat olive" style="font-size:18px;margin-bottom:12px">Personality</div><h1 style="font-size:56px">أربع صفات</h1></div>
 <div style="position:absolute;left:120px;right:120px;top:330px;display:grid;grid-template-columns:repeat(4,1fr);gap:16px">{pe}</div>
 <div style="position:absolute;right:120px;top:640px"><div class="lat olive" style="font-size:18px">Message Pillars</div></div>
 <div style="position:absolute;left:120px;right:120px;top:700px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px">{pp}</div>{ftr(3)}</div>""")

# 4 الشعار
surf=[("الشعار الأساسي: عاجي على كحلي",INK,logo_c("logo",CREAM,GLIGHT),CREAM),
      ("على الأسطح الفاتحة: كحلي",CLIGHT,logo_c("logo",INK,INK),INK),
      ("لمسة مميزة: ذهبي فاتح على كحلي عميق",NAVY2,logo_c("logo",GLIGHT,GLIGHT),GLIGHT)]
st="".join(f'<div style="background:{bg};height:360px;display:flex;flex-direction:column;justify-content:space-between;padding:34px;{"border:1px solid rgba(20,33,61,.15)" if bg==CLIGHT else ""}"><div style="flex:1;display:flex;align-items:center;justify-content:center"><div style="width:78%">{lg}</div></div><div style="font-size:18px;color:{fg};opacity:.85">{lb}</div></div>' for lb,bg,lg,fg in surf)
pages.append(f"""<div class="page">{H(4,"الشعار")}
 <div style="position:absolute;right:120px;top:160px;width:1100px"><div class="lat olive" style="font-size:18px;margin-bottom:12px">Logo System</div><h1 style="font-size:60px">الشعار تركيبة واحدة</h1>
 <p style="margin-top:20px;font-size:26px">مونوغرام GV داخل مربع بزوايا مدوّرة، يليه الاسم GOLDEN VALE بخط Big Shoulders Display. لا يُعاد رسمه ولا تُضاف إليه كلمات أخرى.</p></div>
 <div style="position:absolute;left:120px;right:120px;top:480px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px">{st}</div>{ftr(4)}</div>""")

# 5 مساحة الحماية
X=62
body,vb=logos.DIRS["A"][0](INK,INK,False); x,y,w,h=vb
cs=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x-X*1.6} {y-X*1.6} {w+X*3.2} {h+X*3.2}" style="width:100%;height:auto;display:block">'
    f'<rect x="{x-X}" y="{y-X}" width="{w+2*X}" height="{h+2*X}" fill="none" stroke="#B33" stroke-width="2" stroke-dasharray="8 7"/>'
    f'{body}'+"".join(f'<text x="{tx}" y="{ty}" fill="#B33" font-size="44" text-anchor="middle" font-family="BSD">X</text>' for tx,ty in ((x-X/2,y+h/2+15),(x+w+X/2,y+h/2+15),(x+w/2,y-X/2+15),(x+w/2,y+h+X/2+15)))+'</svg>')
mins=[("72 px","الحد الأدنى الرقمي","72px"),("52 px","الحد الأدنى المطبوع","52px")]
mn="".join(f'<div style="background:var(--cream);padding:28px;display:flex;flex-direction:column;align-items:flex-start;gap:14px"><div style="width:{w}">{logo_c("logo",INK,INK)}</div><div class="lat" style="font-size:16px">{a}</div><div style="font-size:19px">{b}</div></div>' for a,b,w in mins)
wrong=[("لا يُدوَّر","transform:rotate(-12deg)"),("لا يُمَدّ أفقياً","transform:scaleX(1.4)"),("لا يُضغط رأسياً","transform:scaleY(.6)")]
wr="".join(f'<div style="background:var(--cream);height:170px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden"><div style="width:62%;{t}">{logo_c("logo",INK,INK)}</div><div style="position:absolute;bottom:8px;right:12px;font-size:16px;color:#B33">× {l}</div></div>' for l,t in wrong)
pages.append(f"""<div class="page">{H(5,"مساحة الحماية والحد الأدنى")}
 <div style="position:absolute;right:120px;top:160px;width:900px"><div class="lat olive" style="font-size:18px;margin-bottom:12px">Clear Space &amp; Sizing</div><h1 style="font-size:56px">مساحة الحماية</h1>
 <p style="margin-top:18px;font-size:25px">وحدة القياس X تساوي ارتفاع حرف G في المونوغرام. تُترك هذه المساحة فارغة من كل جهة، لا يدخلها نص ولا شعار شريك ولا حافة قالب.</p>
 <p class="deepc" style="margin-top:14px;font-size:22px">أقل من الحد الأدنى تضيع تفاصيل الاسم؛ عند الحاجة لمساحة أصغر يُستخدم مونوغرام GV وحده.</p></div>
 <div style="position:absolute;left:120px;top:180px;width:700px;background:#fff;padding:36px">{cs}</div>
 <div style="position:absolute;left:120px;top:660px;width:700px;display:grid;grid-template-columns:1fr 1fr;gap:14px">{mn}</div>
 <div style="position:absolute;right:120px;top:560px;width:900px"><div class="small deepc" style="font-size:20px;font-weight:600;margin-bottom:10px">ما يكسر العلامة</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">{wr}</div>
 <p class="small" style="margin-top:16px;font-size:19px">ولا يوضع الشعار فوق صورة مزدحمة دون طبقة تعتيم كافية.</p></div>{ftr(5)}</div>""")

# 6 الألوان
pal=[("الكحلي الملكي","Ink",INK,"الخلفيات الداكنة والنصوص",CREAM),("العاجي","Ivory",CREAM,"الخلفية الأساسية",INK),("العاجي الفاتح","Ivory Light",CLIGHT,"الأسطح والبطاقات",INK),
     ("الرملي","Sand",STONE,"الحدود والفواصل",INK),("الذهبي الداكن","Dark Gold",GOLD,"الإجراءات والتمييز",CREAM),("الكحلي العميق","Deep Navy",NAVY2,"اللمسات والتذييلات",CREAM),("الذهبي الفاتح","Light Gold",GLIGHT,"النصوص الذهبية على الكحلي",INK)]
pc="".join(f'<div style="background:{h};color:{fg};padding:26px;height:290px;display:flex;flex-direction:column;justify-content:space-between{";border:1px solid rgba(20,33,61,.18)" if h in (CREAM,CLIGHT) else ""}"><div><div class="lat" style="font-size:14px;opacity:.85">{en}</div><div style="font-size:31px;font-weight:600;font-family:Messiri;margin-top:6px">{n}</div><div style="font-size:17px;margin-top:6px;opacity:.9">{u}</div></div><div class="ltr" style="font-family:BSD;font-size:18px;line-height:1.55;letter-spacing:.05em">{h}<br>RGB {" · ".join(map(str,rgb(h)))}<br>CMYK {" · ".join(map(str,cmyk(h)))}</div></div>' for n,en,h,u,fg in pal)
pages.append(f"""<div class="page">{H(6,"الألوان")}
 <div style="position:absolute;right:120px;top:150px"><div class="lat olive" style="font-size:18px;margin-bottom:10px">Color System</div><h1 style="font-size:56px">سبعة ألوان، بلا إضافات</h1></div>
 <div style="position:absolute;left:120px;right:120px;top:300px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px">{pc}<div style="background:var(--cream);padding:26px;height:290px;display:flex;flex-direction:column;justify-content:center"><div style="font-size:23px;line-height:1.9"><b>توزيع الاستخدام</b><br>60% عاجي أو كحلي<br>25% رملي وعاجي فاتح<br>10% كحلي عميق<br>5% ذهبي داكن</div></div></div>
 <div class="small deepc" style="position:absolute;left:120px;right:120px;bottom:80px;font-size:18px;line-height:1.7">نسبة الذهبي لا تتجاوز 10% من أي مادة. قيم CMYK محسوبة رياضياً من RGB للإرشاد فقط، وتُعتمد بالبروفة من المطبعة.</div>{ftr(6)}</div>""")

# 7 التباين
pairs=[("عاجي على كحلي",CREAM,INK,"الحالة الأساسية للنص"),("كحلي على عاجي فاتح",INK,CLIGHT,"البطاقات والأسطح"),("ذهبي فاتح على كحلي",GLIGHT,INK,"النص الذهبي المعتمد"),
       ("رملي على كحلي",STONE,INK,"نص ثانوي ومصغّر"),("كحلي عميق على عاجي",NAVY2,CREAM,"عناوين وأشرطة"),("ذهبي داكن على عاجي",GOLD,CREAM,"عنوان كبير ورسوم فقط")]
def verdict(r): return "AAA" if r>=7 else ("AA" if r>=4.5 else ("كبير فقط" if r>=3 else "مرفوض"))
cp="".join(f'<div style="background:{bg};color:{fg};padding:30px;height:220px;display:flex;flex-direction:column;justify-content:space-between{";border:1px solid rgba(20,33,61,.18)" if bg in (CREAM,CLIGHT) else ""}"><div style="font-size:44px;font-family:Messiri;font-weight:600">حضور</div><div><div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-size:20px">{l}</span><span class="ltr" style="font-family:BSD;font-size:38px;font-weight:700">{contrast(fg,bg):.1f}:1</span></div><div style="font-size:16px;opacity:.85">{u} · {verdict(contrast(fg,bg))}</div></div></div>' for l,fg,bg,u in pairs)
pages.append(f"""<div class="page">{H(7,"التباين وقابلية القراءة")}
 <div style="position:absolute;right:120px;top:150px;width:1100px"><div class="lat olive" style="font-size:18px;margin-bottom:10px">Contrast</div><h1 style="font-size:56px">التوافق وقابلية القراءة</h1>
 <p style="margin-top:16px;font-size:24px">المعيار WCAG: النص الأساسي يحتاج 4.5:1 على الأقل، والعنوان الكبير 3:1. الذهبي الداكن على العاجي للعناوين الكبيرة والرسوم فقط، لا للنصوص الصغيرة.</p></div>
 <div style="position:absolute;left:120px;right:120px;top:400px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px">{cp}</div>
 <div class="small deepc" style="position:absolute;left:120px;right:120px;bottom:80px;font-size:18px">النسب محسوبة من قيم HEX المعتمدة بمعادلة WCAG 2.x.</div>{ftr(7)}</div>""")

# 8 الخطوط
rows=[("العرض الرئيسي","Big Shoulders Display 700","64 px","BSD",700,64,"GOLDEN VALE"),("عنوان قسم","El Messiri 600","40 px","Messiri",600,40,"نصنع حضوراً يُرى ويُتذكّر"),("عنوان فرعي","El Messiri 500","24 px","Messiri",500,28,"تصميم وإنتاج وتركيب وتشغيل"),
      ("نص أساسي","IBM Plex Sans Arabic 400","18 px","Plex",400,22,"جدول معتمد من الفكرة حتى التسليم، بنقطة تواصل واحدة."),("تسمية علوية","Big Shoulders Display 500","12 px","BSD",500,16,"ADVERTISING &amp; EVENTS · RIYADH")]
tr="".join(f'<div style="display:grid;grid-template-columns:240px 1fr 200px;gap:26px;align-items:baseline;border-top:1px solid rgba(122,95,30,.4);padding:16px 0"><div><div style="font-size:21px;font-weight:600">{n}</div><div class="small deepc" style="font-size:16px">{f}</div></div><div style="font-family:{fam};font-weight:{wt};font-size:{px}px;line-height:1.3;{"letter-spacing:.06em" if fam=="BSD" else ""}">{s}</div><div class="num" style="font-size:20px;text-align:left" dir="ltr">{sz}</div></div>' for n,f,sz,fam,wt,px,s in rows)
pages.append(f"""<div class="page">{H(8,"الخطوط")}
 <div style="position:absolute;right:120px;top:150px;width:1200px"><div class="lat olive" style="font-size:18px;margin-bottom:10px">Typography</div><h1 style="font-size:56px">ثلاثة خطوط</h1>
 <p style="margin-top:14px;font-size:24px">IBM Plex Sans Arabic لنصوص العربية، وEl Messiri للعناوين العربية، وBig Shoulders Display للاتينية والمونوغرام. لا يُستخدم أي خط آخر في أي مادة.</p></div>
 <div style="position:absolute;left:120px;right:120px;top:400px">{tr}</div>{ftr(8)}</div>""")

# 9 اللغة الشكلية
sp="".join(f'<div style="display:flex;align-items:center;gap:20px;padding:6px 0"><span class="num" style="width:110px;font-size:20px" dir="ltr">space-{i+1} · {v}px</span><span style="display:block;height:18px;width:{v*3}px;background:var(--olive)"></span></div>' for i,v in enumerate((8,16,24,32,48,64,96)))
pages.append(f"""<div class="page">{H(9,"اللغة الشكلية")}
 <div style="position:absolute;right:120px;top:150px;width:1000px"><div class="lat olive" style="font-size:18px;margin-bottom:10px">Graphic Language</div><h1 style="font-size:56px">خطوط، لا زخرفة</h1>
 <p style="margin-top:14px;font-size:24px">كل ما يميّز الصفحة يُبنى من ثلاثة عناصر فقط: خط أفقي رفيع، وشبكة من ثمانية، ورقم متباعد. ما عداها زخرفة تُحذف.</p></div>
 <div style="position:absolute;right:120px;top:420px;width:1000px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:30px">
  <div><div style="height:1px;background:var(--char);margin-bottom:18px"></div><h3 style="font-size:30px">الخط الفاصل 1px</h3><p style="font-size:21px;line-height:1.8;margin-top:6px">الفصل بين العناصر بخط، لا بظل ولا بمربع ملوّن. الخط الذهبي مرة واحدة للتأكيد في الصفحة.</p></div>
  <div><div class="num olive" style="font-size:54px;line-height:1;margin-bottom:12px;letter-spacing:.2em" dir="ltr">01</div><h3 style="font-size:30px">الترقيم المتباعد</h3><p style="font-size:21px;line-height:1.8;margin-top:6px">أرقام لاتينية بخط Big Shoulders Display وتباعد 0.2em، تُستخدم للفهرس ومراحل العمل.</p></div>
  <div><div style="width:64px;height:64px;background:var(--char);margin-bottom:18px"></div><h3 style="font-size:30px">شبكة من ثمانية</h3><p style="font-size:21px;line-height:1.8;margin-top:6px">كل هامش وفراغ داخلي من مضاعفات 8px. الزوايا حادة في القوالب، والمدوّر خاص بمربع الشعار.</p></div></div>
 <div style="position:absolute;left:120px;top:170px;width:560px;background:var(--cream);padding:30px"><div style="font-size:20px;font-weight:600;margin-bottom:12px">سلّم المسافات</div>{sp}</div>{ftr(9)}</div>""")

# 10 النبرة
do=[("نُسلّم الجناح في 14 يوم عمل، بجدول معتمد قبل بدء الإنتاج.","أسرع تنفيذ في السوق وبأفضل الأسعار!"),("نطاق العمل مكتوب، والسعر مفصّل بنداً بنداً قبل البدء.","أسعار تنافسية لا تُقاوَم."),("الخامة محددة في العرض: ألمنيوم بسماكة 3 مم وتشطيب مطفي.","خامات عالمية فاخرة تليق بمكانتكم.")]
dr="".join(f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;border-top:1px solid rgba(122,95,30,.4);padding:16px 0;font-size:23px;line-height:1.7"><div><span style="color:#2d7a3d;font-weight:700">+ </span>{a}</div><div style="color:#B33"><span style="font-weight:700">× </span><s>{b}</s></div></div>' for a,b in do)
voc="".join(f'<span style="background:var(--cream);padding:6px 18px;font-size:21px">{v}</span>' for v in ("التسليم","النطاق","الاعتماد","التشطيب","التشغيل","التوثيق","الورشة","الجدول"))
ban="".join(f'<span style="border:1px solid #B33;color:#B33;padding:6px 18px;font-size:21px">{v}</span>' for v in ("الأفضل","الأول","الأسطوري","ثورة","لا مثيل له","أرخص","خيالي"))
pages.append(f"""<div class="page">{H(10,"نبرة الصوت")}
 <div style="position:absolute;right:120px;top:150px;width:1100px"><div class="lat olive" style="font-size:18px;margin-bottom:10px">Voice &amp; Tone</div><h1 style="font-size:56px">واثقة، مباشرة، بلا مبالغة</h1>
 <p style="margin-top:14px;font-size:24px">نكتب كما يتحدث مدير مشروع خبير: يشرح، ثم يلتزم، ثم يسكت. النبرة نفسها في العرض والرسالة واللوحة والموقع. نقول ما نفعله، والأرقام قبل الصفات، وجملة واحدة تكفي.</p></div>
 <div style="position:absolute;left:120px;right:120px;top:400px"><div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;font-size:19px;font-weight:600;padding-bottom:8px"><div>نكتب هكذا</div><div>لا نكتب هكذا</div></div>{dr}
 <div style="margin-top:34px;display:grid;grid-template-columns:1fr 1fr;gap:30px"><div><div style="font-size:20px;font-weight:600;margin-bottom:10px">مفردات العلامة</div><div style="display:flex;flex-wrap:wrap;gap:10px">{voc}</div></div><div><div style="font-size:20px;font-weight:600;margin-bottom:10px">كلمات خارج القاموس</div><div style="display:flex;flex-wrap:wrap;gap:10px">{ban}</div></div></div></div>{ftr(10)}</div>""")

# 11 التصوير
ph=[("الضوء دافئ وطبيعي","إضاءة مواقع حقيقية: ليل الرياض، دافئ المصابيح، بلا ألوان مشبعة مضافة."),("البيئة سعودية وخليجية","مواقع حقيقية بمعمارها وضوئها وناسها، دون نماذج أجنبية أو خلفيات مستوردة."),("التفصيل يُصوَّر قريباً","حافة الألمنيوم، لحام نظيف، خط مطبوع على الخامة: الصورة القريبة دليل الجودة."),("الإنسان جزء من المشهد","زائر يمر، يد تمسّ، فريق يركّب. الحضور يقاس بمن يعيشه.")]
pt="".join(f'<div style="background:var(--cream);padding:28px"><h3 style="font-size:32px">{t}</h3><p style="font-size:21px;line-height:1.8;margin-top:8px">{d}</p></div>' for t,d in ph)
out="".join(f'<li style="padding:10px 0;border-top:1px solid rgba(179,51,51,.4);font-size:21px;color:#B33">× {o}</li>' for o in ("صور استوك عامة بلا علاقة بالمكان","ألوان مشبعة أو فلاتر درامية","وجوه نماذج غير حقيقية أو مبتسمة للكاميرا","صور ثلاثية الأبعاد أو مولّدة تُقدَّم كأعمال منفذة"))
pages.append(f"""<div class="page">{H(11,"الإخراج البصري للصور")}
 <div style="position:absolute;right:120px;top:150px;width:1100px"><div class="lat olive" style="font-size:18px;margin-bottom:10px">Photography</div><h1 style="font-size:56px">نُصوّر ما نُسلّمه</h1>
 <p style="margin-top:14px;font-size:24px">الصورة عندنا وثيقة تنفيذ، لا لوحة إعلانية. ولهذا تبدو دافئة وواقعية وقريبة من التفاصيل. تُنشر الأعمال بموافقة أصحابها، وأي صورة غير حقيقية تُعنوَن «صورة توضيحية».</p></div>
 <div style="position:absolute;left:120px;right:120px;top:400px;display:grid;grid-template-columns:repeat(4,1fr);gap:16px">{pt}</div>
 <div style="position:absolute;left:120px;right:120px;top:740px"><div style="font-size:20px;font-weight:600;margin-bottom:6px">خارج الإطار</div><ul style="list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:0 40px">{out}</ul></div>{ftr(11)}</div>""")
pg = 12

for D in 'A':
    # ---- التطبيقات ----
    def card():
        front = f'<div style="width:420px;height:240px;background:var(--char);display:flex;align-items:center;justify-content:center;box-shadow:0 18px 30px rgba(0,0,0,.35)"><div style="width:240px">{logo(D,"logo","reverse",tagline=False)}</div></div>'
        back = f'''<div style="width:420px;height:240px;background:var(--cream);padding:28px 30px;box-shadow:0 18px 30px rgba(0,0,0,.25);position:relative"><div style="width:44px;position:absolute;left:28px;top:26px">{logo(D,"icon","color")}</div>
         <div style="margin-top:96px;font-weight:600;font-size:21px">فهد سعد العجمي</div><div style="font-size:14px;color:var(--deep)">المؤسس ورئيس مجلس الإدارة</div>
         <div class="ltr" style="font-family:BSD;font-size:13px;margin-top:12px;letter-spacing:.06em">0506221548 · info@goldenvale.com</div><div style="font-size:12px;color:var(--deep);margin-top:2px">الرياض، المملكة العربية السعودية</div></div>'''
        return front, back
    cf, cb = card()
    letter = f'''<div style="width:340px;height:480px;background:#fff;box-shadow:0 18px 30px rgba(0,0,0,.28);padding:32px;position:relative"><div style="width:130px">{logo(D,"logo","color",tagline=False)}</div>
      <div style="margin-top:60px">{"".join('<div style="height:7px;background:#ddd;margin:13px 0;width:%d%%"></div>'%w for w in (96,88,92,70,94,85,60))}</div>
      <div style="position:absolute;left:32px;right:32px;bottom:26px;border-top:1px solid var(--olive);padding-top:8px;font-size:11px;color:var(--deep);display:flex;justify-content:space-between"><span>الرياض · المملكة العربية السعودية</span><span class="ltr" style="font-family:BSD">info@goldenvale.com</span></div></div>'''
    envelope = f'''<div style="width:520px;height:250px;background:var(--cream);box-shadow:0 14px 26px rgba(0,0,0,.28);position:relative"><div style="width:50px;position:absolute;right:26px;top:22px">{logo(D,"icon","color")}</div>
      <div style="position:absolute;left:34px;bottom:30px;font-size:13px;color:var(--deep);line-height:1.9">اسم المستلم<br>العنوان — الرياض</div><div style="position:absolute;left:0;right:0;top:0;height:95px;border-bottom:1px solid rgba(122,95,30,.5);clip-path:polygon(0 0,100% 0,50% 100%)"></div></div>'''
    folder = f'''<div style="width:330px;height:440px;background:var(--char);box-shadow:0 18px 30px rgba(0,0,0,.4);position:relative;display:flex;align-items:center;justify-content:center"><div style="position:absolute;inset:0;opacity:.8">{art("valley",330,440,"#D4A94E",op=.3)}</div><div style="width:200px;position:relative">{logo(D,"logo","reverse")}</div></div>'''
    fascia = f'''<div style="width:760px;height:260px;background:#2B3A5C;box-shadow:0 18px 34px rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center;position:relative"><div style="width:60%;padding:28px;background:var(--char);box-shadow:0 0 60px 8px rgba(212,169,78,.45)">{logo(D,"logo","reverse")}</div></div>'''
    polo = f'''<svg viewBox="0 0 300 300" style="width:330px"><path d="M95 20 L55 38 L12 100 L52 122 L72 96 L72 280 H228 V96 L248 122 L288 100 L245 38 L205 20 Q150 62 95 20Z" fill="#14213D"/><path d="M120 22 L150 70 L180 22" fill="none" stroke="#2d2c29" stroke-width="3"/><g transform="translate(176 104) scale(.2)">{logos.get(D,"icon","reverse")[0].split(">",1)[1].rsplit("</svg>",1)[0]}</g></svg>'''
    banner = f'''<div style="width:240px;height:480px;background:var(--char);box-shadow:0 18px 30px rgba(0,0,0,.4);position:relative;overflow:hidden"><div style="position:absolute;inset:0">{art("beams",240,480,"#D4A94E",op=.4)}</div><div style="position:absolute;left:30px;right:30px;top:40px">{logo(D,"logo","reverse")}</div><div style="position:absolute;left:24px;right:24px;bottom:70px;text-align:center;color:var(--cream);font-size:26px;font-weight:300">[اسم الفعالية]</div></div>'''
    def lab(t): return f'<div style="position:absolute;font-size:16px;background:var(--olive);color:#fff;padding:2px 12px;font-weight:500">{t}</div>'
    wall = "linear-gradient(180deg,#D9D3C3,#D9D3C3)"
    pages.append(f'''<div class="page" style="background:{wall}">{hdr(pg,f"التطبيقات (1/2) — تصوّر")}
     <div style="position:absolute;left:120px;top:170px;display:flex;flex-direction:column;gap:30px">{cf}{cb}</div>
     <div style="position:absolute;left:640px;top:170px">{letter}</div>
     <div style="position:absolute;right:120px;top:170px;display:flex;flex-direction:column;gap:30px;align-items:flex-end">{envelope}{folder}</div>
     <div class="tag" style="left:120px;bottom:100px">تصوّر — بطاقة العمل</div><div class="tag" style="left:640px;bottom:100px">تصوّر — الورق الرسمي</div><div class="tag" style="right:120px;bottom:100px">تصوّر — المظروف والمجلد</div>{ftr(pg).replace("color:var(--deep)","")}</div>''')
    pg += 1
    pages.append(f'''<div class="page" style="background:{wall}">{hdr(pg,f"التطبيقات (2/2) — تصوّر")}
     <div style="position:absolute;left:120px;top:180px">{fascia}</div>
     <div style="position:absolute;left:120px;top:520px;display:flex;gap:70px;align-items:flex-start">{polo}<div style="width:200px;height:290px;background:var(--cream);box-shadow:0 14px 24px rgba(0,0,0,.3);margin-top:20px;position:relative;padding:20px"><div style="width:120px">{logo(D,"logo","color",tagline=False)}</div><div style="margin-top:90px;font-size:18px;font-weight:600">[الاسم]</div><div style="font-size:12px;color:var(--deep)">منظّم · فريق العمليات</div></div></div>
     <div style="position:absolute;right:300px;top:180px">{banner}</div>
     <div style="position:absolute;right:120px;top:210px;width:140px;writing-mode:vertical-rl"></div>
     <div class="tag" style="left:120px;top:150px;display:none"></div>
     <div class="tag" style="left:120px;bottom:100px">تصوّر — لوحة واجهة مضيئة</div><div class="tag" style="left:560px;bottom:100px">تصوّر — الزي والبطاقة</div><div class="tag" style="right:300px;bottom:100px">تصوّر — بنر فعاليات</div>{ftr(pg)}</div>''')
    pg += 1



# ---- القواعد والخطوات التالية ----
rules=[("شبكة من 8 نقاط","كل مسافة أو قياس داخلي من مضاعفات 8px."),("خطوط فاصلة لا ظلال","الفصل بين العناصر بخط 1px من الرملي أو العاجي، دون ظلال أو تدرجات."),("صور من البيئة","مواقع سعودية واقعية وإضاءة دافئة، بلا فلاتر مبالغة."),("نبرة الصوت","واثقة ومباشرة وبلا مبالغة: نقول ما نفعله، ونفي بما نعده.")]
rr="".join(f'<div style="border-top:3px solid var(--olive);padding:22px 0"><span class="num olive" style="font-size:30px;letter-spacing:.2em" dir="ltr">{i+1:02d}</span><h3 style="font-size:32px;margin-top:6px">{t}</h3><p style="font-size:21px;line-height:1.8;margin-top:6px">{d}</p></div>' for i,(t,d) in enumerate(rules))
nots="".join(f'<li style="padding:12px 0;border-top:1px solid rgba(179,51,51,.4);font-size:23px;color:#B33">× {o}</li>' for o in ("تدوير الشعار أو تمديده أو إضافة ظل إليه","استخدام ألوان خارج الجدول السبعة","إضافة خطوط أو كلمات إلى تركيبة الشعار","وضع نص فوق صورة دون طبقة تعتيم كافية"))
pages.append(f"""<div class="page">{H(pg,"قواعد الاستخدام")}
 <div style="position:absolute;right:120px;top:150px"><div class="lat olive" style="font-size:18px;margin-bottom:10px">Usage Rules</div><h1 style="font-size:56px">قواعد تحفظ اتساق العلامة</h1></div>
 <div style="position:absolute;left:120px;right:120px;top:340px;display:grid;grid-template-columns:repeat(4,1fr);gap:30px">{rr}</div>
 <div style="position:absolute;left:120px;right:120px;top:690px;display:grid;grid-template-columns:1fr 1fr;gap:60px"><div><div style="font-size:22px;font-weight:600;margin-bottom:6px">ما لا يُفعل</div><ul style="list-style:none">{nots}</ul></div>
 <div style="background:var(--char);color:var(--cream);padding:34px;font-size:25px;line-height:1.8">عند الشك، استخدم الشعار بالكحلي على العاجي: الحالة الأساسية المعتمدة.</div></div>{ftr(pg)}</div>""")
pg += 1
nx=[("اعتماد الدليل","مراجعة كتابية من مؤسس الشركة قبل أي طباعة."),("فحص التسجيل","التحقق من توفر «Golden Vale» والشعار لدى الهيئة السعودية للملكية الفكرية."),("بروفة المطبعة","طباعة بروفة وتأكيد الذهبي والكحلي، فقيم CMYK هنا إرشادية."),("صور حقيقية","استبدال أي صورة توضيحية بصور أعمال منفذة موثّقة وبموافقة أصحابها.")]
nr="".join(f'<div style="display:flex;gap:34px;align-items:baseline;border-top:1px solid rgba(122,95,30,.4);padding:22px 0"><span class="num olive" style="font-size:44px;width:80px" dir="ltr">{i+1:02d}</span><div><h3 style="font-size:32px">{t}</h3><p style="font-size:23px;margin-top:4px">{d}</p></div></div>' for i,(t,d) in enumerate(nx))
pages.append(f"""<div class="page cream">{H(pg,"الخطوات التالية")}<div style="position:absolute;right:120px;top:170px;width:1250px"><h1 style="font-size:60px;margin-bottom:24px">الخطوات التالية</h1>{nr}</div>
 <div style="position:absolute;left:120px;bottom:90px;font-size:22px;line-height:1.9" class="deepc">Golden Vale · الرياض، المملكة العربية السعودية<br><span class="ltr">0506221548 · info@goldenvale.com</span></div>{ftr(pg)}</div>""")

open("build/guide.html","w",encoding="utf-8").write(html("Golden Vale — دليل الهوية البصرية", pages))
print(len(pages), "pages")
