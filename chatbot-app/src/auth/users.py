from flask import Blueprint, request, jsonify
from models.user import users, get_user_by_username

auth_bp = Blueprint('auth', __name__)

def login_user(username, password):
    user = get_user_by_username(username)
    if user and user["password"] == password:
        return user
    return None

def register_user(mobile_number):
    # For testing, just check if mobile number already exists
    for user in users:
        if user["mobile_number"] == mobile_number:
            return False
    # Registration logic for testing (not persistent)
    return True

@auth_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify({'user': {'id': user["id"], 'mobile_number': user["mobile_number"], 'username': user["username"], 'role': user["role"]}}), 200
    return jsonify({'error': 'User not found'}), 404