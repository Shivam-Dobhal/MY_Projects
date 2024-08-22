# Task 2 : CHAT APPLICATION USING FLASK
#%%
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room

# initialize the flask application
app = Flask(__name__)

# initialize socketIO to handle real-time communication for the app
socketio = SocketIO(app)

# define a route for the homepage
@app.route('/')
def home():
    # Rendering the "index1.html" template when the user visits the home page
    return render_template("index1.html")

# define a route for the chat page
@app.route('/chat')
def chat():
    # get username and room parameters from the query string in the url
    username = request.args.get('username')
    room = request.args.get('room')

    # if either username or room is missing, redirect the user to the home page
    if not username or not room:
        return redirect(url_for('home'))
    
    # Render the "chat.html" template, passing the username and room as context.
    return render_template('chat.html', username=username, room=room)

@socketio.on('send_message')
def handle_send_message_event(data):
    # extract 'username', 'room', and 'message' from the received data
    username = data.get('username')
    room = data.get('room')
    message = data.get('message')

    # If all required fields are present, log the message and emit it to the room
    if username and room and message:
        app.logger.info(f"{username} has sent a message to room {room}: {message}")
        # emit the receive_message
        socketio.emit('receive_message', data, room=room)

# event listener for the "join_room" event
@socketio.on('join_room')
def handle_join_room_event(data):
    # extracting username and room from the received data
    username = data.get('username')
    room = data.get('room')

    # if both fields are present, log the event, make the user join the room, and announce it
    if username and room:
        app.logger.info(f"{username} has joined room {room}")
        # make the user join the specified room
        join_room(room)
        # emit the 'join_room_announcement' event to all clients in the room
        socketio.emit('join_room_announcement', data, room=room)

# event listener for the "leave_room" event
@socketio.on('leave_room')
def handle_leave_room_event(data):
    # extract 'username' and 'room' from the received data
    username = data.get('username')
    room = data.get('room')

    # If both fields are present, log the event, make the user leave the room, and announce it
    if username and room:
        app.logger.info(f"{username} has left room {room}")
        # Make the user leave the specified room
        leave_room(room)
        # emit the 'leave_room_announcement' event to all clients in the room
        socketio.emit('leave_room_announcement', data, room=room)

# entry point of the application
if __name__ == '__main__':
    # run the application 
    socketio.run(app, debug=True)
    





























# %%
