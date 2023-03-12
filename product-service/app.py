from flask import Flask, request, jsonify
from product import Product

app = Flask(__name__)

products = [
    Product(1, 'Product A', 'Desc1', 10.99),
    Product(2, 'Product B', 'Desc2', 20.99),
    Product(3, 'Product C', 'Desc3', 30.99)
]


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify([p.__dict__ for p in products])


@app.route('/products', methods=['POST'])
def add_product():
    product_data = request.get_json()
    new_product = Product(product_data['id'], product_data['name'], product_data['description'], product_data['price'])

    products.append(new_product)
    return jsonify([p.__dict__ for p in products])

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product_data = request.get_json()
    updated_product = Product(product_id, product_data['name'], product_data['description'], product_data['price'])
    for p in products:
        if p.id == updated_product.id:
            p.name = product_data['name']
            p.description = product_data['description']
            p.price = product_data['price']
            return jsonify([p.__dict__ for p in products])
    return "Could not find product with id " + str(product_id)


if __name__ == '__main__':
    app.run(port=5000)