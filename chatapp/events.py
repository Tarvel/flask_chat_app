from .extensions import socketio
from flask_socketio import emit
from flask import request

users = {}


@socketio.on("connect")
def handle_connected():
    print ("client connected!")


@socketio.on("user_join")
def handle_user_join(username):
    print(f"User {username} joined")
    users[username] = request.sid



@socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")
    username = None
    for user in users:
        if users[user] == request.sid:
            username = user
    emit("chat", {'message':message, "username":username}, broadcast=True)