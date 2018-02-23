import os
import certifi
import matplotlib
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from redis import Redis
from config import PLOT_DIR


app = Flask(__name__)

app.config.from_object('config')

# db init
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Celery init
_celery = Celery('request_task', broker='redis://localhost:6379')
# Redis init
_redis = Redis(host='127.0.0.1')
# matplotlib backend init - agg is a non-gui backend for saving png image
matplotlib.use('AGG')
# patch openssl 1.0.1 cert problem of requests
os.environ['REQUESTS_CA_BUNDLE'] = certifi.old_where()

from app.request_tasks import schedule_timer
from app.itchat_tasks import start_itchat
#@app.before_first_request
def init_schedule_timer():
    print('start')
    # init schedule timer of request sender
    schedule_timer.delay()
    # init weixin itchat
    start_itchat.delay()
    # make directory of matplot images
    os.makedirs(PLOT_DIR, exist_ok=True)


from app import models as app_models
from app import views as app_views
