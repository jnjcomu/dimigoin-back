# -*- coding: utf-8 -*-
"""
    frest - flask restful api frame
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This project is the frame of the restful api server created with flask.

    :copyright: (C) 2017 h4wldev@gmail.com
    :license: MIT, see LICENSE for more details.
"""
import os

from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db, routes, handler
from app.config import APP_DEFAULT_PORT, APP_SECRET_KEY, ENVIRONMENT, DEFAULT_URL
from app.modules.auth import login, token


if __name__ == '__main__':
    host = DEFAULT_URL
    port = APP_DEFAULT_PORT

    app.secret_key = APP_SECRET_KEY

    db.create_all()

    migrate = Migrate(app, db)
    manager = Manager(app)

    manager.add_command('db', MigrateCommand)

    if ENVIRONMENT == 'production' or ENVIRONMENT == 'testing':
        manager.add_command('runserver', Server(host=host, port=port, use_debugger=False))
    else:
        manager.add_command('runserver', Server(host=host, port=port, use_debugger=True))

    manager.run()
