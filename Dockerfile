FROM python:3.9-slim

WORKDIR /app

COPY main.py .

ENTRYPOINT ["/app/main.py"]