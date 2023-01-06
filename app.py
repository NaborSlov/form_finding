from flask import Flask, request, jsonify
from utils import validate_type

app = Flask(__name__)


@app.route("/get_form", methods=['POST'])
def search_form():
    data = request.form
    result = validate_type(data)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
