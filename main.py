from flask import Flask,render_template
app = Flask(__name__)

@app.route("/home")
def hello_world():
    return render_template('home.html')

@app.route("/about")
def about():
    return "<h1> About page </h1>"

