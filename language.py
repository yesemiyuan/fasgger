# -*- coding: utf-8 -*-
import random

from flasgger import swag_from
from flask import request, jsonify, Blueprint

language1 = Blueprint('language', __name__)


@language1.route('/api/<string:language>/', methods=['GET'])
@swag_from('./docs/language.yml')
def language(language):
    """
    语言特征
    """
    language = language.lower().strip()
    features = [
        "awesome", "great", "dynamic",
        "simple", "powerful", "amazing",
        "perfect", "beauty", "lovely"
    ]
    size = int(request.args.get('size', 1))
    if language in ['php', 'vb', 'visualbasic', 'actionscript']:
        return "An error occurred, invalid language for awesomeness", 500
    return jsonify(
        language=language,
        features=random.sample(features, size)
    )
