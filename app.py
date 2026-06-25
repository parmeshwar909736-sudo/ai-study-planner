from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = []

    if request.method == "POST":
        exam_days = int(request.form["days"])
        hours = int(request.form["hours"])
        subjects = request.form["subjects"]

        subject_list = subjects.split(",")

        time_per_subject = round(hours / len(subject_list), 1)

        for subject in subject_list:
            result.append(
                f"{subject.strip()} : {time_per_subject} hours/day"
            )

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)