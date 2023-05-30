from flask import Flask, render_template, redirect, url_for, request
import os

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


@app.route("/data-types")
def data_types():
    return render_template("data_types.html")


@app.route("/strings")
def strings():
    return render_template("strings.html")


@app.route("/type-conversion")
def type_conv():
    return render_template("type_conversion.html")


@app.route("/io")
def io_basic():
    return render_template("io.html")

@app.route("/class-task-1")
def class_task():
    return render_template("tasks/class_task.html")



@app.route("/exercise", methods=["GET", "POST"])
def exercise():
    # if 'string' in request.form:
    #     button_value = request.form.get('string')
    current_file = os.path.abspath(__file__) 
    current_dir = os.path.dirname(current_file)
    file_name = f"string_exercise.txt"
    # print(current_dir)
    with open(os.path.join(current_dir, "static/data", file_name)) as f_obj:
        data = f_obj.readlines()
    return render_template("exercise.html", data = data, s=len(data))


if __name__ == "__main__":
    app.run()
