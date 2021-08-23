from flask import Flask
from flask import request, Response
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.errorhandler(HTTPException)
def handle_bad_request(e):
    print(f"Request Headers: {request.headers}")
    print(f"Request Data: {request.data}")
    return Response({}, 200) 
    #return 'bad request!', 400



@app.route("/*", methods=["POST", "PUT", "PATCH", "HEAD", "GET"])
def hello():
    #if request.is_json:
    #    print(f"Request JSON: {request.get_json()}")
    #else:
    #    print(f"Request Data: {request.data}")
    
    print(f"Request Headers: {request.headers}")
    print(f"Request Data: {request.data}")
    return Response({}, 200) 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5998, debug=True)
    app.register_error_handler(handle_bad_request)

