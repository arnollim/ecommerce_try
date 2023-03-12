from flask import Flask, jsonify
from flask_restful import Api, Resource
from product import Product

app = Flask(__name__)
api = Api(app)

products = [
    Product(1, 'Product A', 10.99),
    Product(2, 'Product B', 20.99),
    Product(3, 'Product C', 30.99)
]

class ProductList(Resource):
    def get(self):
        return jsonify([p.__dict__ for p in products])

api.add_resource(ProductList, '/products')

if __name__ == '__main__':
    app.run(debug=True)