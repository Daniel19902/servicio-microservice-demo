FROM python:3.10-slim
WORKDIR /app
RUN pip install -U flask
COPY server/ .
CMD ["python", "index.py"]
