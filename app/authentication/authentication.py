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
    if request.method != 'POST':
        return jsonify({"message": "Method not allowed"}), 405

    try:
        username = request.form['username']
        password = request.form['password']
    except KeyError as e:
        return jsonify({"message": f"Missing form field: {e.args[0]}"}), 400

    if not username or not password:
        return jsonify({"message": "Both username and password are required"}), 400

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
    if request.method != 'POST':
        return jsonify({"message": "Method not allowed"}), 405
    
    try:
        username = request.form['username']
        old_password = request.form['old_password']
        new_password = request.form['new_password']
    except KeyError as e:
        return jsonify({"message": f"Missing form field: {e.args[0]}"}), 400
    
    if not username:
        return jsonify({"message": "Username cannot be empty"}), 400
    if not old_password:
        return jsonify({"message": "Old password cannot be empty"}), 400
    if not new_password:
        return jsonify({"message": "New password cannot be empty"}), 400
    
    try:
        if not admin_service.is_password_same(username, old_password):
            return jsonify({"message": "Old password is incorrect"}), 400

        admin_service.change_password(username, new_password)
    except Exception as e:
        # Log the exception
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"message": "An error occurred while changing the password"}), 500

    return jsonify({"message": "Password successfully changed"}), 200