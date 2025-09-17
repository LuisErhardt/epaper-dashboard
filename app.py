from flask import Flask, render_template, jsonify, request
from pathlib import Path
import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/update-pommes", methods=["POST"])
def update_pommes():
    try:
        home = Path.home()
        result = subprocess.run(
            [home + "/.virtualenvs/pimoroni/bin/python", home + "/inkyCode/pommes.py"],
            text=True,
            check=True,
        )
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/set-text", methods=["POST"])
def set_text():
    try:
        data = request.get_json()
        if not data or "text" not in data:
            raise Exception("Missing field 'text'")
        text = data["text"]
        result = subprocess.run(["sleep", "4"], text=True)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run()
