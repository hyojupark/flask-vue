from flask import render_template
from flask_classful import FlaskView
from flask_classful import route


class BaseView(FlaskView):
    def __init__(self) -> None:
        pass

    def index(self):
        return render_template('index.html')
