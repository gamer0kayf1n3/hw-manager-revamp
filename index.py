from flask import Flask, request, render_template
import json
import time
import errors

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route("/")
def index():
    #return json.load(open("data.json","r"))
    data = json.load(open("data.json","r"))
    return render_template("list.html", data=data)
@app.route("/addpage")
def ren():
    return render_template("new.html")
@app.route("/add", methods=["POST"])
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
        data[time.time()] = {
            "subject":      subject,
            "due":          due,
            "title":        title,
            "description":  description,
            "type":         Atype
        }
        json.dump(data, open("data.json", 'w'))
        return "success", 200
    else:
        return caughtError, 400

app.run()