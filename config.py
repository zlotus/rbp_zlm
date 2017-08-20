CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

PLOT_DIR = os.path.join(basedir, 'PLOTS')

WEEK_SECONDS = 604800
DAY_SECONDS = 86400
FOUR_HOUR_SECONDS = 14400