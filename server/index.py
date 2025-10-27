from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)
port = int(os.getenv("PORT", 3000))
service_name = os.getenv("SERVICE_NAME", "microservice")

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "ts": int(datetime.utcnow().timestamp() * 1000)
    })

@app.route("/hello")
def hello():
    return f"Hello world from argo v5 {service_name}"

if __name__ == "__main__":
    print(f"Listening on port {port}")
    app.run(host="0.0.0.0", port=port)