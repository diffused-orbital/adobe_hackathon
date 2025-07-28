# Adobe Hackathon – Round 1A Submission

## 🧠 Description

This solution uses a custom-trained YOLOv8 model to extract structured outlines (Title, H1, H2, H3) from PDF documents. The model identifies heading blocks visually, and text is extracted via Tesseract OCR.

## 🛠 Dependencies

- Python 3.10
- Ultralytics YOLOv8
- PyMuPDF
- PyTesseract
- Pillow
- Tesseract-OCR (installed in Docker)

## 📦 Docker Instructions

### Build the image:
```bash
docker build --platform linux/amd64 -t round1a-solution .
