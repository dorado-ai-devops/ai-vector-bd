FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        build-essential \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir chromadb[server]


RUN mkdir -p /data/chroma

EXPOSE 8000


CMD ["chromadb", "run", "--path", "/data/chroma", "--host", "0.0.0.0", "--port", "8000"]
