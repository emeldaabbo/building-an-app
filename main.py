import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    # Use static data to inflate the template
    # This will be replaced at a later stage
    dummy_times = [
        datetime.datetime(2021, 1, 1, 10, 0, 0),
        datetime.datetime(2021, 1, 3, 10, 30, 0),
        datetime.datetime(2021, 1, 3, 11, 0, 0),
    ]

    return render_template("index.html", times=dummy_times)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
