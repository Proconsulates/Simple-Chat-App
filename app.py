from flask import Flask
from flask_socketio import SocketIO
from flask import render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!')

@socketio.on('my-event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my-response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app)