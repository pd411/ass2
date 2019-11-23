# coding: utf-8
from flask_restplus import Resource, Api
from app import apiApp

@apiApp.route("/admin")
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}