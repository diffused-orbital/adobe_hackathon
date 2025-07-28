FROM --platform=linux/amd64 python:3.12-slim

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libglib2.0-0 libsm6 libxrender1 libxext6 \
    libgl1 \
    build-essential python3-dev libjpeg-dev zlib1g-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# ✅ Copy requirements first
COPY requirements.txt .

# ✅ Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy the script and model
COPY run.py .
COPY best.pt

# ✅ Run script on container start
ENTRYPOINT ["python", "run.py"]
