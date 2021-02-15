from flask import Flask, jsonify
app = Flask(__name__)


dict = {}


@app.route("/add/<key>/<value>")
def add(key, value):
    dict[key] = value
    return jsonify("Key Added")


@app.route("/get/<key>")
def getvalue(key):
    return dict[key]


@app.route("/remove/<key>")
def hello(key):
    dict.pop(key)
    return "key Removed"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
