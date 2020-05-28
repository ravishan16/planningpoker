#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .main_views import main_blueprint
from . import events

def register_blueprints(app):
    app.register_blueprint(main_blueprint)