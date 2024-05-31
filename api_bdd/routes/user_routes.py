from flask import jsonify, request
from ..models.user import User
from . import user_bp


# route pour recuperer un utilisateur par son ID - GET  (id)
@user_bp.route('/users/<int:id>', methods=["GET"])
def get_user(id):
    """
    Retrieve a user by their ID.

    Args:
        id (int): The ID of the user to retrieve.

    Returns:
        Response: JSON response containing the user data if found,
                  or a 404 error message if the user is not found.
    """
    user = User.get_user(id)
    if user:
        return jsonify(user.to_dict())
    message = {"message": "User not found"}
    return jsonify(message), 404


# route pour recuperer tous les  utilisateurs
@user_bp.route('/users', methods=["GET"])
def get_users():
    """
    Retrieve all users.

    Returns:
        Response: JSON response containing a list of all users.
    """
    users = User.get_users()
    output = jsonify([user.to_dict() for user in users])
    return output


# recevoir un user pour le créer - PUT (email, password, name)
@user_bp.route('/users', methods=["PUT"])
def create_user():
    """
    Create a new user.

    Expects:
        JSON payload containing the user's email, password, and name.

    Returns:
        Response: JSON response containing the new user's
                  data if created successfully,
                  or a 400 error message if there is a validation error.
    """
    data = request.get_json()
    try:
        new_user = User.create_user(data)
        return jsonify(new_user.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# recevoir une user pour vérifier - POST (email, password)
@user_bp.route('/users', methods=["POST"])
def is_user():
    """
    Verify a user's credentials.

    Expects:
        JSON payload containing the user's email and password.

    Returns:
        Response: JSON response containing the user's data
                  if credentials are valid,
                  or a 400 error message if the credentials are invalid.
    """
    data = request.get_json()
    try:
        user = User.get_login(data)
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
