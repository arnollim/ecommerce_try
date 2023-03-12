from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/checkout/<int:user_id>', methods=['POST'])
def checkout(user_id):
    cart_response = requests.get(f'http://127.0.0.1:5002/carts/{user_id}')
    cart = cart_response.json()
    product_ids = [product for product in cart]
    print(product_ids)

    thisCost = 0

    product_response = requests.get(f'http://127.0.0.1:5001/products')
    products = product_response.json()
    for p in product_ids:
        for product in products:
            if p == product['id']:
                thisCost += product['price']

    response = requests.post(f'http://127.0.0.1:5003/orders', json={
  "user_id": user_id,
  "products": [
      {'product_id': product_id for i, product_id in enumerate(product_ids)}
  ],
  "grandTotal": thisCost
})

    return 'Checkout Successful!'



if __name__ == '__main__':
    app.run(port=5004)