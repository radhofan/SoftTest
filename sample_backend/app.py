from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for items
items = []

# Route to list all items
@app.route('/items', methods=['GET'])
def list_items():
    return jsonify(items)

# Route to add a new item
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    
    # If no data is provided, return an error
    if not data:
        return jsonify({'error': 'Invalid input, no data provided'}), 400

    # Just append whatever JSON is provided
    items.append(data)
    return jsonify({'message': 'Item added', 'item': data}), 201

# Route to update an item by index
@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    if index < 0 or index >= len(items):
        return jsonify({'error': 'Item not found'}), 404

    data = request.get_json()

    if not data:
        return jsonify({'error': 'Invalid input, no data provided'}), 400

    items[index] = data
    return jsonify({'message': 'Item updated', 'item': data})

# Route to delete an item by index
@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if index < 0 or index >= len(items):
        return jsonify({'error': 'Item not found'}), 404

    item = items.pop(index)
    return jsonify({'message': 'Item deleted', 'item': item})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
