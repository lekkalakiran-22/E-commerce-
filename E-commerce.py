
from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500}
]

users = []

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User registered successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
