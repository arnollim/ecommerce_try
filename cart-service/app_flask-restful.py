from flask import Flask, jsonify
from flask_restful import Api, Resource
from cart import Cart
import requests

app = Flask(__name__)
api = Api(app)

carts = [
    Cart(1, []),
    Cart(2, []),
    Cart(3, [])
]

class CartList(Resource):
    def get(self):
        return jsonify([c.__dict__ for c in carts])

class CartDetail(Resource):
    def get(self, cart_id):
        cart = next((c for c in carts if c.id == cart_id), None)
        if cart is None:
            return {'message': f'Cart {cart_id} not found'}, 404

        product_ids = cart.products
        products = []
        for product_id in product_ids:
            response = requests.get(f'http://localhost:5000/products/{product_id}')
            if response.status_code == 200:
                products.append(response.json())

        return {'id': cart.id, 'products': products}

    def post(self, cart_id):
        cart = next((c for c in carts if c.id == cart_id), None)
        if cart is None:
            return {'message': f'Cart {cart_id} not found'}, 404

        data = requests.json
        product_id = data.get('product_id')
        if product_id is None:
            return {'message': 'Missing product_id parameter'}, 400

        response = requests.get(f'http://localhost:5000/products/{product_id}')
        if response.status_code == 200:
            cart.products.append(product_id)
            return {'message': f'Added product {product_id} to cart {cart_id}'}, 201
        else:
            return {'message': f'Product {product_id} not found'}, 404