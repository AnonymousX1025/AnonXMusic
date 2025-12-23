FROM python:3.10-slim

WORKDIR /app

# تثبيت الأدوات المطلوبة: FFmpeg + Deno + curl + unzip
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# تثبيت Deno
RUN curl -fsSL https://deno.land/install.sh | sh
ENV DENO_INSTALL="/root/.deno"
ENV PATH="${DENO_INSTALL}/bin:${PATH}"

# تثبيت Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir -r requirements.txt

# نسخ المشروع
COPY . .

# تأكد إن start قابل للتنفيذ
RUN chmod +x start

# تشغيل البوت
CMD ["bash", "start"]
