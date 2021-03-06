from flask import Flask, escape, request
from .stockParser import parse_stock

app = Flask(__name__, static_url_path="/static")


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/test', methods=['GET'])
def test():
    return "Hello World"


@app.route('/stock', methods=['GET'])
def analyze_log():
    stock_id = request.args.get("stockid", "error")
    data = parse_stock(stock_id)
    return data


def start_server():
    app.run(host="0.0.0.0", port=8001)
