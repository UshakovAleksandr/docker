from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST", ])
def index():
    a = request.json["username"]
    return f"Hello World {a}"


if __name__ == '__main__':
    app.run(debug=True)