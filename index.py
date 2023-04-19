from flask import Flask, request, render_template, redirect, url_for
import json
import time
from datetime import datetime
import errors

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route("/")
def index():
    #return json.load(open("data.json","r"))
    data = json.load(open("data.json","r"))
    return render_template("list.html", data=data)

@app.route("/add")
def ren():
    return render_template("new.html")

@app.route("/api/add", methods=["POST"])
def add():
    params = request.form
    data = json.load(open("data.json","r"))

    subject =       params.get("subject")
    due =           params.get("due")
    title =         params.get("title")
    description =   params.get("description")
    Atype =         params.get("type")

    caughtError = errors.check(subject, due, title, description, Atype)
    if caughtError == 0:
        dt_object = datetime.fromisoformat(due)
        unix_timestamp = int(dt_object.timestamp())
        data[time.time()] = {
            "subject":      subject,
            "due":          unix_timestamp,
            "title":        title,
            "description":  description,
            "type":         Atype
        }
        json.dump(data, open("data.json", 'w'))
        return redirect(url_for("index"))
    else:
        return caughtError, 400

@app.route("/desc/<desc_id>")
def d(desc_id):
    data = json.load(open("data.json","r"))
    return data[desc_id]["description"]

app.run()