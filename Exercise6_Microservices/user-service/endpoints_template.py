# =========================
# GET METHOD TEMPLATE
# =========================

# @app.route(...)
# defines API endpoint and HTTP method

# methods=['GET']
# GET is used for retrieving data

# def get_users():
# function executed when endpoint is called

# return jsonify(users)
# converts Python data into JSON response


# =========================
# POST METHOD TEMPLATE
# =========================

# @app.route('/users', methods=['POST'])
# POST endpoint used for adding new data

# data = request.json
# receives JSON data sent from client/Postman

# new_user = {...}
# creates new object using received data

# users.append(new_user)
# adds new object into list/database

# return jsonify(new_user)
# returns created object as JSON response


# =========================
# PUT METHOD TEMPLATE
# =========================

# @app.route('/users/<int:id>', methods=['PUT'])
# PUT endpoint used for updating existing data

# <int:id>
# receives ID from URL

# data = request.json
# receives updated JSON data

# for user in users:
# searches through collection

# if user["id"] == id:
# finds matching object

# user["name"] = data["name"]
# updates existing value

# return jsonify(user)
# returns updated object


# =========================
# DELETE METHOD TEMPLATE
# =========================

# @app.route('/users/<int:id>', methods=['DELETE'])
# DELETE endpoint used for deleting data

# for user in users:
# searches through collection

# if user["id"] == id:
# finds matching object

# users.remove(user)
# removes object from collection

# return jsonify({"message": "Deleted"})
# returns confirmation message