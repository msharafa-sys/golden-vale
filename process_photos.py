# -*- coding: utf-8 -*-
"""قصّ وتنقية صور الملف التعريفي المرسلة من المؤسس (مصدرها غير موثّق: مخزنة/مولّدة).
الاستعمال: python3 process_photos.py <مجلد المصادر>  (يتوقع 4.jpg ... 8.jpg)"""
import sys, os
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(OUT, exist_ok=True)
# (الناتج, المصدر, (يسار, أعلى, يمين, أسفل) كنِسَب, الحجم المعروض px)
JOBS = [
 ("svc-ads",    "5.jpg", (0.03, 0.00, 0.94, 1.00), (880, 540)),   # واجهة محل
 ("svc-events", "4.jpg", (0.00, 0.00, 0.91, 1.00), (880, 540)),   # مسرح وإضاءة (بلا علامة المولّد أسفل اليمين)
 ("svc-brand",  "8.jpg", (0.00, 0.05, 1.00, 0.97), (880, 540)),   # صالة استقبال
 ("svc-exp",    "6.jpg", (0.00, 0.00, 1.00, 0.976), (880, 540)),  # منصة عرض
 ("overview",   "4.jpg", (0.00, 0.17, 0.93, 0.93), (560, 250)),
 ("method",     "7.jpg", (0.42, 0.00, 0.876, 1.00), (520, 760)),
]
for name, f, (l, t, r, b), (w, h) in JOBS:
    im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, f))).convert("RGB")
    W, H = im.size
    im = im.crop((round(l*W), round(t*H), round(r*W), round(b*H)))
    tr, cr = w / h, im.width / im.height
    if cr > tr: nw = round(im.height*tr); x0 = (im.width-nw)//2; im = im.crop((x0, 0, x0+nw, im.height))
    elif cr < tr: nh = round(im.width/tr); y0 = (im.height-nh)//2; im = im.crop((0, y0, im.width, y0+nh))
    im = ImageOps.autocontrast(im, cutoff=0.3)
    im = ImageEnhance.Contrast(im).enhance(1.03)
    scale = min(max(w / im.width, 1.0), 1.25)          # تكبير طفيف فقط عند الضرورة
    if scale > 1.0: im = im.resize((round(im.width*scale), round(im.height*scale)), Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=45, threshold=3))
    im.save(os.path.join(OUT, f"{name}.jpg"), quality=88, optimize=True, progressive=True)
    print(f"{name:10s} <- {f} -> {im.size} (هدف {w}x{h}){'  ⚠ دقة أقل من المعروض' if im.width < w else ''}")
