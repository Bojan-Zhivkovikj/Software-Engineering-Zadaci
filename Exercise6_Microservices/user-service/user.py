from flask import Flask, jsonify  # Standard: Flask creates the API, jsonify returns JSON

app = Flask(__name__)  # Standard: creates the Flask application


@app.route('/users', methods=['GET'])  # Standard: creates GET endpoint /users
def get_users():
    users = [
        {"id": 1, "name": "Viktor Denkovski"},
        {"id": 2, "name": "Daniel Serafimov"}
    ]

    return jsonify(users)  # Standard: converts Python list to JSON


if __name__ == "__main__":  # Standard: runs this file directly
    app.run(host='0.0.0.0', port=5001)  # Standard for Docker: app listens on port 5001



    # Flask is used for building APIs
# jsonify converts Python objects into JSON format

# app = Flask(__name__)
# creates the Flask application instance

# @app.route('/users', methods=['GET'])
# creates GET endpoint accessible from browser/Postman

# host='0.0.0.0'
# allows access outside container

# port=5001
# user service port