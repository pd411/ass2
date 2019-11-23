# coding: utf8
from flask import Blueprint
from app import homeApp

home = Blueprint("home", __name__)

import app.home.views


if __name__ == '__main__':
    homeApp.run(port=8080)
