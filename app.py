from flask import Flask, render_template, request
import os

from parser.alert_parser import detect_alert
from modules.knowledge import load_alert

app = Flask(__name__)

# ------------------------------------
# Dashboard
# ------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ------------------------------------
# RTMT Analyzer
# ------------------------------------
@app.route("/rtmt", methods=["GET", "POST"])
def rtmt():

    result = None

    if request.method == "POST":

        alert_text = request.form.get("alert")

        alert_name = detect_alert(alert_text)

        if alert_name:
            result = load_alert(alert_name)

    return render_template("rtmt.html", result=result)


# ------------------------------------
# Run Flask
# ------------------------------------
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )