from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "<h1>Please submit the form instead.</h1>"
    else:
        name = request.form.get("typename")
        name = name.capitalize()
        return render_template("hello.html", name=name)
