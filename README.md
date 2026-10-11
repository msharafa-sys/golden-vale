# Golden Vale — الهوية البصرية والملف التعريفي

- `logos/` — 24 شعار SVG (3 اتجاهات × شعار/أيقونة × ملوّن/معكوس/أسود/أبيض)
- `الملف-التعريفي_جولدن-فيل.pdf` — ملف تعريفي 14 صفحة 16:9
- `دليل-الهوية_جولدن-فيل.pdf` — دليل الهوية
- المصدر: `logos.py` `common.py` `profile.py` `guide.py` `render.cjs`

## إعادة البناء
```
pip install uharfbuzz fonttools
python3 logos.py && python3 profile.py && python3 guide.py
node render.cjs pdf $PWD/build/profile.html $PWD/الملف-التعريفي_جولدن-فيل.pdf 1920 1080
node render.cjs pdf $PWD/build/guide.html $PWD/دليل-الهوية_جولدن-فيل.pdf 1920 1080
```
(يتطلب Node + Playwright وChromium؛ عدّل المسار في `render.cjs` عند الحاجة.)

## ملاحظات
- المحتوى المعلَّم `[نص مؤقت]` أو `[يُضاف]` يُستبدل بمعلومات موثّقة قبل النشر.
- قيم CMYK إرشادية وتُطابَق مع المطبعة قبل الإنتاج.
- الخطان Jost وIBM Plex Sans Arabic بترخيص OFL.
- مستودع خاص: يحوي بيانات تواصل المؤسس.
