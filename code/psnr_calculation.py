# code/psnr_calculation.py
import cv2
import numpy as np
import math

def psnr(original, processed):
    mse = np.mean((original - processed) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    return 20 * math.log10(max_pixel / math.sqrt(mse))

original = cv2.imread("../images/image.jpg", 0)
blurred_sigma1 = cv2.imread("../images/blurred_sigma1.jpg", 0)
print(f"PSNR (σ=1): {psnr(original, blurred_sigma1):.2f} dB")
blurred_sigma2 = cv2.imread("../images/blurred_sigma2.jpg", 0)
print(f"PSNR (σ=2): {psnr(original, blurred_sigma2):.2f} dB")
blurred_sigma5 = cv2.imread("../images/blurred_sigma5.jpg", 0)
print(f"PSNR (σ=5): {psnr(original, blurred_sigma5):.2f} dB")
