# 11. Create a real-time chat application using Flask-SocketIO.
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index11.html')

@socketio.on('message')
def handle_message(message):
    emit('message', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
