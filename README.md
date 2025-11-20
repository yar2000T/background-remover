# AI Background Remover
 
![Python Version](https://img.shields.io/badge/Python-3.10+-blue?style=flat) [![Build EXE](https://github.com/yar2000T/background-remover/actions/workflows/build.yml/badge.svg)](https://github.com/yar2000T/background-remover/actions/workflows/build.yml) [![Release EXE](https://github.com/yar2000T/background-remover/actions/workflows/build_release.yml/badge.svg)](https://github.com/yar2000T/background-remover/actions/workflows/build_release.yml)

A **modern AI-powered background remover** built with Python. Remove image backgrounds easily and save results as transparent PNG. Features a **sleek dark-themed UI**, auto-scaling previews, and easy-to-use buttons.

---

## Features

* 🌟 Remove background from any image (PNG, JPG, JPEG, BMP, WEBP)
* 🎨 Modern dark-themed Tkinter UI
* 📐 Auto-scaled image previews with preserved aspect ratio
* 💾 Save results as transparent PNG
* 🖱️ Load, process, and save images in a few clicks

---

## Installation

1. Clone this repository or download the `rembg_gui.py` file:

```bash
git clone https://github.com/yar2000T/background-remover.git
cd background-remover
```

2. Create and activate a Python virtual environment (recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install rembg pillow onnxruntime
```

---

## Usage

1. Run the app:

```bash
python remover.py
```

2. In the UI:

* Click **Load Image** to select your image.
* Click **Remove Background** to process the image.
* Click **Save Result** to save the PNG with transparent background.

3. Auto-scaling ensures previews fit perfectly regardless of image size.

---

## Notes

* Requires Python 3.10 or higher.
* GPU acceleration is optional; older GPUs will use CPU.
* Supports PNG, JPG, JPEG, BMP, WEBP.

---

## Future Improvements

* Drag-and-drop image support
* Background replacement with color or image
* Zoom and pan preview
* Compile to standalone `.exe` for easy sharing

---

## License

MIT License – free to use and modify.
