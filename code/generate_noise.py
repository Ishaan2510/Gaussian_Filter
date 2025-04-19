import cv2
import numpy as np

# Load a sample image (e.g., grayscale)
image = cv2.imread("../images/image.jpg", 0)  # Load as grayscale
manan = cv2.imread("../images/manan.jpg", 0)  # Load as grayscale

# Add salt-and-pepper noise
def add_salt_pepper(image, prob=0.05):
    noisy = np.copy(image)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = np.random.random()
            if rdn < prob:
                noisy[i][j] = 0  # Pepper
            elif rdn > thres:
                noisy[i][j] = 255  # Salt
    return noisy

noisy_image = add_salt_pepper(image)
cv2.imwrite("../images/noisy_image.jpg", noisy_image)
manan_b = add_salt_pepper(manan)
cv2.imwrite("../images/manan_bw.jpg", manan_b)
