import os
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="static", static_url_path="/static")


@app.get("/")
def index():
    return send_from_directory("static", "index.html")


@app.get("/health")
def health():
    return jsonify(status="ok", app="nba-dice")


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
