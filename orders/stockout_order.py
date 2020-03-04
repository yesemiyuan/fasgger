# -*- coding: utf-8 -*-
import json

from flasgger import swag_from
from flask import json, request, Blueprint

order = Blueprint('order', __name__)


@order.route("/stockout_orders", methods=["POST"])
@swag_from('../docs/stockout_order.yml')
def create_stockout_order():
    """
    :return:
    """
    json_data = request.get_json()
    if not json_data:
        return json.dumps({'message': 'No input data provided.'}), 422

    erp_order_code = json_data.get('erp_order_code', None)
    sub_order_type = json_data.get('sub_order_type')
    user_name = json_data.get('user_name', 'anonymous')
    supplier_code = json_data.get('supplier_code', None)
    print("params: {0}, {1}, {2}".format(sub_order_type, user_name, supplier_code))

    resp = {"message": 'order data'}
    return json.dumps(resp), 201