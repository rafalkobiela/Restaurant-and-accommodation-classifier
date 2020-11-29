from flask import request
from flask_restplus import Resource, fields

from app.swagger_docs import create_score_input_docs, create_score_response_docs
from model.model import Model
from app import tag

model = Model()
model.load_model()


@tag.route("/predict")
class Predict(Resource):
    @tag.doc(params={'web_text': 'Web text',
                     'title': 'Title',
                     'description': 'Description',
                     'keywords': 'Keywords'})
    def get(self):
        web_text = request.args.get("web_text", "")
        title = request.args.get("title", "")
        description = request.args.get("description", "")
        keywords = request.args.get("keywords", "")
        return model.predict(web_text, title, description, keywords)


@tag.route("/score")
class Score(Resource):
    @tag.expect(create_score_input_docs())
    @tag.marshal_with(create_score_response_docs(), as_list=False)
    def post(self):
        file = request.files["file"]
        return model.score(file).__dict__
