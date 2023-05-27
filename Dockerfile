FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

COPY serviceaccount.json .

ENV PORT=8080

CMD ["python", "app.py"]