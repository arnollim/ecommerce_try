FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY product.py .

EXPOSE 5001

CMD [ "python", "./app.py" ]

RUN apt-get update && \
    apt-get install -y curl