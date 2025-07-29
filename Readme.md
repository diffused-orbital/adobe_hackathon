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
👉 [Google Drive – Trained YOLOv8 Model](https://drive.google.com/drive/folders/1-j4ZGJ9p5aqeNOkBULMzImHfKA-EQY6t?usp=sharing)

Place the `best.pt` file directly in the project root (`Round_1A/`), **at the same level as `run.py`**.

---

## 🐳 Step 2: Build the Docker Image

Open a terminal or PowerShell in the `Round_1A` directory and run:

```bash
docker build -t round1a-solution .
````

This command will:

* Install system dependencies (like Tesseract)
* Install Python packages from `requirements.txt`
* Package your script and model into a ready-to-run container

---

## 📂 Step 3: Prepare Input and Output Folders

Create `input/` and `output/` folders in the project root:

```bash
mkdir input
mkdir output
```

* Add one or more `.pdf` files to the `input/` folder
* The script will write structured JSONs into the `output/` folder

---

## 🚀 Step 4: Run the Container

### 🪟 On Windows (CMD or PowerShell):

```powershell
docker run --rm ^
  -v "%cd%/input:/app/input" ^
  -v "%cd%/output:/app/output" ^
  --network none ^
  round1a-solution
```

### 🐧 On macOS/Linux (or Git Bash):

```bash
docker run --rm \
  -v "$(pwd)/input:/app/input" \
  -v "$(pwd)/output:/app/output" \
  --network none \
  round1a-solution
```

> 📝 Replace `^` with `\` if using Bash or zsh. Always check volume paths if using WSL or Git Bash on Windows.

---

## ✅ Output Format Example

Each output `.json` file looks like this:

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
* **Trained On:** Manually annotated PDF page screenshots
* **Classes:** TITLE, HEADING1, HEADING2, etc.

---

## 🙋‍♂️ Notes

* Uses **Tesseract OCR** to extract text from detected headings.
* Runs on **CPU** by default (no GPU inside Docker).
* Docker container is **fully sandboxed** (`--network none` for security).

---

## 🧼 To Clean Up Docker Image

```bash
docker rmi round1a-solution
```

---

## 🧾 License

This code is part of the Adobe India Hackathon submission by **Sanidhya Srivastava**.

````

