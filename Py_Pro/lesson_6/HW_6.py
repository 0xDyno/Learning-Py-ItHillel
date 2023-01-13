"""
Create a view function that returns the contents of the file with
installed packages in the current project (requirements.txt)

The function should handle the '/' route. Formatting data read from files
should be done in a separate function (for example, in the utils.py module)
"""
from flask import Flask

import HW_6_utils


app = Flask(__name__)
path = "../../requirements.txt"


@app.route('/')
def index():
    with open(path) as reader:
        result = reader.read()
    return HW_6_utils.convert_req_to_html(result)


app.run(debug=True)
