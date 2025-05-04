````markdown
# 🌫️ Gaussian Filter in Image Processing

[![License: MIT](https://img.shields.io/github/license/chetangadhiya4939/Fork_Gaussian_Filter)](LICENSE)
[![Stars](https://img.shields.io/github/stars/chetangadhiya4939/Fork_Gaussian_Filter?style=social)](https://github.com/chetangadhiya4939/Fork_Gaussian_Filter/stargazers)
[![Forks](https://img.shields.io/github/forks/chetangadhiya4939/Fork_Gaussian_Filter?style=social)](https://github.com/chetangadhiya4939/Fork_Gaussian_Filter/network/members)

> **A simple but powerful Python implementation of the Gaussian Blur filter for image smoothing, denoising, and pre-processing in computer vision.**

---

## 🖼️ Demo

### 🔍 Original Image
<img src="https://via.placeholder.com/400x250.png?text=Original+Image" width="400"/>

### 🌫️ Gaussian Filter Applied
<img src="https://via.placeholder.com/400x250.png?text=Blurred+Image" width="400"/>

> Replace these with your actual input and output images for better impact.

---

## 🎯 What is a Gaussian Filter?

The **Gaussian Filter** is used to blur images and remove noise and detail. It uses the **Gaussian function** to calculate the transformation to apply to each pixel and its neighbors.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/3b/Kernel_Gaussian_3x3.svg" width="200" alt="Gaussian Kernel Matrix"/>
</p>

---

## ✨ Features

- 🧮 Customizable Kernel Size & Sigma
- 🖥️ Written in Python using OpenCV & NumPy
- 📉 Reduces image noise and detail
- 📷 Works on color and grayscale images

---

## 🧠 How It Works

1. Convert image to grayscale (optional).
2. Apply a Gaussian filter to smooth the image.
3. Display or save the blurred output.

---

## 🚀 Installation

Clone this repo:

```bash
git clone https://github.com/chetangadhiya4939/Fork_Gaussian_Filter.git
cd Fork_Gaussian_Filter
````

Install dependencies:

```bash
pip install numpy opencv-python
```

---

## ▶️ Usage

```bash
python gaussian_filter.py
```

You can modify the `kernel_size` and `sigma` in the script:

```python
blurred_image = cv2.GaussianBlur(image, (5, 5), 1.5)
```

---

## 📁 Project Structure

```
Fork_Gaussian_Filter/
├── gaussian_filter.py      # Main script
├── input.jpg               # Sample input image
├── output.jpg              # Filtered output image
├── README.md               # This file
└── LICENSE
```

---

## 🔬 Use Cases

* Pre-processing in computer vision
* Edge detection
* Image denoising
* Artistic blur effects

---

## 📈 Future Enhancements

* [ ] Add GUI using Tkinter
* [ ] Add interactive parameter tuning (trackbars)
* [ ] Integrate video stream filtering

---

## 🧑‍💻 Author

**Chetan Gadhiya**
📫 [LinkedIn](https://linkedin.com/in/chetangadhiya)
🌐 [GitHub Profile](https://github.com/chetangadhiya4939)

---

## 🌟 Show Your Support

If you found this project useful, please ⭐ the repo and share it with others!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

```
