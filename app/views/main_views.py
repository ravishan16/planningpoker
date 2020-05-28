#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""planning poker blueprint."""

# from app.models import model
from flask import Blueprint, redirect, render_template, request, url_for, session, escape, jsonify, make_response
from app.models import model
import json

main_blueprint = Blueprint('main', __name__, template_folder='templates')


@main_blueprint.route("/main", methods=['GET', 'POST'])
def main():
    message = "Welcome to the app"
    return render_template(
        "index.html",
        message=message)


@main_blueprint.route("/healthcheck")
def healthcheck():
    return True



