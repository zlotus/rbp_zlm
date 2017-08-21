CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

PLOT_DIR = os.path.join(BASE_DIR, 'PLOTS')

WEEK_SECONDS = 604800
DAY_SECONDS = 86400
FOUR_HOUR_SECONDS = 14400
