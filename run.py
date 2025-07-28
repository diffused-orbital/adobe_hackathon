import os
os.environ["YOLO_DISABLE_CHECKS"] = "1"
import json
import fitz
from ultralytics import YOLO
from PIL import Image
import torch
import io
import pytesseract
from pathlib import Path


# Set up paths for Docker
# INPUT_DIR = r"C:/Adobe Hackathon/Round_1A/input"
# OUTPUT_DIR = r"C:/Adobe Hackathon/Round_1A/output"
INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

MODEL_PATH = "model/best.pt"

# Path to tesseract in Ubuntu
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def extract_headings_from_pdf(pdf_path, model):
    doc = fitz.open(pdf_path)
    images = [Image.open(io.BytesIO(page.get_pixmap(dpi=200).tobytes())) for page in doc]
    results = model(images, verbose=False)

    headings = []
    for i, r in enumerate(results):
        for box in r.boxes:
            label = model.names[int(box.cls[0].item())].upper()
            x1, y1, x2, y2 = map(round, box.xyxy[0].tolist())
            crop = images[i].crop((x1, y1, x2, y2))
            text = pytesseract.image_to_string(crop).strip()
            if text:
                headings.append({
                    "text": text,
                    "label": label,
                    "page": i + 1,
                    "y": y1
                })
    return sorted(headings, key=lambda h: (h["page"], h["y"]))

def main():
    device = "cpu"
    model = YOLO(MODEL_PATH).to(device)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith(".pdf"):
            continue
        path = os.path.join(INPUT_DIR, filename)
        headings = extract_headings_from_pdf(path, model)

        title = next((h["text"] for h in headings if h["label"] == "TITLE"), "Untitled Document")
        outline = [
            {
                "level": h["label"].replace("HEADING", "H"),
                "text": h["text"],
                "page": h["page"]
            }
            for h in headings if h["label"] != "TITLE"
        ]

        json_output = {
            "title": title,
            "outline": outline
        }

        json_name = Path(filename).with_suffix(".json").name
        with open(os.path.join(OUTPUT_DIR, json_name), "w", encoding="utf-8") as f:
            json.dump(json_output, f, indent=2)

    print("✅ All PDFs processed.")

if __name__ == "__main__":
    main()
