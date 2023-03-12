from flask import Flask, request, jsonify
from cart import Cart
import requests

app = Flask(__name__)

carts = [
    Cart(1, [1, 2]),
    Cart(2, [1]),
    Cart(3, [1, 2, 3])
]

@app.route('/carts/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    product_response = requests.get(f'http://127.0.0.1:5001/products')
    products = product_response.json()
    response = []
    thisCart = None
    for c in carts:
        if c.id == user_id:
            thisCart = c
            break
    if thisCart == None:
        return "Could not find cart with id " + str(user_id)
    for p in thisCart.products:
        for product in products:
            if p == product['id']:
                response.append(p)
                #response.append(product)
    return jsonify(response)

@app.route('/carts/<int:user_id>', methods=['POST'])
def add_to_cart(user_id):
    product_id_toAdd = request.get_json()['product_id']

    product_response = requests.get(f'http://127.0.0.1:5001/products')
    products = product_response.json()

    product_toAdd = None
    for product in products:

        if product_id_toAdd == product['id']:
            product_toAdd = product
            break
    if product_toAdd == None:
        return 'Error: product_id does not exist'

    cart_toAdd = None
    carts_check = [c.__dict__ for c in carts]
    for cart in carts_check:
        if user_id == cart['id']:
            cart_toAdd = cart
            break
        return 'Error: user_id does not exist'

    if product_id_toAdd not in [product['id'] for product in products]:
        return 'Error: product_id does not exist'

    if product_id_toAdd in cart_toAdd['products']:
        return 'Error: Cart already contains this item. Can only add one of each item '

    cart_toAdd['products'].append(product_id_toAdd)
    return jsonify([cart_toAdd])

@app.route('/carts/<int:user_id>', methods=['DELETE'])
def remove_from_cart(user_id):
    product_id_toDelete = request.get_json()['product_id']

    product_response = requests.get(f'http://127.0.0.1:5001/products')
    products = product_response.json()

    product_toDelete = None
    for product in products:

        if product_id_toDelete == product['id']:
            product_toDelete = product
            break
    if product_toDelete == None:
        return 'Error: product_id does not exist'

    cart_toDelete = None
    carts_check = [c.__dict__ for c in carts]
    for cart in carts_check:
        if user_id == cart['id']:
            cart_toDelete = cart
            break
        return 'Error: user_id does not exist'

    if product_id_toDelete not in [product['id'] for product in products]:
        return 'Error: product_id does not exist'

    if product_id_toDelete not in cart_toDelete['products']:
        return 'Error: Cart already contains this item. Can only add one of each item '
    else:
        cart_toDelete['products'].remove(product_id_toDelete)
        return jsonify([cart_toDelete])


if __name__ == '__main__':
    app.run(port=5002)