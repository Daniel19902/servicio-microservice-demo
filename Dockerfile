FROM python:3.10-slim
WORKDIR /app
RUN pip install -U flask
COPY . .
CMD ["python", "index.py"]
