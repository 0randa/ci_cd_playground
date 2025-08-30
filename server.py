from flask import Flask

import task

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/task")
def get_task():
    tasks = task.get_tasks()

    ret_string = "<div>"

    for t in tasks:
        ret_string += f"<p>{t}</p>"

    ret_string += "</div>"

    return ret_string
