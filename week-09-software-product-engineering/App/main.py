from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",title="Home", name="Hasthi")
#for the questions asked about the extra name and title, it is to pass data into the html site instead of hardcode values
@app.route("/about")
def about():
    return render_template("about.html", title="About", name="Hasthi")

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}"

@app.route("/add", methods=["POST"])
def add():
    item = request.form["item"]          # from the POST body
    qty = int(request.form["qty"])
    return f"Added {qty} x {item}"