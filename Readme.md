Here's the complete `README.md` content — updated to reflect **no `model/` folder** and a **Drive link** for downloading `best.pt`:

---

```markdown
# 📄 Adobe Hackathon Round 1A – Heading Detection from PDFs

This project uses a custom-trained [YOLOv8](https://github.com/ultralytics/ultralytics) model to detect hierarchical headings (TITLE, HEADING1, HEADING2, etc.) in PDF files and outputs a structured JSON outline.

---

## 📁 Project Structure

```

Round\_1A/
├── run.py                  # Script to run inference on PDFs
├── Dockerfile              # Docker setup for containerization
├── requirements.txt        # Required Python dependencies
├── README.md               # You're reading it
├── input/                  # Input PDFs go here
├── output/                 # Output JSONs are saved here
└── best.pt                 # ✅ Trained YOLOv8 model (manually downloaded)

````

---

## 📥 Step 1: Download the Model

The `best.pt` file is **not included** in this repository.

🔗 Download it from:  
👉 [Google Drive - Trained YOLOv8 Model](https://drive.google.com/drive/folders/1-j4ZGJ9p5aqeNOkBULMzImHfKA-EQY6t?usp=sharing)

Place the `best.pt` file directly in the project root (`Round_1A/`), **at the same level as `run.py`**.

---

## 🐳 Step 2: Build the Docker Image

Open terminal in the `Round_1A` directory and run:

```bash
docker build -t round1a-solution .
````

---

## 📂 Step 3: Prepare Input and Output Folders

Create `input/` and `output/` directories in the same folder as your `run.py`:

```bash
mkdir input
mkdir output
```

* Place one or more `.pdf` files inside the `input/` folder.
* Output JSON files will be saved in the `output/` folder.

---

## 🚀 Step 4: Run the Container

```bash
docker run --rm ^
  -v "%cd%/input:/app/input" ^
  -v "%cd%/output:/app/output" ^
  --network none ^
  round1a-solution
```

> 🔄 If you're on PowerShell or Bash and `^` doesn't work, replace it with `\` or type the command in one line.

---

## ✅ Output Format Example

The script generates a structured JSON for each input PDF.

```json
{
  "title": "Sample Document Title",
  "outline": [
    {
      "level": "H1",
      "text": "Introduction",
      "page": 1
    },
    {
      "level": "H2",
      "text": "Background",
      "page": 1
    }
  ]
}
```

---

## 🧠 Model Info

* **Model Type:** YOLOv8 (custom-trained)
* **Trained On:** Manually annotated images of PDF page screenshots
* **Classes:** TITLE, HEADING1, HEADING2, etc.

---

## 🙋‍♂️ Notes

* Tesseract OCR is used to extract text from detected heading regions.
* The container uses CPU by default for inference.
* Network access is **disabled** in Docker for security (`--network none`).

---

## 🧼 To Clean Up

```bash
docker rmi round1a-solution
```

---

## 🧾 License

This code is part of the Adobe India Hackathon submission by **Sanidhya Srivastava**.

```

---

Just copy and paste this into `README.md`.

Let me know if you want a version for GitHub-flavored markdown with badges or if you're submitting to Adobe as a ZIP.
```
