from flask import Flask
from flask_restplus import Api

app = Flask(__name__)
api = Api(app,
          version='1.0',
          title='Restaurant and accommodation classifier',
          description='Toptal recruitment task',
          contact_email="kobiela.rafal@gmail.com")

tag = api.namespace('classifier',
                    description='Restaurant and accommodation classifier endpoints')
