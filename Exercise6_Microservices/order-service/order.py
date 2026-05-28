from flask import Flask, jsonify  # Standard: Flask creates the API, jsonify returns JSON

app = Flask(__name__)  # Standard: creates the Flask application


@app.route('/orders', methods=['GET'])  # Standard: creates GET endpoint /orders
def get_orders():
    orders = [
        {"id": 1, "item": "Laptop"},
        {"id": 2, "item": "Phone"}
    ]

    return jsonify(orders)  # Standard: converts Python list to JSON


if __name__ == "__main__":  # Standard: runs this file directly
    app.run(host='0.0.0.0', port=5002)  # Standard for Docker: app listens on port 5002