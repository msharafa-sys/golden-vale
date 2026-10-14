# -*- coding: utf-8 -*-
"""ملف تعريفي 25 صفحة — Golden Vale (الاتجاه أ). بلا خطوط ذهبية، RTL، صور توضيحية، عملاء placeholders."""
import re
from common import *
art = lambda *a, **k: ""
P_ = logos.PAL
PH = "[نص مؤقت]"
BV = "<bdi>Golden Vale</bdi>"
pages = []
CUT = 52

def hdr(n, section, left=120):
    return f'<div class="hdr" style="left:{left}px"><span>{section}</span><span class="lat">Golden Vale · {n:02d}</span></div>'
def ftr(n, left=120):
    return f'<div class="ftr" style="left:{left}px"><span class="num" style="font-size:20px">{n:02d}</span><span class="lat" style="font-size:14px">Company Profile · Riyadh · 2026</span></div>'
def photo(name, x, y, w, h, tag=True, anchor="left", cut=CUT):
    clip = f"polygon(0 0,{w-cut}px 0,{w}px {cut}px,{w}px {h}px,0 {h}px)"
    t = '<span style="position:absolute;left:0;bottom:0;background:rgba(27,26,24,.72);color:#EDE6D8;font-size:13px;padding:4px 14px">صورة توضيحية</span>' if tag else ""
    return (f'<div style="position:absolute;{anchor}:{x}px;top:{y}px;width:{w}px;height:{h}px;clip-path:{clip};overflow:hidden;background:var(--char)">'
            f'<img src="../images/{name}.jpg" style="width:100%;height:100%;object-fit:cover;display:block">{t}</div>')
def ph(x, y, w, h, text="[صورة — تُضاف لاحقًا]", anchor="left"):
    return f'<div class="ph" style="position:absolute;{anchor}:{x}px;top:{y}px;width:{w}px;height:{h}px">{text}</div>'
def title(en, ar, dark=False, top=160, w=1200):
    c = "var(--olive-l)" if dark else "var(--olive)"
    return f'<div style="position:absolute;right:120px;top:{top}px;width:{w}px"><div class="lat" style="font-size:18px;margin-bottom:16px;color:{c}">{en}</div><h1>{ar}</h1></div>'
def add(fn, cls=""):
    n = len(pages) + 1
    pages.append(f'<div class="page {cls}">{fn(n)}</div>')

# 01 غلاف
add(lambda n: f'<div style="position:absolute;left:0;right:0;top:230px;display:flex;justify-content:center"><div style="width:760px">{logo("A","logo","paper")}</div></div>'
    f'<div style="position:absolute;left:0;right:0;top:770px;text-align:center"><h2 style="font-weight:300;font-size:64px">الملف التعريفي للشركة</h2><div class="lat" style="margin-top:26px;font-size:20px;color:var(--olive-l)">Company Profile · Riyadh · 2026</div></div>', "dark")

# 02 المحتويات
SECS = [("نظرة عامة","Overview",3),("كلمة رئيس مجلس الإدارة","Chairman's Message",4),("الرؤية والرسالة","Vision & Mission",5),("القيم الجوهرية","Core Values",6),
        ("خدماتنا","Services",7),("القطاعات المستهدفة","Target Sectors",12),("نموذج التنفيذ","Delivery Model",13),("منهجية العمل","How We Work",14),
        ("مراحل التنفيذ","Project Phases",15),("الجودة والسلامة","Quality & Safety",16),("لماذا Golden Vale","Why Golden Vale",17),("طرق التعاون","Engagement",18),
        ("معرض الصور","Gallery",19),("نموذج دراسة حالة","Case Study",20),("العملاء والشركاء","Clients",21),("الفريق","Team",22),("هويتنا البصرية","Our Identity",23),("التواصل","Contact",24)]
def row(i, a, b, p):
    return (f'<div style="display:flex;align-items:baseline;gap:22px;border-top:1px solid rgba(27,26,24,.13);padding:15px 0"><span class="num olive" style="font-size:28px;width:56px">{i+1:02d}</span>'
            f'<span style="font-size:27px;font-weight:400;flex:1">{a}</span><span class="lat" style="font-size:12px;color:var(--deep)">{b}</span><span class="num" style="font-size:22px;width:44px;text-align:left">{p:02d}</span></div>')
def contents(n):
    c1 = "".join(row(i, *SECS[i]) for i in range(9)); c2 = "".join(row(i, *SECS[i]) for i in range(9, 18))
    return (hdr(n, "المحتويات") + title("Contents", "المحتويات") +
            f'<div style="position:absolute;right:120px;top:340px;width:820px">{c1}</div><div style="position:absolute;left:120px;top:340px;width:820px">{c2}</div>' + ftr(n))
add(contents)

# 03 نظرة عامة
FACTS = [("الاسم التجاري","Golden Vale"),("الكيان","شركة ذات مسؤولية محدودة (شخص واحد)"),("التأسيس","2026"),("المقر","الرياض، المملكة العربية السعودية"),("المجال","الدعاية والإعلان وتنظيم الفعاليات"),("الرقم الوطني الموحد (السجل التجاري)",'<span class="ltr" style="font-family:Jost;font-weight:300">7055194109</span>')]
fx = "".join(f'<div style="display:flex;justify-content:space-between;border-top:1px solid rgba(27,26,24,.13);padding:15px 0;font-size:23px"><span class="deepc" style="font-weight:500">{a}</span><span style="font-weight:300">{b}</span></div>' for a, b in FACTS)
add(lambda n: hdr(n,"نظرة عامة") +
    f'<div style="position:absolute;right:120px;top:190px;width:980px"><div class="lat olive" style="font-size:18px;margin-bottom:22px">Overview</div><h1>وكالة سعودية للدعاية والإعلان وتنظيم الفعاليات</h1>'
    f'<p style="margin-top:34px">تأسست {BV} عام 2026 في الرياض لتقدّم للعلامات التجارية والجهات حلولًا متكاملة في الدعاية والإعلان وتنظيم الفعاليات وإدارة الهوية البصرية وتصميم التجارب الإبداعية، عبر نقطة اتصال واحدة من الفكرة حتى التسليم.</p>'
    f'<p style="margin-top:14px" class="small deepc">{PH} نموذج التنفيذ (فريق داخلي، أو شركاء إنتاج معتمدون، أو كلاهما) يُحدَّد قبل الاعتماد النهائي.</p></div>'
    f'<div style="position:absolute;left:120px;top:210px;width:560px;background:var(--cream);padding:34px 40px">{fx}</div>' + photo("overview",120,700,560,250) + ftr(n))

# 04 كلمة رئيس مجلس الإدارة
add(lambda n: ph(0,0,640,1080,"[صورة رئيس مجلس الإدارة — تُضاف لاحقًا]").replace('border:2px dashed','border:none;border:0').replace('class="ph"','class="ph" data-x="1"') +
    '<div style="position:absolute;right:120px;top:130px;width:1000px"><div class="lat olive" style="font-size:18px;margin-bottom:34px">Chairman\'s Message</div>'
    '<h2 style="font-weight:400;font-size:52px;line-height:1.55">نؤمن أن لكل علامة حضورًا يستحق أن يُصنع بعناية، وأن الفعالية الناجحة تبدأ بفكرة واضحة وتنتهي بتسليم منضبط.</h2>'
    '<p style="margin-top:36px;font-size:25px">تنطلق '+BV+' في مرحلة يشهد فيها قطاع الفعاليات والترفيه في المملكة نموًا متسارعًا ضمن مستهدفات رؤية 2030. ونلتزم بأن نكون شريكًا يُعتمد عليه في الجودة والمواعيد والشفافية، وببناء كل علاقة مع عملائنا على الثقة والنتائج.</p>'
    f'<div style="border-top:1px solid rgba(27,26,24,.13);margin-top:44px;padding-top:26px"><h3>فهد سعد العجمي</h3><div class="deepc" style="font-size:22px;margin-top:4px">المؤسس ورئيس مجلس الإدارة</div><div class="small deepc" style="margin-top:14px">{PH} مسودة للمراجعة والاعتماد قبل النشر.</div></div></div>', "cream")

# 05 الرؤية والرسالة
add(lambda n: hdr(n,"الرؤية والرسالة") +
    '<div style="position:absolute;right:120px;top:260px;width:720px"><div class="lat" style="color:var(--olive-l);font-size:18px">Vision</div><h1 style="margin:22px 0 30px;color:var(--cream)">رؤيتنا</h1><p style="margin-top:36px;font-size:32px;line-height:1.9">أن نكون الشريك الأول للعلامات والجهات في المملكة لصناعة حضور لا يُنسى.</p></div>'
    '<div style="position:absolute;left:50%;top:230px;bottom:200px;width:1px;background:rgba(237,230,216,.2)"></div>'
    '<div style="position:absolute;left:120px;top:260px;width:720px"><div class="lat" style="color:var(--olive-l);font-size:18px">Mission</div><h1 style="margin:22px 0 30px;color:var(--cream)">رسالتنا</h1><p style="margin-top:36px;font-size:32px;line-height:1.9">تحويل أهداف عملائنا إلى حملات وفعاليات متقنة، عبر منهجية واضحة تجمع الفكرة والتصميم والإنتاج والتشغيل.</p></div>' + ftr(n), "dark")

# 06 القيم
VALS = [("الإبداع","أفكار تلفت الانتباه وتخدم هدف العميل."),("الإتقان","عناية بالتفاصيل في كل مرحلة، من الفكرة إلى التسليم."),("الالتزام","جداول معتمدة وتسليم في الموعد."),("المرونة","نتكيّف مع المتغيرات وتغيّر المتطلبات."),("الشراكة","نجاح العميل هو مقياس نجاحنا.")]
def cards(items, h=470, top=430, cols=None, dark_last=True, gap=26, title_size=38):
    cols = cols or len(items)
    out = "".join(f'<div style="background:{"var(--char)" if (dark_last and i==len(items)-1) else "#fff"};color:{"var(--cream)" if (dark_last and i==len(items)-1) else "var(--char)"};padding:34px 30px;height:{h}px"><div class="num" style="font-size:44px;color:{"var(--olive-l)" if (dark_last and i==len(items)-1) else "var(--olive)"}">{i+1:02d}</div><h3 style="margin:{h//5}px 0 14px;font-size:{title_size}px">{a}</h3><p style="font-size:22px;line-height:1.8">{b}</p></div>' for i, (a, b) in enumerate(items))
    return f'<div style="position:absolute;left:120px;right:120px;top:{top}px;display:grid;grid-template-columns:repeat({cols},1fr);gap:{gap}px">{out}</div>'
add(lambda n: hdr(n,"القيم الجوهرية") + title("Core Values","قيمنا الجوهرية",top=180) + cards(VALS) + ftr(n))

# 07 خدماتنا — نظرة
SV = [("الدعاية والإعلان","حملات متكاملة، إعلانات الطرق واللوحات، الإعلانات الرقمية، وإنتاج المحتوى المرئي."),("تنظيم الفعاليات","مؤتمرات وملتقيات، فعاليات مؤسسية وموسمية، حفلات إطلاق، وإنتاج وإضاءة وصوت."),("إدارة الهوية البصرية","تصميم الهوية، مطبوعات وتغليف، لوحات وواجهات، وزي موحد وهدايا."),("التجارب الإبداعية","معارض وأجنحة، تفعيلات تفاعلية، مناطق تصوير، وتجارب رقمية.")]
add(lambda n: hdr(n,"خدماتنا") + title("Our Services","أربع خدمات تحت سقف واحد",top=180) + cards(SV, h=470, top=430, dark_last=False) + ftr(n), "cream")

# 08-11 الخدمات
SERV = [("01","Advertising","الدعاية والإعلان","حملات تبدأ من الفكرة وتنتهي بالأثر، عبر قنوات تصل إلى جمهورك في المكان والوقت المناسبين.",["حملات إعلانية متكاملة","إعلانات الطرق واللوحات","الإعلانات الرقمية","إنتاج المحتوى المرئي"],"svc-ads",False),
        ("02","Events","تنظيم الفعاليات","من الفكرة إلى الافتتاح، ندير كل مرحلة بدقة لتقديم فعاليات منظمة وتجربة تُرضي الحضور.",["المؤتمرات والملتقيات","الفعاليات المؤسسية والموسمية","حفلات الإطلاق","الإنتاج والإضاءة والصوت"],"svc-events",True),
        ("03","Brand Identity","إدارة الهوية البصرية","هوية متسقة في كل نقطة تماس، من اللوحة إلى الهدية إلى الزي الموحد.",["تصميم الهوية البصرية","المطبوعات والتغليف","اللوحات والواجهات","الزي الموحد والهدايا"],"svc-brand",False),
        ("04","Creative Experiences","التجارب الإبداعية","تجارب تفاعلية تجعل الزائر جزءًا من حكاية علامتك.",["المعارض والأجنحة","التفعيلات التفاعلية","مناطق التصوير","التجارب الرقمية"],"svc-exp",True)]
def service(i):
    num, en, ar, desc, subs, img, dk = SERV[i]
    def f(n):
        boxes = "".join(f'<div style="border:1.5px solid {"rgba(237,230,216,.28)" if dk else "rgba(27,26,24,.18)"};padding:22px 26px;font-size:24px;font-weight:400;background:{"transparent" if dk else "var(--cream)"}">{s}</div>' for s in subs)
        c = "var(--olive-l)" if dk else "var(--olive)"
        return (hdr(n,"خدماتنا") + photo(img,120,170,880,540) +
                f'<div style="position:absolute;left:120px;top:740px;width:880px;display:grid;grid-template-columns:1fr 1fr;gap:16px">{boxes}</div>'
                f'<div style="position:absolute;right:120px;top:170px;width:700px"><div style="display:flex;align-items:baseline;gap:26px"><span class="num" style="font-size:96px;color:{c}">{num}</span><span class="lat" style="font-size:18px;color:{c}">{en}</span></div>'
                f'<h1 style="margin:26px 0 30px">{ar}</h1><p style="font-size:28px">{desc}</p></div>' + ftr(n))
    return f, ("dark" if dk else "")
for i in range(4):
    fn, cl = service(i); add(fn, cl)

# 12 القطاعات المستهدفة
SECT = [("المطورون العقاريون","لوحات المواقع وتغليف السياجات والمكعبات الإعلانية."),("المعارض التجارية","أجنحة مخصصة للشركات والعلامات التجارية."),("الجهات الحكومية","حملات توعوية ومعارض داخلية."),("الوجهات الترفيهية","مواسم ومناسبات وبوابات ومجسمات."),("قطاع التجزئة","واجهات المتاجر والتفعيلات الموسمية.")]
add(lambda n: hdr(n,"القطاعات المستهدفة") + title("Target Sectors","القطاعات التي نستهدفها",top=180) + cards(SECT, h=470, top=430, dark_last=False, gap=22, title_size=32) + ftr(n))

# 13 نموذج التنفيذ
STEPS4 = [("التصميم والتصور","تصاميم ثلاثية الأبعاد ومقاسات معتمدة قبل أي تصنيع."),("التصنيع والإنتاج","إنتاج العناصر وفق المواصفات المعتمدة وفحصها."),("التركيب والتشغيل","تركيب في الموقع وتشغيل بإشراف مباشر."),("الفك والتسليم","فك وإعادة الموقع وتسليم بمحضر استلام.")]
def delivery(n):
    out = "".join(f'<div style="background:rgba(237,230,216,.06);padding:34px 30px;height:430px"><div class="num" style="font-size:44px;color:var(--olive-l)">{i+1:02d}</div><h3 style="margin:84px 0 14px;font-size:34px;color:var(--cream)">{a}</h3><p style="font-size:22px;line-height:1.8;color:var(--cream)">{b}</p></div>' for i, (a, b) in enumerate(STEPS4))
    return (hdr(n,"نموذج التنفيذ") + title("Delivery Model","من التصميم إلى التسليم",dark=True,top=180) +
            f'<div style="position:absolute;left:120px;right:120px;top:430px;display:grid;grid-template-columns:repeat(4,1fr);gap:22px">{out}</div>'
            f'<div style="position:absolute;right:120px;top:900px;font-size:19px;color:var(--olive-l)">{PH} يُحدَّد ما يُنفَّذ داخليًا وما يُنفَّذ عبر شركاء إنتاج معتمدين.</div>' + ftr(n))
add(delivery, "dark")

# 14 منهجية العمل
METH = [("الاستماع","نفهم هدفك وجمهورك وميزانيتك."),("التصور","نقدّم الفكرة والتصاميم وعرض السعر."),("التنفيذ","إنتاج وتشغيل بإشراف مباشر."),("المتابعة","قياس الأثر وتقرير ختامي.")]
def meth(n):
    st = "".join(f'<div style="display:flex;align-items:center;gap:44px;border-top:1px solid rgba(27,26,24,.13);padding:24px 0"><span class="num olive" style="font-size:64px;width:130px">{i+1:02d}</span><div><h3 style="font-size:40px">{a}</h3><p class="small" style="font-size:24px;line-height:1.6">{b}</p></div></div>' for i, (a, b) in enumerate(METH))
    return hdr(n,"منهجية العمل") + title("How We Work","آلية العمل",top=180,w=1000) + f'<div style="position:absolute;right:120px;top:340px;width:1000px">{st}</div>' + photo("method",120,190,520,760) + ftr(n)
add(meth)

# 15 مراحل التنفيذ
PH5 = [("التخطيط","خطة المشروع وجدول التسليم."),("التصميم والاعتماد","تصاميم معتمدة وعرض سعر."),("الإنتاج","عناصر مصنّعة ومفحوصة."),("التركيب","تركيب في الموقع بمحضر استلام."),("التشغيل والختام","تشغيل ومتابعة وتقرير ختامي.")]
def phases(n):
    out = "".join(f'<div style="background:#fff;padding:30px 26px;height:400px"><div class="lat" style="font-size:13px;color:var(--olive)">Phase {i+1:02d}</div><h3 style="margin:60px 0 12px;font-size:32px">{a}</h3><div class="deepc" style="font-size:16px;margin-bottom:6px">المخرجات</div><p style="font-size:21px;line-height:1.7">{b}</p></div>' for i, (a, b) in enumerate(PH5))
    return (hdr(n,"مراحل التنفيذ") + title("Project Phases","مراحل تنفيذ الفعالية أو المشروع",top=180) +
            f'<div style="position:absolute;left:120px;right:120px;top:430px;display:grid;grid-template-columns:repeat(5,1fr);gap:20px">{out}</div>'
            f'<div style="position:absolute;right:120px;top:880px;font-size:19px" class="deepc">{PH} تُحدَّد مدة كل مرحلة في عرض السعر حسب نطاق المشروع.</div>' + ftr(n))
add(phases, "cream")

# 16 الجودة والسلامة
QS = [("فحص الجودة قبل التسليم","نراجع العناصر المصنّعة والمطبوعة على المواصفات المعتمدة قبل شحنها."),("السلامة في المواقع","نلتزم باشتراطات السلامة المهنية في مواقع التركيب والأعمال على الارتفاعات."),("توثيق الاستلام","نوثّق التسليم بمحضر استلام موقّع من العميل."),("ضبط التعديلات","نسجّل أي تعديل في المقاسات أو النطاق ونعتمد أثره على السعر والجدول.")]
def quality(n):
    out = "".join(f'<div style="display:flex;gap:30px;align-items:baseline;border-top:1px solid rgba(27,26,24,.13);padding:22px 0"><span class="num olive" style="font-size:40px;width:70px">{i+1:02d}</span><div><h3 style="font-size:32px">{a}</h3><p style="font-size:22px;line-height:1.7">{b}</p></div></div>' for i, (a, b) in enumerate(QS))
    return (hdr(n,"الجودة والسلامة") + title("Quality & Safety","التزاماتنا في الجودة والسلامة",top=180) +
            f'<div style="position:absolute;right:120px;top:360px;width:1000px">{out}</div>' + ph(120,360,560,420,"[الشهادات والتراخيص — تُضاف عند توفرها]") + ftr(n))
add(quality)

# 17 لماذا Golden Vale
WHY = [("نقطة اتصال واحدة","تصميم وإنتاج وتشغيل تحت إدارة واحدة."),("فكرة أصيلة","مفاهيم مستوحاة من هوية العلامة والمكان."),("التزام بالمواعيد","جداول معتمدة ومتابعة مستمرة."),("شفافية التسعير","عروض أسعار مفصلة ونطاق عمل واضح."),("جودة التنفيذ","خامات ومعايير إنتاج محددة سلفًا."),("دعم مستمر","متابعة قبل الفعالية وخلالها وبعدها.")]
wc = "".join(f'<div style="background:#fff;padding:34px;height:285px"><div class="num olive" style="font-size:30px">{i+1:02d}</div><h3 style="margin:30px 0 10px;font-size:34px">{a}</h3><p style="font-size:22px;line-height:1.7">{b}</p></div>' for i, (a, b) in enumerate(WHY))
add(lambda n: hdr(n,f"لماذا {BV}") + title("Why Golden Vale",f"لماذا {BV}",top=170) + f'<div style="position:absolute;left:120px;right:120px;top:400px;display:grid;grid-template-columns:repeat(3,1fr);gap:22px">{wc}</div>' + ftr(n), "cream")

# 18 طرق التعاون
ENG = [("مشروع محدد","نطاق وسعر ومدة واضحة لمشروع أو فعالية واحدة."),("عقد مواسم متكرر","تنفيذ مواسم وفعاليات دورية بشروط وأسعار متفق عليها سلفًا."),("دعم فريق العميل","إسناد جزء من العمل: تصميم أو تصنيع أو تركيب أو تشغيل.")]
add(lambda n: hdr(n,"طرق التعاون") + title("Engagement Models","كيف نعمل معكم",top=180) + cards(ENG, h=440, top=430, dark_last=False, gap=26) + ftr(n))

# 19 معرض الصور
def gallery(n):
    tiles = [("svc-events","مسرح وإضاءة"),("svc-ads","شاشة إعلانية"),("svc-brand","واجهة محل"),("svc-exp","جدار تفاعلي"),("gal-lounge","صالة استقبال"),("gal-build","تجهيز مسرح")]
    out = ""
    for i, (img, cap) in enumerate(tiles):
        x = 120 + (i % 3) * (544 + 24); y = 330 + (i // 3) * (300 + 24)
        out += photo(img, x, y, 544, 300, cut=36)
    return hdr(n,"معرض الصور") + title("Gallery","معرض الصور",dark=True,top=160) + f'<div style="position:absolute;left:120px;top:210px;font-size:17px;color:var(--olive-l);max-width:640px;text-align:left">صور توضيحية للأجواء والمستوى المستهدف، وليست أعمالًا منفذة.</div>' + out + ftr(n)
add(gallery, "dark")

# 20 نموذج دراسة حالة
def casestudy(n):
    meta = "".join(f'<div style="flex:1;background:var(--cream);padding:18px 22px"><div class="deepc" style="font-size:16px">{a}</div><div style="font-size:22px;margin-top:4px">[يُضاف]</div></div>' for a in ("العميل","نوع المشروع","الموقع","المدة"))
    cols = "".join(f'<div style="background:#fff;padding:34px 30px;height:400px"><div class="num olive" style="font-size:36px">{i+1:02d}</div><h3 style="margin:44px 0 12px;font-size:34px">{a}</h3><p style="font-size:22px;line-height:1.8" class="deepc">{PH} {b}</p></div>' for i, (a, b) in enumerate((("التحدي","ما الذي طلبه العميل وما القيود؟"),("الحل","ما الذي صمّمناه ونفّذناه؟"),("النتيجة","ما الذي تحقق؟ بأرقام موثّقة وبموافقة العميل."))))
    return (hdr(n,"نموذج دراسة حالة") + title("Case Study","[اسم المشروع]",top=170) +
            f'<div style="position:absolute;left:120px;right:120px;top:330px;display:flex;gap:16px">{meta}</div>' +
            f'<div style="position:absolute;left:120px;right:120px;top:480px;display:grid;grid-template-columns:repeat(3,1fr);gap:22px">{cols}</div>' +
            f'<div style="position:absolute;right:120px;top:930px;font-size:18px" class="deepc">تُملأ بمشروع منفذ وبموافقة كتابية من العميل، ولا تُنشر أرقام غير موثّقة.</div>' + ftr(n))
add(casestudy)

# 21 العملاء والشركاء — يقرأ clients.json؛ لا يظهر اسم إلا إذا consent=true (موافقة كتابية)
import json
CL = json.load(open("clients.json", encoding="utf-8"))
def clients(n):
    boxes = ""
    for c in CL[:12]:
        if c.get("consent"):
            boxes += f'<div style="height:170px;display:flex;align-items:center;justify-content:center;text-align:center;background:rgba(237,230,216,.08);font-size:26px;font-weight:400;color:var(--cream);padding:16px">{c["name"]}</div>'
        else:
            boxes += '<div class="ph" style="height:170px;font-size:19px">[عميل — بانتظار الموافقة]<br>[يُضاف]</div>'
    return (hdr(n,"العملاء والشركاء") + title("Clients & Partners","عملاؤنا وشركاؤنا",dark=True,top=160) +
            '<div style="position:absolute;right:120px;top:300px;font-size:19px;color:var(--olive-l)">[تُضاف الأسماء والشعارات بعد الحصول على موافقة كل عميل كتابيًا، ولا يُنشر أي اسم قبل ذلك.]</div>' +
            f'<div style="position:absolute;left:120px;right:120px;top:400px;display:grid;grid-template-columns:repeat(6,1fr);gap:20px">{boxes}</div>' + ftr(n))
add(clients, "dark")

# 22 الفريق
ROLES = [("الإدارة التنفيذية","فهد سعد العجمي — المؤسس"),("الإبداع والتصميم","[الاسم — يُضاف]"),("الإنتاج والتصنيع","[الاسم — يُضاف]"),("العمليات والتركيب","[الاسم — يُضاف]")]
def team(n):
    out = "".join(f'<div style="background:#fff"><div class="ph" style="height:300px;border:none;background:var(--cream)">[صورة — تُضاف لاحقًا]</div><div style="padding:26px 26px 30px"><h3 style="font-size:30px">{a}</h3><p style="font-size:21px;margin-top:8px" class="deepc">{b}</p></div></div>' for a, b in ROLES)
    return hdr(n,"الفريق") + title("Team","الفريق",top=170) + f'<div style="position:absolute;left:120px;right:120px;top:360px;display:grid;grid-template-columns:repeat(4,1fr);gap:24px">{out}</div>' + ftr(n)
add(team)

# 23 هويتنا
def identity(n):
    sw = [("زيتوني ذهبي",P_["olive"]),("فحمي",P_["char"]),("كريمي",P_["cream"]),("زيتوني فاتح",P_["olive_light"]),("زيتوني عميق",P_["deep"]),("حجر",P_["stone"])]
    s = "".join(f'<div style="background:{h};height:170px;padding:18px 20px;display:flex;flex-direction:column;justify-content:flex-end;{"border:1px solid rgba(237,230,216,.3);" if h==P_["char"] else ""}color:{"#1B1A18" if h in (P_["cream"],P_["olive_light"],P_["stone"]) else "#EDE6D8"}"><div style="font-size:19px;font-weight:500">{a}</div><div class="num" style="font-size:15px;direction:ltr;text-align:right">{h.upper()}</div></div>' for a, h in sw)
    return (hdr(n,"هويتنا البصرية") + title("Our Identity","هويتنا البصرية",dark=True,top=160) +
            f'<div style="position:absolute;left:120px;top:380px;width:560px">{logo("A","logo","paper")}</div>' +
            f'<div style="position:absolute;right:120px;top:360px;width:900px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px">{s}</div>' +
            '<div style="position:absolute;right:120px;top:780px;width:900px;font-size:22px;line-height:1.9;color:var(--cream)">الخطوط: <span style="font-family:Jost">Jost</span> للاتينية، وIBM Plex Sans Arabic للعربية.<br>الشعار: خط واحد منضبط وخط أفق يعلو الاسم.</div>' + ftr(n))
add(identity, "dark")

# 24 التواصل
CT = [("الاسم التجاري",f"{BV} — شركة ذات مسؤولية محدودة (شخص واحد)"),("المؤسس","فهد سعد العجمي"),("الجوال",'<span class="ltr num" style="font-weight:300">0506221548</span>'),("البريد الإلكتروني",'<span class="ltr" style="font-family:Jost;font-weight:300">fd-0@hotmail.com</span>'),("المقر","الرياض، المملكة العربية السعودية"),("الرقم الوطني الموحد (السجل التجاري)",'<span class="ltr" style="font-family:Jost;font-weight:300;letter-spacing:.04em">7055194109</span>')]
def contact(n):
    cr = "".join(f'<div style="border-top:1px solid rgba(27,26,24,.13);padding:15px 0"><div class="deepc" style="font-size:19px">{a}</div><div style="font-size:31px;font-weight:400;margin-top:4px">{b}</div></div>' for a, b in CT)
    return (f'<div style="position:absolute;left:0;top:0;bottom:0;width:720px;background:var(--char);display:flex;align-items:center;justify-content:center"><div style="width:420px">{logo("A","logo","paper")}</div></div>' +
            hdr(n,"التواصل",780) + f'<div style="position:absolute;right:120px;top:180px;width:900px"><div class="lat olive" style="font-size:18px;margin-bottom:18px">Contact</div><h1 style="margin-bottom:40px">تواصل معنا</h1>{cr}</div>')
add(contact, "cream")

# 25 ختام
add(lambda n: f'<div style="position:absolute;left:0;right:0;top:300px;display:flex;justify-content:center"><div style="width:620px">{logo("A","logo","paper")}</div></div>'
    '<div style="position:absolute;left:0;right:0;top:760px;text-align:center"><h2 style="font-weight:300;font-size:56px">نصنع حضورًا يُرى ويُتذكّر</h2><div class="lat" style="margin-top:22px;font-size:18px;color:var(--olive-l)">Golden Vale · Riyadh · 2026</div></div>', "dark")

assert len(pages) == 25, len(pages)
H = html("Golden Vale — الملف التعريفي", pages)
H = H.replace("border-bottom:1px solid rgba(140,127,62,.45)", "border-bottom:none")
H = H.replace("rgba(140,127,62,", "rgba(27,26,24,").replace("rgba(184,169,94,", "rgba(237,230,216,")
H = re.sub(r"rgba\(27,26,24,\.\d+\)", "rgba(27,26,24,.13)", H)
H = re.sub(r"rgba\(237,230,216,\.\d+\)", "rgba(237,230,216,.2)", H)
H = H.replace(".rule{height:3px;width:120px;background:var(--olive)}", ".rule{display:none}")
open("build/profile25.html", "w", encoding="utf-8").write(H)
print(len(pages), "pages")
