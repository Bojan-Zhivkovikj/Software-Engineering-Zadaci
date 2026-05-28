from flask import Flask, request, jsonify
# STAYS SAME: Flask is used to create the API
# STAYS SAME: request is needed for POST data
# STAYS SAME: jsonify returns JSON responses

from flask_sqlalchemy import SQLAlchemy
# STAYS SAME: SQLAlchemy handles the database

from flask_bcrypt import Bcrypt
# STAYS SAME: Bcrypt hashes passwords securely

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
# STAYS SAME: JWT tools for login tokens and protected routes


app = Flask(__name__)
# STAYS SAME: creates the Flask app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# MIGHT CHANGE: database name can change, for example students.db, products.db

app.config['JWT_SECRET_KEY'] = 'SEexe7'
# MIGHT CHANGE: secret key can be changed for another project


db = SQLAlchemy(app)
# STAYS SAME: initializes database

bcrypt = Bcrypt(app)
# STAYS SAME: initializes password hashing

jwt = JWTManager(app)
# STAYS SAME: initializes JWT system


class User(db.Model):
    # MIGHT CHANGE: class name can change, but for authentication it is usually User

    id = db.Column(db.Integer, primary_key=True)
    # STAYS SAME: primary key ID is almost always needed

    username = db.Column(db.String(80), unique=True, nullable=False)
    # MIGHT CHANGE: could be email instead of username

    password = db.Column(db.String(200), nullable=False)
    # STAYS SAME: password field is needed for authentication


with app.app_context():
    db.create_all()
    # STAYS SAME: creates database tables


@app.route('/register', methods=['POST'])
# USUALLY STAYS SAME: /register is standard for registration
def register():

    data = request.get_json()
    # STAYS SAME: gets JSON data from request

    hashed_password = bcrypt.generate_password_hash(
        data['password']
    ).decode('utf-8')
    # STAYS SAME: hashes password before saving

    new_user = User(
        username=data['username'],
        password=hashed_password
    )
    # MIGHT CHANGE: fields change if using email, role, etc.

    db.session.add(new_user)
    # STAYS SAME: adds object to database

    db.session.commit()
    # STAYS SAME: saves changes

    return jsonify(message="User registered successfully!")
    # MIGHT CHANGE: message text can change


@app.route('/login', methods=['POST'])
# USUALLY STAYS SAME: /login is standard for login
def login():

    data = request.get_json()
    # STAYS SAME: gets login data

    user = User.query.filter_by(
        username=data['username']
    ).first()
    # MIGHT CHANGE: filter by email instead of username

    if user and bcrypt.check_password_hash(
        user.password,
        data['password']
    ):
        # STAYS SAME: checks if password is correct

        access_token = create_access_token(
            identity=user.username
        )
        # MIGHT CHANGE: identity can be username, email, or user.id

        return jsonify(access_token=access_token)
        # STAYS SAME: returns JWT token

    return jsonify(message="Invalid credentials"), 401
    # STAYS SAME: 401 means unauthorized


@app.route('/users', methods=['GET'])
# MIGHT CHANGE: route can become /students, /customers, /admins
def get_users():

    users = User.query.all()
    # MIGHT CHANGE: variable/table name can change

    users_list = [
        {
            "id": user.id,
            "username": user.username
        }
        for user in users
    ]
    # MIGHT CHANGE: returned fields depend on requirements

    return jsonify(users_list)
    # STAYS SAME: returns JSON list


@app.route('/protected', methods=['GET'])
# MIGHT CHANGE: route name can change, for example /dashboard or /profile

@jwt_required()
# STAYS SAME: this makes route protected
def protected():

    current_user = get_jwt_identity()
    # STAYS SAME: gets logged-in user from token

    return jsonify(
        message=f"Hello, {current_user}! You accessed a protected route."
    )
    # MIGHT CHANGE: protected route response can change


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
    # STAYS SAME for Docker: host='0.0.0.0' allows access outside container
    # MIGHT CHANGE: port can change depending on requirements
    # STAYS SAME for local testing
    # MIGHT CHANGE in Docker/cloud: host='0.0.0.0', port=5000



    # After the code, copy this command into terminal:
    # pip install flask flask-jwt-extended flask-bcrypt flask-sqlalchemy

    # http://127.0.0.1:5000/users to see all users
    # To test user creation in Postman:
    # http://127.0.0.1:5000/register with POST and JSON body {"username": "testuser", "password": "testpass"}
    # To test login in Postman:

    #http://127.0.0.1:5000/login with POST and JSON body {"username": "testuser", "password": "testpass"}
    # Expected response: "access_token": "very-long-token-here"
    # With the token, you select GET method with http://127.0.0.1:5000/protected 
    #   and in the Authorization tab, choose Bearer Token and paste the token there. 
    #   You should get a message confirming access to the protected route.



