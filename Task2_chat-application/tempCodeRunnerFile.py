from flask import Flask, render_template, redirect, url_for, request
# from flask_socketio import SocketIO, join_room

# app = Flask(__name__)
# socketio = SocketIO(app)

# @app.route('/')
# def home():
#     return render_template("index1.html")

# @app.route('/chat')
# def chat():
#     username = request.args.get('username')
#     room = request.args.get('room')

#     if username and room:
#         return render_template('chat.html', username=username, room=room)
#     else:
#         return redirect(url_for('home'))

# @socketio.on('join_room')
# def handle_join_room_event(data):
#     app.logger.info("{} has joined the room {}".format(data['username'], data['room']))
#     join_room(data['room'])  # Add this line to actually join the room
#     socketio.emit('join_room_announcement',data)

# if __name__ == '__main__':
#     socketio.run(app, debug=True)