# Golden Vale — الهوية البصرية والملف التعريفي وعروض الأسعار

- `Golden-Vale_Company-Profile_25-pages.pdf` — الملف التعريفي الموسّع (25 صفحة) — `profile25.py`، وأمر إعادة إنشائه في `PROMPT_company-profile-25.md`
- `Golden-Vale_Company-Profile.pdf` — النسخة المختصرة (14 صفحة)
- `Golden-Vale_Brand-Guidelines.pdf` — دليل الهوية (الاتجاهان أ وب)
- `Golden-Vale_Quotation_GV-2026-0105.pdf` — عرض السعر، و`Golden-Vale_Quotation-Template.pdf` قالب فارغ
- `logos/` — شعارات SVG (اتجاهان × شعار/أيقونة × ملوّن/معكوس/أسود/أبيض)
- `quotes/*.json` بيانات العروض، و`quote.py` المولّد (`python3 quote.py quotes/X.json build/x.html`)
- المصدر: `logos.py` `common.py` `profile.py` `guide.py` `process_photos.py` `render.cjs`

- `clients.json` — قائمة العملاء للصفحة 21: لا يظهر اسم إلا مع `consent: true` (موافقة كتابية)

- `print/` — حزمة الطباعة (بطاقة، ورق رسمي، مظروف، ورقة تعريف، بطاقة موظف، غلاف مجلد، صور رمزية، توقيع بريد) + `print/cmyk/` + `README-print.md`
- `cards.json` بيانات البطاقات، و`stationery.py` مولّد مقتنيات الهوية

## قواعد ثابتة
- اسم الشركة في كل مستند: **Golden Vale** (لاتينيًا فقط، بلا ترجمة عربية).
- لا اسم للمالك في عروض الأسعار.
- بلا خطوط ذهبية في الملف التعريفي؛ كل المستندات من اليمين إلى اليسار.

## إعادة البناء
```
pip install uharfbuzz fonttools
python3 logos.py && python3 guide.py && python3 profile.py A
node render.cjs pdf $PWD/build/profile_A.html $PWD/Golden-Vale_Company-Profile.pdf 1920 1080
node render.cjs pdf $PWD/build/guide.html $PWD/Golden-Vale_Brand-Guidelines.pdf 1920 1080
python3 quote.py quotes/GV-2026-0105.json build/quote_0105.html
node render.cjs pdf $PWD/build/quote_0105.html $PWD/Golden-Vale_Quotation_GV-2026-0105.pdf 794 1123
```
(يتطلب Node + Playwright وChromium.)

## ملاحظات
- `[نص مؤقت]` و`[صورة — تُضاف لاحقًا]` تُستبدل بمعلومات وصور موثّقة قبل النشر.
- قيم CMYK إرشادية وتُطابَق مع المطبعة.
- الخطان Jost وIBM Plex Sans Arabic بترخيص OFL. مستودع خاص (بيانات تواصل).
