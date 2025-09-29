# Base image
FROM python:3.10-slim

# Környezeti változók a Python gyorsabb működéséhez
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Munkakönyvtár létrehozása
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Függőségek másolása és telepítése
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt




COPY ./src .

RUN chmod +x run.sh


# Futtatási parancs
CMD ["tail", "-f", "/dev/null"]
