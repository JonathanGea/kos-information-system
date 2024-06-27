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
            print("masdu")
            session['logged_in'] = True
            return jsonify({"message": "Login successful"}), 200
        
        return jsonify({"message": "Invalid credentials"}), 401
    

@app.route('/api/logout', methods=['POST'])
@login_required
def logout():
    session.pop('logged_in', None)
    return jsonify({"message": "Logged out successfully"}), 200
        
        # return jsonify({"message": "Failed login"}), 401 
    
        # userData = getUserByEmail(email)  
        # if userData is not None:
        #     user = User(userData[0], userData[1], userData[2], userData[3], userData[4])
        #     if check_password_hash(user.password, password):
        #         login_user(user)
                
        #         return jsonify({"message": "Registration successful", "redirect_url": url_for('home')}), 200
        #     else:
        #         print("login gagal")
        #         return jsonify({"message": "Failed login"}), 401 
        # else:
        #     return jsonify({"message": "Failed login"}), 401 