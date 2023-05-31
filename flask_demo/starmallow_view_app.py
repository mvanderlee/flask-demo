from marshmallow.validate import Range
from marshmallow_api_utils.fields import required_field
from marshmallow_api_utils.ma_dataclass import MaDataclass  # provides 'Schema' as classvar
from marshmallow_dataclass import dataclass as ma_dataclass
from starmallow import StarMallow
from starmallow.endpoints import APIHTTPEndpoint

app = StarMallow()


@ma_dataclass
class QueryParams(MaDataclass):
    age: int = required_field(validate=Range(min=18), help='This will show up in swagger')


@app.api_route('/')
class Hello(APIHTTPEndpoint):
    def get(self):
        return 'Hello, World!'


@app.api_route('/query_params')
class QueryParamsAPI(APIHTTPEndpoint):
    def get(self, qp: QueryParams) -> QueryParams:
        return {'age': qp.age}
