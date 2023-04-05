from typing import Any, Dict

import marshmallow as ma
import marshmallow.fields as mf
from flask import Flask
from flask.views import MethodView
from flask_smorest import Api, Blueprint
from marshmallow.validate import Range

app = Flask(__name__)
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
api = Api(app)

blp = Blueprint("root", "root")


# Marshmallow
class QueryParamsSchema(ma.Schema):
    age = mf.Integer(required=True, validate=Range(min=18))

    @ma.post_load
    def make_object(self, data: Dict[str, Any], **kwargs):
        return QueryParams(**data)


# Native python, allows us to use dot-notation
class QueryParams:
    def __init__(self, age: int):
        self.age = age


# Flask-smorest requires the Flask MethodView and can not work with a standalone function like Flask
@blp.route('/')
class Hello(MethodView):
    def get(self):
        return 'Hello, World!'


# Flask-smorest route
@blp.route('/query_params')
class QueryParamsAPI(MethodView):

    @blp.arguments(QueryParamsSchema, location='query')
    def get(self, qp: QueryParams):
        return {'age': qp.age}


api.register_blueprint(blp)
