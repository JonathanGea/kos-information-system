from flask import render_template, redirect, url_for, request, jsonify
from app.utils.auth import login_required


from app import app

@app.route('/')
@login_required
def homeRoute():
    return render_template("admin/dashboard.html")

# @app.route('/')
# @login_required
# def homeRoute():
#     return render_template("admin/admin.html")

@app.route('/register', methods=["GET"])
def registerRoute():
    return render_template('authentication/register.html')
    
@app.route('/login', methods=["GET"])
def loginRoute():
    return render_template('authentication/login.html')


@app.route('/change_password', methods=["GET"])
def change_password_route():
    return render_template('admin/change_password.html')


    
