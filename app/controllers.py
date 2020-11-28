from flask import request, jsonify
from pandas.errors import ParserError

from app import app
from model.model import Model

model = Model()
model.load_model()


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, ParserError):
        code = 400
    return jsonify(error=str(e)), code


@app.route("/predict", methods=["GET"])
def predict():
    if request.method == "GET":
        web_text = request.args.get("web_text", "")
        title = request.args.get("title", "")
        description = request.args.get("description", "")
        keywords = request.args.get("keywords", "")

        return model.predict(web_text, title, description, keywords)


@app.route("/score", methods=["POST"])
def score():
    if request.method == "POST":
        file = request.files["file"]
        return jsonify(model.score(file).__dict__)
