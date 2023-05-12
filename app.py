from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/fundamentals")
def fundamentals():
    return render_template("fundamentals.html")


@app.route("/data_types")
def data_types():
    return render_template("data_types.html")


@app.route("/strings")
def strings():
    return render_template("strings.html")


if __name__ == "__main__":
    app.run()
