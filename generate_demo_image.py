"""
Generate a synthetic low-contrast grayscale image to use as demo input.
Saves it to demo_images/badquality.jpg.
"""
import numpy as np
import cv2 as cv
import os

os.makedirs('demo_images', exist_ok=True)

# Create a 400x400 synthetic low-contrast image
# Pixel values constrained to a narrow range [80, 160] to simulate poor quality
rng = np.random.default_rng(42)
base = rng.integers(80, 160, size=(400, 400), dtype=np.uint8)

# Add some structure: circles and gradients
x, y = np.meshgrid(np.arange(400), np.arange(400))
gradient = ((x + y) / (400 + 400) * 60).astype(np.uint8)  # range ~0-60
base = np.clip(base.astype(np.int16) + gradient - 20, 70, 170).astype(np.uint8)

# Draw faint circular blobs
for cx, cy, r in [(100, 100, 60), (300, 150, 80), (200, 300, 100), (350, 330, 50)]:
    mask = (x - cx) ** 2 + (y - cy) ** 2 < r ** 2
    base[mask] = np.clip(base[mask].astype(np.int16) + 20, 70, 170).astype(np.uint8)

# Apply slight Gaussian blur to simulate real-world blur
base = cv.GaussianBlur(base, (5, 5), 1.5)

cv.imwrite(os.path.join('demo_images', 'badquality.jpg'), base)
print("Demo image saved to demo_images/badquality.jpg")
