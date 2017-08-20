import flask
from flask import request
from sqlalchemy import func
from app import app, db
from app.utils import set_debug_response_header
import json
from app.models import XauusdSequencial


@app.route('/', methods=['GET'])
@app.route('/api/v1/data', methods=['GET'])
def user_login_service():
    resp = flask.Response(json.dumps({'count': db.session.execute(db.session.query(func.count(XauusdSequencial.id))).first()[0]}))
    return set_debug_response_header(resp)
