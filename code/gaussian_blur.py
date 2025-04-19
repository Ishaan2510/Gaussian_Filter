import cv2

def apply_gaussian_blur(image_path, sigma):
    image = cv2.imread(image_path)
    blurred = cv2.GaussianBlur(image, (5, 5), sigma)  # Kernel size 5x5
    cv2.imwrite(f"../images/blurred_sigma{sigma}.jpg", blurred)

# Apply to noisy image
apply_gaussian_blur("../images/noisy_image.jpg", sigma=1)
apply_gaussian_blur("../images/noisy_image.jpg", sigma=2)
apply_gaussian_blur("../images/noisy_image.jpg", sigma=5)
apply_gaussian_blur("../images/manan.jpg", sigma=10)
