#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""DB Model."""

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, session
from sqlalchemy import Boolean, DateTime, Column, Integer, \
    String, ForeignKey, Date, Float
from . import db


builtin_list = list


def from_sql(row):
    """Translates a SQLAlchemy model instance into a dictionary"""
    data = row.__dict__.copy()
    data['id'] = row.id
    data.pop('_sa_instance_state')
    return data


class planningSession(db.Model):
    __tablename__ = 'planning_poker_session'

    id = Column(Integer, primary_key=True)
    room_code = Column(Integer(), nullable=False, index=True)
    created_date = Column(DateTime, default=datetime.utcnow, index=True)

    def __repr__(self):
        return "<planning_poker_session {0} - {1}>".format(self.id, self.room_code)



