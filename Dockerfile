FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg curl unzip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip && pip3 install -U -r requirements.txt

COPY . .


CMD ["python3", "-m", "anony", "web"]
