Getting Started

1. Clone the Repository

```bash
git clone https://github.com/yourusername/gaussian-blur.git
cd gaussian-blur
```

2. Create a Virtual Environment

```bash
python -m venv venv
```

3. Activate the Virtual Environment

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

4. Install Required Libraries

```bash
pip install numpy matplotlib opencv-python
```

Usage

1. Generate a Noisy Image

Run the following script to create a synthetic noisy grayscale image:

```bash
python code/generate_noise.py
```

This will save a noisy image in the `images/` folder.

2. Apply Gaussian Blur

Run the Gaussian blur script to process the noisy image with different sigma values:

```bash
python code/gaussian_blur.py
```

This will generate blurred images (with various sigma values) in the `images/` folder.

3. Calculate PSNR

To quantitatively compare the blurred images with the original, run:

```bash
python code/psnr_calculation.py
```
