from app import app
from flask import render_template, redirect, url_for, request, jsonify, session
# from flask_login import LoginManager, UserMixin, login_user, current_user, login_required
# from werkzeug.security import generate_password_hash, check_password_hash
from app.utils.auth import login_required
from app.models.admin import Admin
from app.service.admin_service import AdminService

admin_service = AdminService()

@app.route('/api/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            return jsonify({"message": "REQUIRED"}), 400
        
        if admin_service.login(username, password):
            session['logged_in'] = True
            return jsonify({"message": "Login successful"}), 200
        
        return jsonify({"message": "Invalid credentials"}), 401
    
@app.route('/api/logout', methods=['POST'])
@login_required
def logout():
    session.pop('logged_in', None)
    return jsonify({"message": "Logged out successfully"}), 200

@app.route('/api/change_password', methods=['POST'])
@login_required
def change_password():
    if request.method == 'POST':  
        username = request.form['username']
        old_password = request.form['old_password']
        new_password = request.form['new_password']

        if not username or not old_password or new_password:
            return jsonify({"message": "REQUIRED"}), 400
        
        if not admin_service.is_password_same(username, old_password):
            return jsonify({"message": "PASSWORD MISSMATCH"}), 400

        admin_service.change_password(username, new_password)

    return jsonify({"message": "SUCCESS"}), 200
     