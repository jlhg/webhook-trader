#!/usr/bin/env python
from threading import Thread

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/webhook')
def webhook():
    socketio.emit('get', 'hello!')
    return 'success'


def run_http_server():
    app.run(host='0.0.0.0', port=5000)


def run_ws_server():
    socketio.run(app, host='0.0.0.0', port=5001)



if __name__ == '__main__':
    thread = Thread(target=run_http_server)
    thread.start()
    thread = Thread(target=run_ws_server)
    thread.start()
    thread.join()
