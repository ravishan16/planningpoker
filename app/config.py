#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration File for app."""
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_host = "127.0.0.1:3307"

class Config:
    """Config Class."""

    # os.urandom(24)
    SECRET_KEY = '\x1d\xa3\xad(y\xfd\xdbC\xa3xk\xbb\xf6\x16\x10\xa60\x99\x89\xccQ\xef\xa3\x13'
    DEBUG = False
    # CACHE
    CACHE_TYPE = 'simple'
    JSON_SORT_KEYS = False
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Config Class DevelopmentConfig."""

    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}/planning-poker-dev.db'.format(basedir)



class TestingConfig(Config):
    """Config Class TestingConfig."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}/planning-poker--test.db'.format(basedir)
    WTF_CSRF_ENABLED = False
    SERVER_NAME = "localhost"


class ProductionConfig(Config):
    """Config Class ProductionConfig."""
    DEBUG = False
    DEBUG_TB_PROFILER_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}/planning-poker--test.db'.format(basedir)



config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
