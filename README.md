# Histogram Equalization Test

مشروع بسيط بلغة Python لعرض وتطبيق تقنيات تسوية الهيستوغرام (Histogram Equalization) على الصور باستخدام مكتبة OpenCV.

## ما يقوم به المشروع

الكود يقرأ صورة بدرجة رمادية (grayscale) ويعرض مقارنة بين ثلاث حالات:

1. **الصورة الأصلية** (Original Image) مع الهيستوغرام والدالة التراكمية (CDF)
2. **التسوية العادية** (Global Histogram Equalization) باستخدام `cv.equalizeHist()`
3. **التسوية التكيفية المُقيّدة** (CLAHE) باستخدام `cv.createCLAHE()`

يتم حفظ النتيجة كصورة في ملف `result.png` وفتحها تلقائياً.

## بنية المشروع

```
Histogram Equalization test/
├── histogram_equalization.py      # الكود الرئيسي للمعالجة والعرض
├── generate_demo_image.py         # توليد صورة تجريبية منخفضة التباين
├── demo_images/
│   └── badquality.jpg             # الصورة التجريبية المدخلة
├── result.png                     # نتيجة المعالجة (تُولد تلقائياً)
├── .gitignore
└── README.md
```

## متطلبات التشغيل

- Python 3.x
-opencv-python
- numpy
- matplotlib

للتثبيت:

```bash
pip install opencv-python numpy matplotlib
```

## طريقة التشغيل

1. تأكد من وجود صورة باسم `badquality.jpg` داخل مجلد `demo_images/`.
   (أو شغّل `generate_demo_image.py` لتوليد صورة تجريبية تلقائياً)
2. شغّل الكود الرئيسي:

```bash
python histogram_equalization.py
```

3. ستظهر نافذة بمقارنة الصور والهيستوغرامات، وسيتم حفظ النتيجة في `result.png`.

## متطلبات الرفع على GitHub

قبل الرفع، تأكد من إنشاء مستودع جديد (Repository) على GitHub ثم نفذ الأوامر التالية في مجلد المشروع:

```bash
git init
git add .
git commit -m "Initial commit: Histogram Equalization project"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO_NAME.git
git push -u origin main
```

استبدل `USERNAME` و`REPO_NAME` باسم مستخدمك واسم المستودع على GitHub."# histogram-equalization-test" 
