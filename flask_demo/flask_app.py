from flask import Flask, Response, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/query_params')
def query_params():
    args = request.args

    # Validate that age exists
    if 'age' not in args:
        return {'error': 'age is required'}, 422

    # Validate that age is an integer
    try:
        age = int(args['age'])
    except Exception:
        return jsonify({'error': 'age must be an integer'}), 422

    # Validate that age is >= 18
    if age < 18:
        return Response('{"error": "age must be greater than 18"}', status=422, mimetype='application/json')

    return jsonify({'age': args['age']}), 200, {'HELPME': 'PLEASE!!'}
