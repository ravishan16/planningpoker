#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""App Module."""
from flask import current_app, Flask, redirect, url_for, request, abort, render_template, \
    make_response, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from .config import config_by_name
import logging
import os
from flask_wtf.csrf import CSRFProtect
from app.models.model import planningSession
from app.models import db
from flask_cors import CORS
from flask_socketio import SocketIO


# Instantiate Flask extensions
csrf_protect = CSRFProtect()
toolbar = DebugToolbarExtension()
socketio = SocketIO()


def create_app(config_name):
    """Create Flask App."""
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config['BASE_DIR'] = os.path.dirname(os.path.abspath(__file__))

    CORS(app)

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-toolbar
    # toolbar.init_app(app)

    # Setup WTForms CSRFProtect
    csrf_protect.init_app(app)

    # Register BluePrints
    from .views import register_blueprints
    register_blueprints(app)

    socketio.init_app(app)

    # Add a default root route.
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(403)
    def page_forbidden(e):
        return render_template('403.html'), 403

    @app.errorhandler(500)
    def server_error(e):
        return render_template('500.html'), 500


    return app