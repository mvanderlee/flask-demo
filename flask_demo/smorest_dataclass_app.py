from dataclasses import field

from flask import Flask
from flask.views import MethodView
from flask_smorest import Api, Blueprint
from marshmallow.validate import Range
from marshmallow_dataclass import dataclass as ma_dataclass

app = Flask(__name__)
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
api = Api(app)

blp = Blueprint("root", "root")


@ma_dataclass
class QueryParams:
    age: int = field(metadata=dict(required=True, validate=Range(min=18), metadata=dict(help='')))


@blp.route('/')
class Hello(MethodView):
    def get(self):
        return 'Hello, World!'


@blp.route('/query_params')
class QueryParamsAPI(MethodView):

    @blp.arguments(QueryParams.Schema, location='query')
    @blp.response(status_code=200, schema=QueryParams.Schema)
    def get(self, qp: QueryParams):
        return {'age': qp.age}


api.register_blueprint(blp)
