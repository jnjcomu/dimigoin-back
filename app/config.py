# -*- coding: utf-8 -*-

# -----------------------------
#  Import
# -----------------------------

import os
import binascii

# -----------------------------
#  COMMON CONFIG
# -----------------------------

# ENVIRONMENT (development, production)
ENVIRONMENT = os.environ.get('DMGI_ENV', 'development')

# DEFAULT URL
DEFAULT_URL = 'http://0.0.0.0:5000'

# LOGGER FORMATTING
LOGGER_FORMAT = '[%(levelname)s][%(filename)s:%(lineno)s] %(message)s'


# -----------------------------
#  APP CONFIG
# -----------------------------

# APP DEFAULT PORT (default : 3000)
APP_DEFAULT_PORT = int(os.environ.get('DMGI_PORT', 3000))

# APP SECRET KEY
APP_SECRET_KEY = os.environ.get('DMGI_SECRET', binascii.hexlify(os.urandom(24)))

# TOKEN
TOKEN_SCHEME = "bearer"
TOKEN_EXPIRE_TIME = 60 * 60 * 24 * 30 * 6 # Total 6 Month


# -----------------------------
#  API CONFIG
# -----------------------------

# API VERSION
API_VERSION = 1

# API ACCEPT HEADER
API_ACCEPT_HEADER = 'application/json'


# -----------------------------
#  MOBILE APPLICATION CONFIG
# -----------------------------

# APPLICATION VERSION
APP_VERSION = '1.0.0'


# -----------------------------
#  DATABASE CONFIG
# -----------------------------

# DATABASE URL & SETTING
DATABASE = {
    'engine': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'user': os.environ.get('DMGI_DB_USER'),
    'password': os.environ.get('DMGI_DB_PWD'),
    'database': os.environ.get('DMGI_DB_NAME')
}

DATABASE_URI = '%(engine)s://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s' % DATABASE
