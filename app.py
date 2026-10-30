from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.route("/")
def home():
    return {
        "application": "Python Incident Tracker",
        "status": "running",
        "version": VERSION
    }

@app.route("/health")
def health():
    return {"status": "UP"}

@app.route("/incidents")
def incidents():
    return {
        "incidents": [
            {"id": 101, "service": "API", "status": "resolved"},
            {"id": 102, "service": "Database", "status": "investigating"}
        ]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
