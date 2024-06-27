from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Mock data
users = {
    "1": {"name": "Piyushh", "age": 30, "location": "Location 1"},
    "2": {"name": "ajay", "age": 25, "location": "Location 2"},
    
}

products = {
    "1": {"name": "piyush bluetooth speaker", "category": "speaker", "price": 49.99},
    "2": {"name": "piyush electric brush", "category": "Toothbrush", "price": 99.99},
    # Add more product data as needed
}

# Interaction actions for simulation
interaction_actions = ["view", "click", "purchase"]

# Function to generate interaction data
def generate_interactions(user_id):
    interactions = []
    for _ in range(random.randint(1, 10)):
        interaction = {
            "user_id": user_id,
            "product_id": random.choice(list(products.keys())),
            "action": random.choice(interaction_actions),
            "timestamp": "2024-06-27T12:00:00Z"
        }
        interactions.append(interaction)
    return interactions

# Mock API endpoints
@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    if product_id in products:
        return jsonify(products[product_id])
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/api/interactions', methods=['GET'])
def get_interactions():
    user_id = request.args.get('user_id')
    if user_id in users:
        interactions = generate_interactions(user_id)
        return jsonify(interactions)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
