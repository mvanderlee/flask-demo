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


class QueryParamsSchema(ma.Schema):
    age = mf.Integer(required=True, validate=Range(min=18))


@blp.route('/')
class Hello(MethodView):
    def get(self):
        return 'Hello, World!'


@blp.route('/query_params')
class QueryParamsAPI(MethodView):

    @blp.arguments(QueryParamsSchema, location='query')
    def get(self, qp: Dict[str, Any]):
        return {'age': qp['age']}


api.register_blueprint(blp)
