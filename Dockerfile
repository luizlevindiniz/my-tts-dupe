FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y -qq --no-install-recommends espeak-ng && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app
COPY ./main.py /app/main.py

RUN python -c "from app.ai import Kokoro; Kokoro()"

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]