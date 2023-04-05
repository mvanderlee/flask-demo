import marshmallow as ma
import marshmallow.fields as mf
from flask import Flask, request
from marshmallow.validate import Range

app = Flask(__name__)


class QueryParamsSchema(ma.Schema):
    age = mf.Integer(required=True, validate=Range(min=18))


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/query_params')
def query_params():
    try:
        args = QueryParamsSchema().load(request.args)
    except ma.ValidationError as e:
        return e.messages, 422

    return {'age': args['age']}
