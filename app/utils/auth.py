from functools import wraps
from flask import request, jsonify, session, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session or not session['logged_in']:
            # return jsonify({"message": "Authentication required"}), 
            return redirect(url_for('loginRoute'))
        return f(*args, **kwargs)
    return decorated_function
