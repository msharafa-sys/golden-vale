# -*- coding: utf-8 -*-
from common import *
import sys
D = sys.argv[1] if len(sys.argv)>1 else "A"
LETTER = {"A":"أ","B":"ب","C":"ج"}[D]
COVER = {"A":(760,230),"B":(560,200),"C":(600,170)}[D]
CONTACT_W = {"A":440,"B":340,"C":420}[D]

PH_NOTE = "[نص مؤقت]"
def hdr(n, section, left=120):
    return f'<div class="hdr" style="left:{left}px"><span class="lat">Golden Vale · {n:02d}</span><span>{section}</span></div>'
def ftr(n, left=120):
    return f'<div class="ftr" style="left:{left}px"><span class="lat" style="font-size:14px">Company Profile · Riyadh · 2026</span><span class="num" style="font-size:20px">{n:02d}</span></div>'

pages = []

# 01 غلاف
pages.append(f'''<div class="page dark">
 <div style="position:absolute;inset:0">{art("valley",1920,1080,"#B8A95E",op=.16)}</div>
 <div style="position:absolute;left:0;right:0;top:{COVER[1]}px;display:flex;justify-content:center"><div style="width:{COVER[0]}px">{logo(D,"logo","reverse")}</div></div>
 <div style="position:absolute;left:0;right:0;top:760px;text-align:center">
   <div class="rule" style="margin:0 auto 34px"></div>
   <h2 style="font-weight:300;font-size:64px">الملف التعريفي للشركة</h2>
   <div class="lat" style="margin-top:26px;font-size:20px;color:var(--olive-l)">Company Profile · Riyadh · 2026</div></div>
</div>''')

# 02 المحتويات
items = [("نظرة عامة","Overview",3),("كلمة رئيس مجلس الإدارة","Chairman's Message",4),("الرؤية والرسالة","Vision & Mission",5),("القيم الجوهرية","Core Values",6),
         ("خدماتنا","Services",7),("نماذج من أعمال الفريق","Portfolio",11),("منهجية العمل","How We Work",12),("لماذا جولدن فيل","Why Golden Vale",13),("العملاء والشركاء","Clients & Partners",14),("التواصل","Contact",15)]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:28px;border-top:1px solid rgba(140,127,62,.4);padding:6px 0"><span class="num olive" style="font-size:28px;width:70px">{i+1:02d}</span><span style="font-size:29px;font-weight:400;flex:1">{a}</span><span class="lat" style="font-size:14px;color:var(--deep)">{b}</span><span class="num" style="font-size:24px;width:50px;text-align:left">{p:02d}</span></div>' for i,(a,b,p) in enumerate(items))
pages.append(f'''<div class="page">{hdr(2,"المحتويات",620)}
 <div style="position:absolute;right:120px;top:150px;width:1000px"><h1>المحتويات</h1><div class="rule" style="margin:18px 0 14px"></div>{rows}</div>
 <div style="position:absolute;left:0;top:0;bottom:0;width:560px;background:var(--char)">{art("beams",560,1080,"#B8A95E",op=.35)}</div>{ftr(2,620)}</div>''')

# 03 نظرة عامة
facts = [("التأسيس","2026"),("المقر","الرياض، المملكة العربية السعودية"),("المجال","الدعاية والإعلان وتنظيم الفعاليات"),("السجل التجاري","[رقم السجل التجاري — يُضاف]")]
fx = "".join(f'<div style="display:flex;justify-content:space-between;border-top:1px solid rgba(140,127,62,.4);padding:16px 0;font-size:23px"><span class="deepc" style="font-weight:500">{a}</span><span style="font-weight:300">{b}</span></div>' for a,b in facts)
pages.append(f'''<div class="page">{hdr(3,"نظرة عامة")}
 <div style="position:absolute;right:120px;top:190px;width:980px"><div class="lat olive" style="font-size:18px;margin-bottom:22px">Overview</div>
  <h1>وكالة سعودية للدعاية والإعلان وتنظيم الفعاليات</h1><div class="rule" style="margin:34px 0"></div>
  <p>تأسست جولدن فيل عام 2026 في الرياض لتقدّم للعلامات التجارية والجهات حلولًا متكاملة في الدعاية والإعلان وتنظيم الفعاليات وإدارة الهوية البصرية وتصميم التجارب الإبداعية، عبر نقطة اتصال واحدة من الفكرة حتى التسليم.</p>
  <p style="margin-top:14px" class="small deepc">{PH_NOTE} نموذج التنفيذ (فريق داخلي، أو شركاء إنتاج معتمدون، أو كلاهما) يُحدَّد قبل الاعتماد النهائي.</p></div>
 <div style="position:absolute;left:120px;top:210px;width:560px;background:var(--cream);padding:34px 40px">{fx}</div>
 <div style="position:absolute;left:120px;top:700px;width:560px;height:250px;overflow:hidden"><img src="../images/overview.jpg" style="width:100%;height:100%;object-fit:cover;display:block"><span class="tag" style="left:0;bottom:0">جناح معرض</span></div>{ftr(3)}</div>''')

# 04 كلمة رئيس مجلس الإدارة
pages.append(f'''<div class="page cream">
 <div class="ph" style="position:absolute;left:0;top:0;bottom:0;width:640px;border:none;border-right:2px dashed rgba(140,127,62,.7);background:var(--stone)">[صورة رئيس مجلس الإدارة — تُضاف لاحقًا]</div>
 <div style="position:absolute;right:120px;top:130px;width:1000px">
  <div class="lat olive" style="font-size:18px;margin-bottom:34px">Chairman's Message</div>
  <div class="rule" style="width:90px"></div>
  <h2 style="font-weight:400;font-size:52px;line-height:1.55;margin-top:40px">نؤمن أن لكل علامة حضورًا يستحق أن يُصنع بعناية، وأن الفعالية الناجحة تبدأ بفكرة واضحة وتنتهي بتسليم منضبط.</h2>
  <p style="margin-top:36px;font-size:25px">تنطلق جولدن فيل في مرحلة يشهد فيها قطاع الفعاليات والترفيه في المملكة نموًا متسارعًا ضمن مستهدفات رؤية 2030. ونلتزم بأن نكون شريكًا يُعتمد عليه في الجودة والمواعيد والشفافية، وببناء كل علاقة مع عملائنا على الثقة والنتائج.</p>
  <div style="border-top:1px solid rgba(140,127,62,.5);margin-top:44px;padding-top:26px"><h3>فهد سعد العجمي</h3><div class="deepc" style="font-size:22px;margin-top:4px">المؤسس ورئيس مجلس الإدارة</div>
  <div class="small deepc" style="margin-top:14px;opacity:.85">{PH_NOTE} مسودة للمراجعة والاعتماد من الأستاذ فهد سعد العجمي قبل النشر.</div></div></div></div>''')

# 05 الرؤية والرسالة
pages.append(f'''<div class="page dark">{hdr(5,"الرؤية والرسالة")}
 <div style="position:absolute;inset:0;opacity:.7">{art("beams",1920,1080,"#B8A95E",op=.12)}</div>
 <div style="position:absolute;right:120px;top:260px;width:720px"><div class="lat" style="color:var(--olive-l);font-size:18px">Vision</div><h1 style="margin:22px 0 30px;color:var(--cream)">رؤيتنا</h1><div class="rule"></div>
   <p style="margin-top:36px;font-size:32px;line-height:1.9">أن نكون الشريك الأول للعلامات والجهات في المملكة لصناعة حضور لا يُنسى.</p></div>
 <div style="position:absolute;left:50%;top:230px;bottom:200px;width:1px;background:rgba(184,169,94,.5)"></div>
 <div style="position:absolute;left:120px;top:260px;width:720px"><div class="lat" style="color:var(--olive-l);font-size:18px">Mission</div><h1 style="margin:22px 0 30px;color:var(--cream)">رسالتنا</h1><div class="rule"></div>
   <p style="margin-top:36px;font-size:32px;line-height:1.9">تحويل أهداف عملائنا إلى حملات وفعاليات متقنة، عبر منهجية واضحة تجمع الفكرة والتصميم والإنتاج والتشغيل.</p></div>{ftr(5)}</div>''')

# 06 القيم
vals = [("الإبداع","أفكار تلفت الانتباه وتخدم هدف العميل."),("الإتقان","عناية بالتفاصيل في كل مرحلة، من الفكرة إلى التسليم."),("الالتزام","جداول معتمدة وتسليم في الموعد."),("المرونة","نتكيّف مع المتغيرات وتغيّر المتطلبات."),("الشراكة","نجاح العميل هو مقياس نجاحنا.")]
cards = "".join(f'<div style="flex:1;background:{"var(--char)" if i==4 else "#fff"};color:{"var(--cream)" if i==4 else "var(--char)"};border-top:3px solid var(--olive);padding:34px 30px;height:470px"><div class="num" style="font-size:44px;color:{"var(--olive-l)" if i==4 else "var(--olive)"}">{i+1:02d}</div><h3 style="margin:90px 0 14px;font-size:38px">{a}</h3><p style="font-size:22px;line-height:1.8">{b}</p></div>' for i,(a,b) in enumerate(vals))
pages.append(f'''<div class="page">{hdr(6,"القيم الجوهرية")}
 <div style="position:absolute;right:120px;top:180px"><div class="lat olive" style="font-size:18px;margin-bottom:20px">Core Values</div><h1>قيمنا الجوهرية</h1></div>
 <div style="position:absolute;left:120px;right:120px;top:430px;display:flex;gap:26px">{cards}</div>{ftr(6)}</div>''')

# 07-10 الخدمات
svcs = [("01","Advertising","الدعاية والإعلان","حملات تبدأ من الفكرة وتنتهي بالأثر، عبر قنوات تصل إلى جمهورك في المكان والوقت المناسبين.",["حملات إعلانية متكاملة","إعلانات الطرق واللوحات","الإعلانات الرقمية","إنتاج المحتوى المرئي"],"valley",False),
 ("02","Events","تنظيم الفعاليات","من الفكرة إلى الافتتاح، ندير كل مرحلة بدقة لتقديم فعاليات منظمة وتجربة تُرضي الحضور.",["المؤتمرات والملتقيات","الفعاليات المؤسسية والموسمية","حفلات الإطلاق","الإنتاج والإضاءة والصوت"],"beams",True),
 ("03","Brand Identity","إدارة الهوية البصرية","هوية متسقة في كل نقطة تماس، من اللوحة إلى الهدية إلى الزي الموحد.",["تصميم الهوية البصرية","المطبوعات والتغليف","اللوحات والواجهات","الزي الموحد والهدايا"],"tri",False),
 ("04","Creative Experiences","التجارب الإبداعية","تجارب تفاعلية تجعل الزائر جزءًا من حكاية علامتك.",["المعارض والأجنحة","التفعيلات التفاعلية","مناطق التصوير","التجارب الرقمية"],"grid",True)]
IMGS = [("svc-ads","لوحة مضيئة — تركيب ليلي"),("svc-events","بوابة فعالية موسمية"),("svc-brand","زي موحد للمتطوعين"),("svc-exp","جناح معرض")]
for k,(n,en,ar,desc,subs,kind,dk) in enumerate(svcs):
    pg = 7+k
    boxes = "".join(f'<div style="border:1.5px solid {"rgba(184,169,94,.7)" if dk else "rgba(140,127,62,.6)"};padding:26px 28px;font-size:25px;font-weight:400;background:{"transparent" if dk else "var(--cream)"}">{s}</div>' for s in subs)
    pages.append(f'''<div class="page {"dark" if dk else ""}">{hdr(pg,"خدماتنا",760)}
 <div style="position:absolute;left:0;top:0;bottom:0;width:700px;background:var(--char);overflow:hidden"><img src="../images/{IMGS[k][0]}.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block">
   <div style="position:absolute;left:0;right:0;bottom:0;height:260px;background:linear-gradient(0deg,rgba(27,26,24,.85),rgba(27,26,24,0))"></div>
   <div style="position:absolute;left:0;right:0;top:0;height:3px;background:var(--olive)"></div>
   <div style="position:absolute;left:36px;bottom:46px;color:var(--cream);font-size:22px;font-weight:400">{IMGS[k][1]}</div></div>
 <div style="position:absolute;right:120px;top:180px;width:960px">
   <div style="display:flex;align-items:baseline;gap:26px"><span class="num" style="font-size:96px;color:{"var(--olive-l)" if dk else "var(--olive)"}">{n}</span><span class="lat" style="font-size:18px;color:{"var(--olive-l)" if dk else "var(--olive)"}">{en}</span></div>
   <h1 style="margin:26px 0 26px">{ar}</h1><div class="rule"></div>
   <p style="margin:34px 0 56px;font-size:29px">{desc}</p>
   <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px">{boxes}</div></div>{ftr(pg,760)}</div>''')

# معرض الأعمال
WORKS = [('work-1', 'بوابة فعالية موسمية', ''), ('work-2', 'لوحة مضيئة — تركيب ليلي', ''), ('work-3', 'جناح معرض — إعلان معلّق', ''), ('work-4', 'جناح معرض', ''), ('work-5', 'مجسّم كبير — مرحلة التركيب', ''), ('', 'مكان لعمل منفذ إضافي', 'PH')]
tiles = "".join(f'<div><div style="position:relative;height:280px;overflow:hidden;background:var(--char)">' + (f'<img src="../images/{n}.jpg" style="width:100%;height:100%;object-fit:cover;display:block">' if n else '<div class="ph" style="width:100%;height:100%;background:var(--cream)">[صورة عمل منفذ — تُضاف لاحقًا]</div>') + f'</div><div style="border-top:3px solid var(--olive);padding:10px 0 0;font-size:22px;font-weight:400">{t}</div></div>' for n,t,c in WORKS)
pages.append(f'''<div class="page">{hdr(11,"نماذج من أعمال الفريق")}
 <div style="position:absolute;right:120px;top:160px"><div class="lat olive" style="font-size:18px;margin-bottom:12px">Portfolio</div><h1 style="font-size:60px">نماذج من أعمال الفريق</h1></div>
 <div class="small deepc" style="position:absolute;left:120px;top:200px;font-size:17px;max-width:700px;text-align:left">[ملاحظة داخلية: تُنشر الأعمال وما يظهر فيها من أسماء وشعارات بموافقة أصحابها الكتابية.]</div>
 <div style="position:absolute;left:120px;right:120px;top:310px;display:grid;grid-template-columns:repeat(3,1fr);gap:26px 24px">{tiles}</div>{ftr(11)}</div>''')

# 11 منهجية العمل
steps = [("الاستماع","نفهم هدفك وجمهورك وميزانيتك."),("التصور","نقدّم الفكرة والتصاميم وعرض السعر."),("التنفيذ","إنتاج وتشغيل بإشراف مباشر."),("المتابعة","قياس الأثر وتقرير ختامي.")]
st = "".join(f'<div style="display:flex;align-items:center;gap:44px;border-top:1px solid rgba(140,127,62,.5);padding:24px 0"><span class="num olive" style="font-size:64px;width:130px">{i+1:02d}</span><div><h3 style="font-size:40px">{a}</h3><p class="small" style="font-size:24px;line-height:1.6">{b}</p></div></div>' for i,(a,b) in enumerate(steps))
pages.append(f'''<div class="page">{hdr(12,"منهجية العمل")}
 <div style="position:absolute;right:120px;top:180px;width:1000px"><div class="lat olive" style="font-size:18px;margin-bottom:20px">How We Work</div><h1>آلية العمل</h1><div style="margin-top:34px">{st}</div></div>
 <div style="position:absolute;left:120px;top:190px;width:520px;height:760px;background:var(--char);overflow:hidden"><img src="../images/method.jpg" style="width:100%;height:100%;object-fit:cover;display:block"><div style="position:absolute;left:0;right:0;top:0;height:3px;background:var(--olive)"></div><div style="position:absolute;left:0;right:0;bottom:0;height:150px;background:linear-gradient(0deg,rgba(27,26,24,.85),rgba(27,26,24,0))"></div><div style="position:absolute;left:28px;bottom:28px;color:var(--cream);font-size:21px">تركيب لوحة مضيئة في الموقع</div></div>{ftr(12)}</div>''')

# 12 لماذا
why = [("نقطة اتصال واحدة","تصميم وإنتاج وتشغيل تحت إدارة واحدة."),("فكرة أصيلة","مفاهيم مستوحاة من هوية العلامة والمكان."),("التزام بالمواعيد","جداول معتمدة ومتابعة مستمرة."),("شفافية التسعير","عروض أسعار مفصلة ونطاق عمل واضح."),("جودة التنفيذ","خامات ومعايير إنتاج محددة سلفًا."),("دعم مستمر","متابعة قبل الفعالية وخلالها وبعدها.")]
wc = "".join(f'<div style="background:#fff;border-top:3px solid var(--olive);padding:34px 34px;height:285px"><div class="num olive" style="font-size:30px">{i+1:02d}</div><h3 style="margin:30px 0 10px;font-size:34px">{a}</h3><p style="font-size:22px;line-height:1.7">{b}</p></div>' for i,(a,b) in enumerate(why))
pages.append(f'''<div class="page cream">{hdr(13,"لماذا جولدن فيل")}
 <div style="position:absolute;right:120px;top:170px"><div class="lat olive" style="font-size:18px;margin-bottom:18px">Why Golden Vale</div><h1>لماذا جولدن فيل</h1></div>
 <div style="position:absolute;left:120px;right:120px;top:400px;display:grid;grid-template-columns:repeat(3,1fr);gap:22px">{wc}</div>{ftr(13)}</div>''')

# 13 العملاء
cl = "".join('<div class="ph" style="height:170px;font-size:19px">شعار العميل<br>[يُضاف]</div>' for _ in range(12))
pages.append(f'''<div class="page dark">{hdr(14,"العملاء والشركاء")}
 <div style="position:absolute;right:120px;top:170px;width:1500px"><div class="lat" style="color:var(--olive-l);font-size:18px;margin-bottom:18px">Clients & Partners</div><h1 style="color:var(--cream)">عملاؤنا وشركاؤنا</h1>
  <p class="small" style="margin-top:14px;color:var(--olive-l)">[تُضاف الشعارات بعد الحصول على موافقة كل عميل كتابيًا، ولا يُنشر أي اسم قبل ذلك.]</p></div>
 <div style="position:absolute;left:120px;right:120px;top:410px;display:grid;grid-template-columns:repeat(6,1fr);gap:20px">{cl}</div>{ftr(14)}</div>''')

# 14 التواصل
ct = [("المؤسس","فهد سعد العجمي"),("الجوال",'<span class="ltr num" style="font-weight:300">0506221548</span>'),("البريد الإلكتروني",'<span class="ltr" style="font-family:Jost;font-weight:300">fd-0@hotmail.com</span>'),("المقر","الرياض، المملكة العربية السعودية"),("السجل التجاري","[رقم السجل التجاري — يُضاف]")]
cr = "".join(f'<div style="border-top:1px solid rgba(140,127,62,.5);padding:20px 0"><div class="deepc" style="font-size:19px">{a}</div><div style="font-size:34px;font-weight:400;margin-top:6px">{b}</div></div>' for a,b in ct)
pages.append(f'''<div class="page cream">{hdr(15,"التواصل",780)}
 <div style="position:absolute;right:120px;top:180px;width:900px"><div class="lat olive" style="font-size:18px;margin-bottom:18px">Contact</div><h1 style="margin-bottom:40px">تواصل معنا</h1>{cr}</div>
 <div style="position:absolute;left:0;top:0;bottom:0;width:720px;background:var(--char);display:flex;align-items:center;justify-content:center">
   <div style="position:absolute;inset:0">{art("valley",720,1080,"#B8A95E",op=.18)}</div>
   <div style="width:{CONTACT_W}px;position:relative">{logo(D,"logo","reverse")}</div></div></div>''')

open(f"build/profile_{D}.html","w",encoding="utf-8").write(html("جولدن فيل — الملف التعريفي", pages))
print(len(pages), "pages")
