# -*- coding: utf-8
import os

from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
app.config['SWAGGER'] = {'doc_dir': './docs'}
swag = Swagger(
    app,
    template_file=os.path.join(
        os.getcwd(), 'docs', 'colors.yml'),
    parse=True)


@app.route('/colors/<palette>/')
def colors(palette):
    """
    返回颜色组
    """
    all_colors = {
        'cmyk': ['cian', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue']
    }
    if palette == 'all':
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return jsonify(result)


app.run(debug=True)
