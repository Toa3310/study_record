from flask import Flask, render_template, request
from study_record import add_record, get_records, get_average, get_total

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/record', methods=["GET", "POST"])
def record():
    message = ""

    if request.method == "POST":
        try:
            date = request.form["date"]
            subject = request.form["subject"]
            study_time = int(request.form["time"])
            comment = request.form["comment"]

            success = add_record(date, subject, study_time, comment)

            if success:
                message = "記録が正常に完了しました"
            else:
                message = "記録に失敗しました"
        except ValueError:
            message = "入力内容が正しくありません"

    return render_template("record.html", message=message)

@app.route('/records')
def records():
    records = get_records()
    average = get_average()
    total = get_total()

    return render_template("records.html", records=records, average=average, total=total)

if __name__ == "__main__":
    app.run(debug=True)