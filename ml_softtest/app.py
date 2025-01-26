from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/test', methods=['POST'])
def handle_test():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Log the received data
        print("Received data:", data)
        
        # Send a response back to the client
        return jsonify({"message": "Data received successfully!", "data": data}), 200
    except Exception as e:
        # Handle any unexpected errors
        print("Error occurred:", str(e))
        return jsonify({"message": "An error occurred.", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
