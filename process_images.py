# -*- coding: utf-8 -*-
"""اختيار الأفضل من أعمال الشركة وتنقيحها وقصّها لأماكنها في الملف التعريفي.
الاستعمال: python3 process_images.py <مجلد الصور الأصلية>"""
import sys, glob, os
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
files = sorted(glob.glob(os.path.join(SRC, "*.jpg")))

# (اسم الناتج, رقم الأصل بعد الفرز, (يسار, أعلى, يمين, أسفل) كنِسَب, الحجم المعروض px, رفع إضاءة gamma)
JOBS = [
 ("svc-ads",   10, (0, .094, 1, .960), (700, 1080), .88),
 ("svc-events", 7, (.136, 0, 1, 1),    (700, 1080), 1.0),
 ("svc-brand", 11, (0, .05, 1, .918),  (700, 1080), 1.0),
 ("svc-exp",    8, (0, .03, 1, .90),   (700, 1080), 1.0),
 ("overview",  12, (0, 0, 1, .995),    (560, 250),  1.0),
 ("method",     5, (0, .05, 1, .872),  (520, 760),  .90),
 ("work-1",     7, (0, .26, 1, .77),   (544, 370),  1.0),
 ("work-2",    10, (0, .24, 1, .62),   (544, 370),  .88),
 ("work-3",     8, (0, .12, 1, .50),   (544, 370),  1.0),
 ("work-4",    12, (.28, 0, .94, 1),   (544, 370),  1.0),
 ("work-5",     4, (.12, 0, .95, 1),   (544, 370),  1.0),
 ("work-6",     0, (.10, 0, .93, 1),   (544, 370),  1.0),
]
def gamma(im, g):
    lut = [round(255 * (i / 255) ** g) for i in range(256)]
    return im.point(lut * 3)
for name, idx, (l, t, r, b), (w, h), g in JOBS:
    im = ImageOps.exif_transpose(Image.open(files[idx])).convert("RGB")
    W, H = im.size
    im = im.crop((round(l*W), round(t*H), round(r*W), round(b*H)))
    # قصّ لنسبة الهدف بدقة
    tr = w / h; cr = im.width / im.height
    if cr > tr: nw = round(im.height * tr); x0 = (im.width - nw)//2; im = im.crop((x0, 0, x0+nw, im.height))
    elif cr < tr: nh = round(im.width / tr); y0 = (im.height - nh)//2; im = im.crop((0, y0, im.width, y0+nh))
    if g != 1.0: im = gamma(im, g)
    im = ImageOps.autocontrast(im, cutoff=0.4)
    im = ImageEnhance.Color(im).enhance(.94)
    im = ImageEnhance.Contrast(im).enhance(1.04)
    scale = max(w / im.width, 1.0)                     # لا تكبير إلا لبلوغ الحجم المعروض
    scale = min(scale, 1.6)
    im = im.resize((round(im.width*scale), round(im.height*scale)), Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.3, percent=55, threshold=3))
    im.save(os.path.join(OUT, f"{name}.jpg"), quality=86, optimize=True, progressive=True)
    print(f"{name:10s} <- #{idx:<2d} {os.path.basename(files[idx])[:26]:26s} -> {im.size}  (الهدف {w}x{h})")
