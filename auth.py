#temp.py
from flask import jsonify, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_restful import Resource
import sqlite3

login_manager = LoginManager()

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (user_id,)).fetchone()
    conn.close()
    if user:
        return User(user['username'])
    return None

class Login(Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        if user and user['password'] == password:
            user = User(username)
            login_user(user)
            return jsonify({"message": "Login successful"})
        else:
            return jsonify({"error": "Invalid credentials"}), 401

class Logout(Resource):
    @login_required
    def get(self):
        logout_user()
        return jsonify({"message": "Logged out successfully"})

# 下面的代码逻辑视你具体框架结构而定，可能需要进一步整合到你的 Flask 应用中。
