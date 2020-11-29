from flask_restplus import fields
from werkzeug.datastructures import FileStorage

from app import tag


def create_score_input_docs():
    parser = tag.parser()
    parser.add_argument("file", type=FileStorage,
                        location='files',
                        required=True,
                        help='csv file')
    return parser


def create_score_response_docs():
    return tag.model('Todo', {
        'accuracy': fields.Float(required=True, description='Accuracy of the uploaded data'),
        'precision': fields.Float(required=True, description='Precision of the uploaded data'),
        'recall': fields.Float(required=True, description='Recall of the uploaded data')
    })
