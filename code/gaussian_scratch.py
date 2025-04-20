import numpy as np
import time
import cv2

# cv2 is in 3.12.4 appdata-- now installed in global

def create_2d_gaussian_kernel(sigma, size=None):
    """Non-optimized 2D Gaussian kernel creation"""
    if size is None:
        size = int(6 * sigma + 1)
        size = size if size % 2 else size + 1
    else:
        size = size if size % 2 else size + 1
    
    ax = np.linspace(-(size-1)//2, (size-1)//2, size)
    x, y = np.meshgrid(ax, ax)
    
    kernel = np.exp(-(x**2 + y**2)/(2 * sigma**2))
    kernel /= kernel.sum()
    return kernel


def non_optimized_gaussian_blur(img, sigma):
    """Naive O(n²) convolution implementation"""
    kernel = create_2d_gaussian_kernel(sigma)
    k_size = kernel.shape[0]
    pad = k_size // 2
    
    # Add padding
    img_pad = np.pad(img, pad, mode='reflect')
    
    # Initialize output
    output = np.zeros_like(img)
    
    # Convolution loops
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            output[i,j] = np.sum(
                kernel * img_pad[i:i+k_size, j:j+k_size]
            )
    
    return output


def optimized_gaussian_blur(img, sigma):
    """Optimized separable O(2n) implementation"""
    # Create 1D kernel
    size = int(6 * sigma + 1)
    size = size if size % 2 else size + 1
    ax = np.arange(-size//2 + 1, size//2 + 1)
    kernel = np.exp(-ax**2/(2 * sigma**2))
    kernel /= kernel.sum()

    # Horizontal pass
    blurred = np.apply_along_axis(
        lambda r: np.convolve(r, kernel, mode='same'),
        axis=1,
        arr=img
    )

    # Vertical pass
    blurred = np.apply_along_axis(
        lambda c: np.convolve(c, kernel, mode='same'),
        axis=0,
        arr=blurred
    )

    # check datatype 
    print(blurred.dtype)
    return blurred.astype(img.dtype)


# Benchmarking and validation
if __name__ == "__main__":
    # Test image (grayscale)
    img = cv2.imread('mario.jpg', cv2.IMREAD_GRAYSCALE).astype(np.float32)/255
    print(f"image shape (grayscale) {img.shape}")
    print(f"image dtype (grayscale) {img.dtype}")
    img_for_cv2 = cv2.imread('mario.jpg')

    print("=== image info from cv2 ===")
    print(f"image shape {img_for_cv2.shape}")
    print(f"image dtype {img_for_cv2.dtype}")
    
    print("=== Performance Comparison ===")
    
    # Non-optimized
    start = time.perf_counter()
    naive_blur = non_optimized_gaussian_blur(img, sigma=10)
    print(f"2D convolution: {time.perf_counter()-start:.2f}s")

    # Optimized
    start = time.perf_counter()
    sep_blur = optimized_gaussian_blur(img, sigma=10)
    print(f"Separable convolution: {time.perf_counter()-start:.2f}s")

    # OpenCV reference
    start = time.perf_counter()
    # the below is for grayscale conversion
    cv_blur = cv2.GaussianBlur(img, (0,0), sigmaX=10)
    # the below is for coloured conversion
    # cv_blur = cv2.GaussianBlur(img_for_cv2, (0,0), sigmaX=10)
    print(f"OpenCV optimized: {time.perf_counter()-start:.2f}s")

    # Validation
    print("\n=== Accuracy Check ===")
    print(f"Naive vs OpenCV MSE: {np.mean((naive_blur - cv_blur)**2):.6f}")
    print(f"Separable vs OpenCV MSE: {np.mean((sep_blur - cv_blur)**2):.6f}")

    # Save results
    cv2.imwrite('naive_blur.jpg', (naive_blur*255).astype(np.uint8))
    # cv2.imwrite('sep_blur.jpg', sep_blur*255)
    cv2.imwrite('sep_blur.jpg', (sep_blur*255).astype(np.uint8))
    # cv2.imwrite('cv2_blur.jpg', cv_blur)
