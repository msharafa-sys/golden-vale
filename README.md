# Golden Vale — الهوية البصرية والملف التعريفي

- `logos/` — 24 شعار SVG (3 اتجاهات × شعار/أيقونة × ملوّن/معكوس/أسود/أبيض)
- `الملف-التعريفي_جولدن-فيل_اتجاه-أ.pdf` — الملف التعريفي المعتمد (الاتجاه أ)، 15 صفحة 16:9، بصور أعمال الفريق
- `alternatives/` — الاتجاهان ب وج (بدون صور، للأرشفة)
- `images/` و`process_images.py` — الصور المنقّحة وسكربت المعالجة (`python3 process_images.py <مجلد الأصول>`)
- `دليل-الهوية_جولدن-فيل.pdf` — دليل الهوية (18 صفحة، تطبيقات لكل اتجاه)
- المصدر: `logos.py` `common.py` `profile.py` `guide.py` `render.cjs`

## إعادة البناء
```
pip install uharfbuzz fonttools
python3 logos.py && python3 guide.py && for d in A B C; do python3 profile.py $d; done
node render.cjs pdf $PWD/build/profile_A.html $PWD/الملف-التعريفي_جولدن-فيل_اتجاه-أ.pdf 1920 1080   # وكذلك B وC
node render.cjs pdf $PWD/build/guide.html $PWD/دليل-الهوية_جولدن-فيل.pdf 1920 1080
```
(يتطلب Node + Playwright وChromium؛ عدّل المسار في `render.cjs` عند الحاجة.)

## ملاحظات
- المحتوى المعلَّم `[نص مؤقت]` أو `[يُضاف]` يُستبدل بمعلومات موثّقة قبل النشر.
- قيم CMYK إرشادية وتُطابَق مع المطبعة قبل الإنتاج.
- الخطان Jost وIBM Plex Sans Arabic بترخيص OFL.
- مستودع خاص: يحوي بيانات تواصل المؤسس.
