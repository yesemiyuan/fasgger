# -*- coding: utf-8 -*-
from flasgger import Swagger
from flask import Flask

# 蓝图导入区域
from language import language1
from username import user_name
from orders.stockout_order import order

app = Flask(__name__)
Swagger(app)

# 注册蓝图区域
app.register_blueprint(language1)
app.register_blueprint(user_name)
app.register_blueprint(order)

app.run()
