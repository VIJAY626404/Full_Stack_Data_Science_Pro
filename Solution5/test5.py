# 5. Implement user sessions in a Flask app to store and display user-specific data
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session security

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        # You can add authentication logic here, for simplicity, let's just set the username in the session.
        session['username'] = username
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the session data to log out the user
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    # Retrieve user-specific data from the session
    username = session.get('username')

    # You can use the username to fetch user-specific data from a database or other sources
    # For simplicity, let's just pass the username to the template
    return render_template('dashboard.html', username=username)


if __name__ == '__main__':
    app.run(host ='0.0.0.0',port=4004)