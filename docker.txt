# STEP 4.1: Base image (Python)
FROM python:3.11-slim

# STEP 4.2: Set working directory inside container
WORKDIR /app

# STEP 4.3: Copy requirements file
COPY requirements.txt .

# STEP 4.4: Install Python packages
RUN pip install --no-cache-dir -r requirements.txt && \
    python -m textblob.download_corpora

# STEP 4.5: Copy application code
COPY app.py .

# STEP 4.6: Expose Flask port
EXPOSE 5000

# STEP 4.7: Start Flask app
CMD ["python", "app.py"]
