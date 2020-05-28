from flask import session, request
from flask_socketio import emit, join_room, leave_room, close_room, rooms
from .. import socketio
import random
import string


@socketio.on('joined', namespace='/events')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    session['user'] = message['user']
    session['room']  = message['room']
    room = message['room']
    user = message['user']
    # if room in rooms(sid=request.sid):
    join_room(room)
    print(message)
    emit('status', {'msg': user + ' has entered the room.'}, room=room)
    # else:
    #     emit('error', {'error': 'Unable to join, room does not exist.'})


# @socketio.on('text', namespace='/events')
# def text(message):
#     """Sent by a client when the user entered a new message.
#     The message is sent to all people in the room."""
#     room = session.get('room')
#     emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)


# @socketio.on('left', namespace='/events')
# def left(message):
#     """Sent by clients when they leave a room.
#     A status message is broadcast to all people in the room."""
#     room = session.get('room')
#     leave_room(room)
#     emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)


@socketio.on('create', namespace='/events')
def create(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = ''.join(random.SystemRandom().choice(
        string.ascii_uppercase) for _ in range(5))
    session['room']  = room
    session['user'] = message['user']
    user = message['user']
    join_room(room)
    emit('status', {'msg': user + ' has entered the room. '+ room}, room=room)

@socketio.on('disconnect')
def disconnect_user():
    print('disconnecting'+request.sid)
