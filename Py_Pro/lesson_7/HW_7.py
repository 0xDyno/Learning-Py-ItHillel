from flask import Flask

import HW_7_utils


app = Flask(__name__)
size_data = "hw.csv"


@app.route("/")
def index():
    return "Hey, open 127.0.0.1:5000/avr_data"


@app.route("/avr_data")
def get_avr_data():
    with open(size_data) as r:
        data = r.read()
    return HW_7_utils.ave_size(data)


app.run(port=12345)