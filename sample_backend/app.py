from flask import Flask, request, jsonify
from flask_cors import CORS  
  
app = Flask(__name__)  
CORS(app)
  
# In-memory storage for items  
items = []  
  
# Helper function to find an item by index  
def get_item_by_index(index):  
    if 0 <= index < len(items):  
        return items[index]  
    return None  
  
# Route to list all items  
@app.route('/items', methods=['GET'])  
def list_items():  
    return jsonify(items)  
  
# Route to add a new item  
@app.route('/items', methods=['POST'])  
def add_item():  
    data = request.get_json()  
    if not data or 'item' not in data:  
        return jsonify({'error': 'Invalid input'}), 400  
    item = data['item']  
    items.append(item)  
    return jsonify({'message': 'Item added', 'item': item}), 201  
  
# Route to update an item by index  
@app.route('/items/<int:index>', methods=['PUT'])  
def update_item(index):  
    item = get_item_by_index(index)  
    if item is None:  
        return jsonify({'error': 'Item not found'}), 404  
    data = request.get_json()  
    if not data or 'item' not in data:  
        return jsonify({'error': 'Invalid input'}), 400  
    new_item = data['item']  
    items[index] = new_item  
    return jsonify({'message': 'Item updated', 'item': new_item})  
  
# Route to delete an item by index  
@app.route('/items/<int:index>', methods=['DELETE'])  
def delete_item(index):  
    item = get_item_by_index(index)  
    if item is None:  
        return jsonify({'error': 'Item not found'}), 404  
    items.pop(index)  
    return jsonify({'message': 'Item deleted', 'item': item})  
  
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000, debug=True)
