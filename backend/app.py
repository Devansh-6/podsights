from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='../frontend', static_url_path='')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Implement prediction logic here
    return jsonify({"prediction": "This is a mock prediction"})

if __name__ == '__main__':
    app.run(debug=True)
