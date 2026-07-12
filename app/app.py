from flask import Flask, render_template, request, redirect

app = Flask(__name__)

events = []


@app.route("/")
def index():
    return render_template("index.html", events=events)


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        event = {
            "title": request.form["title"],
            "date": request.form["date"],
            "priority": request.form["priority"]
        }

        events.append(event)

        return redirect("/")

    return render_template("add.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
