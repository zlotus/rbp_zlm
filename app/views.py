import os
import flask
import requests
from config import BASE_DIR, EFUNDS_DIST_DIR, XAUUSD_DIST_DIR
from sqlalchemy import func
from app import app, db
from app.utils import set_debug_response_header
from app.models import XauusdSequencial


@app.route('/zlm', methods=['GET'])
def index():
    os.path.isfile('QR.png')
    content = """
    <html>
        <body>
        <p>
            Database row Count: {}
        </p>
        <!--QR.png-->
        </body>
    </html>
    """.format((db.session.execute(db.session.query(func.count(XauusdSequencial.id))).first()[0]))
    if os.path.isfile(os.path.join(BASE_DIR, 'QR.png')):
        content = content.replace('<!--QR.png-->', '<p><img src="QR.png"/></p>')
    else:
        content = content.replace('<!--QR.png-->', '')
    resp = flask.Response(content)
    return set_debug_response_header(resp)


@app.route('/zlm/QR.png', methods=['GET'])
def send_qr():
    return set_debug_response_header(flask.send_from_directory(BASE_DIR, 'QR.png'))


# publish xauusd front-end to port 80
@app.route('/xauusd', methods=['GET'])
def xauusd_entry():
    resp = flask.send_from_directory(XAUUSD_DIST_DIR, 'index.html', mimetype='text/javascript')
    resp.headers['content-type'] = 'text/html'
    return resp


@app.route('/xauusd/<path:path>', methods=['GET'])
def xauusd_files(path):
    print(path)
    return flask.send_from_directory(XAUUSD_DIST_DIR, path)


# publish efunds front-end to port 80
@app.route('/fund', methods=['GET'])
def entry_efunds_dist():
    resp = flask.send_from_directory(EFUNDS_DIST_DIR, 'index.html', mimetype='text/javascript')
    resp.headers['content-type'] = 'text/html'
    return resp


@app.route('/fund/<path:path>', methods=['GET'])
def entry_dist(path):
    return flask.send_from_directory(EFUNDS_DIST_DIR, path)


# temporary efunds proxy
@app.route('/efunds', methods=['GET'])
def get_efunds_plan_list():
    return flask.jsonify(requests.get('http://localhost:8080/efunds').json())


@app.route('/efunds/<fund_code>/valuations', methods=['GET'])
def get_real_time_valuation(fund_code):
    return flask.jsonify(requests.get('http://localhost:8080/efunds/' + fund_code + '/valuations').json())


@app.route('/efunds/<fund_code>/transactions', methods=['GET'])
def get_transaction_history(fund_code):
    return flask.jsonify(requests.get('http://localhost:8080/efunds/' + fund_code + '/transactions').json())


@app.route('/efunds/<fund_code>/values/<duration>', methods=['GET'])
def get_value_history(fund_code, duration):
    return flask.jsonify(requests.get('http://localhost:8080/efunds/' + fund_code + '/values/' + duration).json())
