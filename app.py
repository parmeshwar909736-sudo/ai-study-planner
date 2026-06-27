from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = []

    if request.method == "POST":
        exam_days = int(request.form.get("days", 0))
        hours = int(request.form.get("hours", 0))
        subjects = request.form.get("subjects", "")

        subject_list = [s.strip() for s in subjects.split(",") if s.strip()]

        if len(subject_list) > 0 and hours > 0:
            time_per_subject = round(hours / len(subject_list), 1)

            for subject in subject_list:
                result.append(f"{subject} : {time_per_subject} hours/day")

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)