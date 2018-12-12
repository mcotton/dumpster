from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
    if request.is_json:
        print(request.get_json())
    else:
        print(request.data)
    return request.data


