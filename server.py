import logging
from flask import Flask
from flask import request
from flask.logging import default_handler

class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)

formatter = RequestFormatter(
        '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
        '%(levelname)s in %(module)s: %(message)s'
        )

default_handler.setFormatter(formatter)



app = Flask(__name__)

@app.route("/success", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def success():
    if request.is_json:
        app.logger.info(request.get_json())
        print(request.get_json())
    else:
        app.logger.info(request.data)
        print(request.data)
    return request.data

@app.route("/failure", methods=["POST", "GET"])
def failure():
    if request.is_json:
        app.logger.info(request.get_json())
        print(request.get_json())
    else:
        app.logger.info(request.data)
        print(request.data)
    return request.data
