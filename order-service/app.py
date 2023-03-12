from flask import Flask, request, jsonify
from order import Order
import requests

app = Flask(__name__)

orders = [
    Order(7, [1, 2], 50.00),
    Order(8, [1], 60.00),
    Order(9, [1, 2, 3], 70.00)
]

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify([o.__dict__ for o in orders])

@app.route('/orders', methods=['POST'])
def add_order():
    order_data = request.get_json()
    new_order = Order(order_data['user_id'], [product['product_id'] for product in order_data['products']], order_data['grandTotal'])
    orders.append(new_order)
    #return jsonify([o.__dict__ for o in orders])
    return 'Order created!'

if __name__ == '__main__':
    app.run(port=5002)