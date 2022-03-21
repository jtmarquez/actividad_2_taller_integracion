from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
  return "Hello World!"

@app.route("/status", methods=['GET'])
def response_status():
  return "",204

@app.route("/info", methods=['GET'])
def response_info():
  response_obj = {
    'url': request.base_url,
  }

  return jsonify(response_obj), 200

@app.route("/security", methods=["DELETE"])
def response_security():
  return "",401


if __name__ == '__main__':
  app.run()