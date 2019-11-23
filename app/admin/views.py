# coding: utf-8
from flask import Flask
from flask_restplus import Resource, Api

apiApp = Flask(__name__)
api = Api(apiApp)
apiApp.debug = True

# Api start
@api.route("/admin")
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# Api end

if __name__ == '__main__':
    apiApp.run(port=5000)
