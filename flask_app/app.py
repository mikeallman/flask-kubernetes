from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    body = {'Hello': 'World'}
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(body), 200, headers)


if __name__ == '__main__':
    app.run()
