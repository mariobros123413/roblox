from flask import Flask, json, request, jsonify, send_file
import os

app = Flask(__name__)

SAVE_DIRECTORY = 'json_files'
os.makedirs(SAVE_DIRECTORY, exist_ok=True)

@app.route('/saveJson/<filename>', methods=['POST'])
def save_json(filename):
    if request.is_json:
        data = request.get_json()
        filepath = os.path.join(SAVE_DIRECTORY, filename)
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file)
        return jsonify({"message": f"File '{filename}' saved successfully!"}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/getJson/<filename>', methods=['GET'])
def get_json(filename):
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    else:
        return jsonify({"error": f"File '{filename}' not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
