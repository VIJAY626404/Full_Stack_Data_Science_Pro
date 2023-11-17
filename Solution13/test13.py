# 13. Implement notifications in a Flask app using websockets to notify users of updates
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index13.html')

@socketio.on('notify_update')
def handle_notify_update(data):
    emit('notification', {'message': 'New update available!', 'data': data}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
