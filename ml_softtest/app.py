import json
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def insert_vulnerability(url, vulnerability_type):
    xss_payload = "<script>alert('XSS')</script>"
    sql_injection_payload = "' OR '1'='1"
    command_injection_payload = "; ls -la"
    
    base_url, actual_value = url.rsplit('/', 1)
    
    if vulnerability_type == "XSS":
        modified_value = f"{actual_value}{xss_payload}"
    elif vulnerability_type == "SQL Injection":
        modified_value = f"{actual_value}{sql_injection_payload}"
    elif vulnerability_type == "Command Injection":
        modified_value = f"{actual_value}{command_injection_payload}"
    elif vulnerability_type == "All type":
        modified_value = f"{actual_value}{xss_payload}{sql_injection_payload}{command_injection_payload}"
    else:
        return url
    
    return f"{base_url}/{modified_value}"

def insert_vulnerability_json(json_input):
    xss_payload = "<script>alert('XSS')</script>"
    sql_injection_payload = "' OR '1'='1"
    command_injection_payload = "; ls -la"

    if isinstance(json_input, dict):
        return {key: f"{value}{xss_payload}{sql_injection_payload}{command_injection_payload}" if isinstance(value, str) else value for key, value in json_input.items()}
    return json_input


@app.route('/api/test', methods=['POST'])
def handle_test():
    try:
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({"message": "Invalid data. Missing required fields."}), 400

        request_type = data.get('requestType', '')
        
        if request_type == 'json':
            json_input_str = data.get('jsonInput', '')
            if json_input_str:
                try:
                    json_input = json.loads(json_input_str)  
                except json.JSONDecodeError:
                    return jsonify({"message": "Invalid JSON format."}), 400
            else:
                json_input = {}

            modified_json = insert_vulnerability_json(json_input)
            print(modified_json)
            
            original_url = data['url']
            response = requests.post(original_url, json=modified_json)  
            return jsonify({"status_code": response.status_code}), 200
        
        else:
            modified_url = insert_vulnerability(data['url'], data.get('vulnerabilityType', ''))
            
            response = requests.get(modified_url)  
            return jsonify({"status_code": response.status_code}), 200

    except Exception as e:
        print("Error occurred:", str(e))
        return jsonify({"message": "An error occurred.", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
