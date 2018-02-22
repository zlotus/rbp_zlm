CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DIST_DIR = os.path.join(BASE_DIR, 'efunds_dist')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

PLOT_DIR = os.path.join(BASE_DIR, 'PLOTS')

WEEK_SECONDS = 604800
DAY_SECONDS = 86400
FOUR_HOUR_SECONDS = 14400

# from logging.config import dictConfig
# 
# dictConfig({
#     'version': 1,
#     'formatters': {
#         'file_fmt': {
#             'format': '[%(asctime)s] - %(levelname)s in %(module)s: %(message)s',
#         },
#         'console_fmt': {
#             'format': '[%(asctime)s] - %(levelname)s - %(message)s',
#         },
#     },
#     'handlers': {
#         'file': {
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': 'error.log',
#             'formatter': 'file_fmt',
#             'level': 'DEBUG',
#         },
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'console_fmt',
#             'stream': 'ext://sys.stdout',
#             'level': 'DEBUG',
#         },
#     },
#     'root': {
#         'level': 'DEBUG',
#         'handlers': ['file', 'console']
#     }
# })
