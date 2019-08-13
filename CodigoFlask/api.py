from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Cliente(Resource):
    def get(self, name):
        return {"Hello Cliente":name}


api.add_resource(Cliente, '/cliente/<name>')



if __name__ == '__main__':
 app.run(debug=True)


