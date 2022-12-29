from flask import Flask, render_template

import HW_7_utils


app = Flask(__name__)
size_data = "hw.csv"
port = 12345


@app.route("/")
def index():
    return render_template("index.html", port=port)


@app.route("/avr_data")
def get_avr_data():
    with open(size_data) as r:
        data = r.read()
    return HW_7_utils.ave_size(data)


app.run(port=port)