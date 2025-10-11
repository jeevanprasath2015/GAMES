from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import json, os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # change this in production

USER_FILE = 'users.json'


def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=4)


@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already exists!', 'warning')
        else:
            users[username] = {'password': generate_password_hash(password)}
            save_users(users)
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)