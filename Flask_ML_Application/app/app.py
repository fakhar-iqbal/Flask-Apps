from flask import Flask, redirect, url_for, render_template
import numpy as np
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello there"

@app.route('/<name>')
def user(name):
    return render_template("index.html",heading=name,content="I am building an app", title="Web App")

@app.route("/admin")
def admin():
    return redirect(url_for("user",name="Admin"))


if __name__=="__main__":
    app.run()