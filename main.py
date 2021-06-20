import datetime

from flask import Flask, render_template
from google.cloud import datastore

datastore_client = datastore.Client()

app = Flask(__name__)


def store_time(dt):
    entity = datastore.Entity(key=datastore_client.key("visit"))
    entity["timestamp"] = dt
    datastore_client.put(entity)


def fetch_times(limit):
    query = datastore_client.query(kind="visit")
    query.order = ["-timestamp"]

    times = query.fetch(limit=limit)
    return times


@app.route("/")
def root():
    # Store the current time in Datastore (new visit)
    store_time(datetime.datetime.now())

    # Get the most recent 10 access times
    times = fetch_times(10)

    return render_template("index.html", times=times)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
