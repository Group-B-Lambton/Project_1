# 📦 Base Image: Lightweight Python 3.9 with security updates
FROM python:3.9-slim

# 📁 Set working directory inside the container
WORKDIR /app

# 📄 Copy necessary application files into the container
COPY requirements.txt .
COPY app.py .
COPY README.md .

# ⚙️ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 🌐 Expose Streamlit default port
EXPOSE 8501

# 🚀 Launch the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
