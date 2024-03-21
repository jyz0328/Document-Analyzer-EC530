# auth.py
from flask import jsonify, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_restful import Resource

login_manager = LoginManager()

users = {"admin": {"password": "admin"}}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)

class Login(Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return jsonify({"message": "Login successful"})
        else:
            return jsonify({"error": "Invalid credentials"}), 401

class Logout(Resource):
    @login_required
    def get(self):
        logout_user()
        return jsonify({"message": "Logged out"})

