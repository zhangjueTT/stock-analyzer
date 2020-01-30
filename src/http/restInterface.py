from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    return "Hello World"


@app.route('/task', methods=['GET'])
def analyze_log():
    return "task"


def start_server():
    app.run(host="0.0.0.0", port=8001)
