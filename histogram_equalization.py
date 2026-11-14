import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def histogram_equal():
    # تحديد مسار الصورة وقراءتها بتدرج الرمادي
    root = os.getcwd()
    image_path = os.path.join(root, 'demo_images', 'badquality.jpg')
    image = cv.imread(image_path, 0)  # 0 تعني قراءة الصورة كـ Grayscale

    if image is None:
        print(f"[ERROR] Could not load image from: {image_path}")
        print("Please place a 'badquality.jpg' image inside the 'demo_images' folder.")
        return

    # ==========================================
    # 1. الصورة الأصلية (Original Image)
    # ==========================================
    hist = cv.calcHist([image], [0], None, [256], [0, 256])
    cdf = hist.cumsum()                                    # حساب الدالة التراكمية
    cdf_norm = cdf * float(hist.max()) / cdf.max()        # تطبيع الدالة لتتناسب مع الرسم

    fig = plt.figure(figsize=(14, 7))
    fig.suptitle('Histogram Equalization Comparison', fontsize=14, fontweight='bold')

    # عرض الصورة الأصلية
    ax1 = plt.subplot(2, 3, 1)
    ax1.imshow(image, cmap='gray')
    ax1.set_title('Original Image')
    ax1.axis('off')

    # عرض المدرج التكراري للصورة الأصلية
    ax4 = plt.subplot(2, 3, 4)
    ax4.plot(hist, color='black', label='Histogram')
    ax4.plot(cdf_norm, color='blue', label='CDF')
    ax4.set_title('Original Histogram')
    ax4.set_xlabel('Pixel Intensity')
    ax4.set_ylabel('Number of Pixels')
    ax4.legend()
    ax4.set_xlim([0, 256])

    # ==========================================
    # 2. التسوية العادية (Global Histogram Equalization)
    # ==========================================
    equalize_image = cv.equalizeHist(image)

    eq_hist = cv.calcHist([equalize_image], [0], None, [256], [0, 256])
    eq_cdf = eq_hist.cumsum()
    eq_cdf_norm = eq_cdf * float(eq_hist.max()) / eq_cdf.max()

    # عرض الصورة بعد التسوية العادية
    ax2 = plt.subplot(2, 3, 2)
    ax2.imshow(equalize_image, cmap='gray')
    ax2.set_title('Global Equalization')
    ax2.axis('off')

    # عرض المدرج التكراري بعد التسوية العادية
    ax5 = plt.subplot(2, 3, 5)
    ax5.plot(eq_hist, color='black', label='Histogram')
    ax5.plot(eq_cdf_norm, color='blue', label='CDF')
    ax5.set_title('Equalized Histogram')
    ax5.set_xlabel('Pixel Intensity')
    ax5.set_ylabel('Number of Pixels')
    ax5.legend()
    ax5.set_xlim([0, 256])

    # ==========================================
    # 3. التسوية التكيفية (CLAHE)
    # ==========================================
    # إنشاء كائن CLAHE بحد أقصى 5 للتباين، وشبكة 8x8
    clahe_obj = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    clahe_image = clahe_obj.apply(image)

    clahe_hist = cv.calcHist([clahe_image], [0], None, [256], [0, 256])
    clahe_cdf = clahe_hist.cumsum()
    clahe_cdf_norm = clahe_cdf * float(clahe_hist.max()) / clahe_cdf.max()

    # عرض صورة CLAHE
    ax3 = plt.subplot(2, 3, 3)
    ax3.imshow(clahe_image, cmap='gray')
    ax3.set_title('CLAHE')
    ax3.axis('off')

    # عرض المدرج التكراري لـ CLAHE
    ax6 = plt.subplot(2, 3, 6)
    ax6.plot(clahe_hist, color='black', label='Histogram')
    ax6.plot(clahe_cdf_norm, color='blue', label='CDF')
    ax6.set_title('CLAHE Histogram')
    ax6.set_xlabel('Pixel Intensity')
    ax6.set_ylabel('Number of Pixels')
    ax6.legend()
    ax6.set_xlim([0, 256])

    plt.tight_layout()

    # حفظ النتيجة كصورة وفتحها تلقائياً
    output_path = os.path.join(root, 'result.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.show()
    print(f"Result saved to: {output_path}")

    # فتح الصورة تلقائياً بمشاهد الصور الافتراضي
    import subprocess
    subprocess.Popen(['start', output_path], shell=True)


if __name__ == '__main__':
    histogram_equal()
