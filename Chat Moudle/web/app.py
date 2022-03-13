from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app  = Flask(__name__)
api = Api(app)


def validate_postedData(postedData,func_name):
    if func_name=='add':
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200

class Add(Resource):
    def post(self):
        ##step 1
        postedData = request.get_json()
        status_code = validate_postedData(postedData,'add')
        if status_code!=200:
            retJson={
                    'Message': 'An error occured',
                    'Status code': status_code

                    }
            return jsonify(retJson)


        x = postedData['x']
        y = postedData['y']
        x,y = int(x),int(y)
        ret = x+y
        retMap = {
                'Sum': ret,
                'Status Code': 200
                }
        return jsonify(retMap)



api.add_resource(Add,'/add')


@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/hithere')
def hi_there():
    return "Hi guys"

@app.route('/json')
def json_ret():
    retJson = {
        'x':26,
        'y':28
    }
    return jsonify(retJson)

if __name__=='__main__':
    app.run(host='0.0.0.0')