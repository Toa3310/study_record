from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    mode = ""
    
    if request.method == "POST":
        mode = request.form["mode"]
        if mode == "1":
            mode = "記録"
        elif mode == "2":
            mode = "一覧表示"
        else:
            mode = "平均学習時間表示"

    return render_template("index.html", mode = mode)

if __name__ == "__main__":
    app.run(debug=True)