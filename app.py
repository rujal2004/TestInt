from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo-container:27017/mydatabase"
mongo = PyMongo(app)
users_collection = mongo.db.users


@app.route('/')
def home():
    return jsonify("Welcome to API")


@app.route('/users',methods =['GET'])
def get_users():
    
    #Fetch all users from the mongodb ,excluding passwords
    users = list(users_collection.find({},{"password": 0}))
    for user in users:
    #convert objectid to string before returning
        user['_id'] = str(user['_id'])
    return jsonify(users)


#Get single user by the respective id
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    #Find the user with the given id in database excluding the passwords
    user = users_collection.find_one({'_id': ObjectId(id)}, {"password": 0})
    if user:
        #convert objectid to string before returning
        user['_id'] = str(user['_id'])
        return jsonify(user)
    # Return error if user is not found
    return jsonify({"error": "User not found"}),404

@app.route('/users',methods=['POST'])
def create_user():
    # Recieve updated user fields from request JSON body
    data = request.json
    # Hash the password before saving it
    hashed_password = generate_password_hash(data["password"])
    #Insert new user into the database
    result = users_collection.insert_one({
        "name": data.get("name"),
        "email": data.get("email"),
        "password": hashed_password
        
    })
    #Return the id of the newly created user
    return jsonify({"_id": str(result.inserted_id)}), 201

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    #Get the updated data from request body
    data = request.json
    #Update the user in the database
    result = users_collection.update_one(
        {'_id': ObjectId(id)},
        {'$set': {
            "name": data.get("name"),
            "email": data.get("email"),
            "password": generate_password_hash(data.get("password"))
        }}
    )
    # check if any document was matched and updated
    if result.matched_count > 0:
        return jsonify({"message": "User updated successfully"}), 200
    return jsonify({"error": "User not found"}), 404


@app.route('/users/<id>',methods=['DELETE'])
def delete_user(id):
    result = users_collection.find_one({'_id': ObjectId(id)})
    if result:
        # Delete the user from mongodb
        users_collection.delete_one({'_id': ObjectId(id)})
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')