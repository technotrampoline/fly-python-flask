from flask import Flask, jsonify
import random

application = Flask(__name__)

port = 8080


@application.route("/")
def hello():
    return jsonify({"message": "Hello, World!"})


@application.route("/random")
def generate_random_number():
    return jsonify({"number": random.randint(0, 100)})


if __name__ == "__main__":
    application.run(port=port)
