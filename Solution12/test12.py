# 12. Build a Flask app that updates data in real-time using WebSocket connections
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index12.html')

def background_thread():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        socketio.emit('update', {'data': f'Update {count}', 'timestamp': timestamp}, namespace='/test')

@socketio.on('connect', namespace='/test')
def handle_connect():
    print('Client connected')
    emit('update', {'data': 'Connected', 'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())})

if __name__ == '__main__':
    # Start the background thread for sending updates
    thread = Thread(target=background_thread)
    thread.daemon = True
    thread.start()

    # Start the Flask application with SocketIO support
    socketio.run(app, debug=True)
