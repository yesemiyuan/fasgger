# -*- coding: utf-8 -*-
from flask import Blueprint
from flasgger import swag_from
from flask_restful import Resource


class Username(Resource):
    def get(self, username):
        """
        This examples uses FlaskRESTful Resource
        It works also with swag_from, schemas and spec_dict
        ---
        parameters:
         - in: path
           name: username
           type: string
           required: true
        responses:
         200:
           description: A single user item
           schema:
             id: User
             properties:
               username:
                 type: string
                 description: The name of the user
                 default: Steven Wilson
        """
        return {'username': username}, 200


user_name = Blueprint('username', __name__)


@user_name.route('/api/username', methods=['GET'])
@swag_from('./docs/language.yml')
def username():
    """
    parameters:
         - in: path
           name: username
           type: string
           required: true
        responses:
         200:
           description: A single user item
           schema:
             id: User
             properties:
               username:
                 type: string
                 description: The name of the user
                 default: Steven Wilson
    :return:
    """
    print(111)
