#!/bin/env python
from app import create_app, socketio
import os
import atexit

config_name = os.getenv('FLASKAPP_ENV') or 'dev'
print("Starting App in {} Environment".format(config_name))
app = create_app(config_name)

def exit_handler():
    pass

if __name__ == '__main__':
    atexit.register(exit_handler)
    socketio.run(app, use_reloader=True)
