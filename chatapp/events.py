from .extensions import socketio
from flask_socketio import emit
@socketio.on("connect")
def handle_connected():
    print ("client connected!")


@socketio.on("user_join")
def handle_user_join(username):
    print(f"User {username} joined")

@socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")
    emit("chat",{'message':message}, broadcast=True)