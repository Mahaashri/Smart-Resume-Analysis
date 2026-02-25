from flask import Flask, render_template, request
import os
from utils.nlp_engine import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["resume"]
    job_description = request.form["jd"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    role, score, missing = analyze_resume(filepath, job_description)

    return render_template(
        "result.html",
        role=role,
        score=score,
        missing=missing
    )


if __name__ == "__main__":
    app.run(debug=True)