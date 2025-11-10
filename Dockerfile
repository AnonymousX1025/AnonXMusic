FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg curl unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deno.land/install.sh | sh \
    && ln -s /root/.deno/bin/deno /usr/local/bin/deno

RUN pip3 install -U pip && pip3 install -U -r requirements.txt
COPY . .

CMD ["bash", "start"]
