import os
import flask
from config import BASE_DIR
from sqlalchemy import func
from app import app, db
from app.utils import set_debug_response_header
from app.models import XauusdSequencial


@app.route('/', methods=['GET'])
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


@app.route('/QR.png', methods=['GET'])
def send_qr():
    return set_debug_response_header(flask.send_from_directory(BASE_DIR, 'QR.png'))
