import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta, date
import random
import string

app = Flask(__name__)

# CRITICAL: Set secret key for sessions to work
app.config['SECRET_KEY'] = 'super-secret-key-for-sessions-to-work'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///education_complete.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    try:
        return "Hello World! App is working!"
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    print("Starting debug application...")
    app.run(host='0.0.0.0', port=5000, debug=True)
