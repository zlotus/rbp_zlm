import requests
import re
import json
import schedule
import time
from app.models import XauusdSequencial
from app import db, _celery


@_celery.task
def schedule_timer():
    # schedule.every(5).seconds.do(request_task)
    schedule.every(5).minutes.do(request_task)

    while True:
        schedule.run_pending()
        time.sleep(1)


def request_task():
    # ref http://gold.hexun.com/
    # ref img.hexun.com/gold/js/hexun.index.gold.js
    # ref quote.forex.hexun.com/rest1/quote_jsonx.ashx?list=XAUUSD
    latest_row = XauusdSequencial.query.order_by(XauusdSequencial.id.desc()).first()

    start_time = time.time()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
    }
    try:
        text = requests.get('http://quote.forex.hexun.com/rest1/quote_jsonx.ashx?list=XAUUSD',
                            headers=headers, timeout=30).text
        p = re.compile('Price:([0-9.]*)')
        price = float(p.search(text).group(1))
    except requests.Timeout:
        price = latest_row.price

        # ref https://widgets-m.fxpro.com/cn/statistics/client-positions
    try:
        text = requests.get('https://widgets-m.fxpro.com/cn/statistics/client-positions', timeout=30).text
        p = re.compile('<div class="label">GOLD</div>\n\t\t\t\t<div class="percentage buy">([0-9.]+)%</div>')
        fxpro = float(p.search(text).group(1))
    except requests.Timeout:
        fxpro = latest_row.fxpro

    # ref https://datacenter.jin10.com/reportType/dc_ssi_trends
    try:
        text = requests.get('https://datacenter.jin10.com/get_dc_second_data?type=dc_ssi_shark_fx_current',
                            timeout=30).text
        p = re.compile('/\*\*/JQ_[0-9]{10}\(([^()]*)\)*;')
        json_text = p.search(text).group(1)
        jd = json.loads(json_text)['data']['pairs']['XAUUSD']
        average, dukscopy, ftroanda, fxcm, myfxbook, saxobank = \
            float(jd['average']), float(jd['dukscopy']), float(jd['ftroanda']), \
            float(jd['fxcm']), float(jd['myfxbook']), float(jd['saxobank'])
    except requests.Timeout:
        average, dukscopy, ftroanda, fxcm, myfxbook, saxobank = \
            latest_row.average, latest_row.dukscopy, latest_row.ftroanda, \
            latest_row.fxcm, latest_row.myfxbook, latest_row.saxobank
    # print('%s, %f, %f, %f, %f, %f, %f, %f, %f' % (datetime.fromtimestamp(start_time),
    #                                               price, fxpro, average, dukscopy,
    #                                               ftroanda, fxcm, myfxbook, saxobank))
    insert_xauusd_row(start_time, price, fxpro, average, dukscopy, ftroanda, fxcm, myfxbook, saxobank)


def insert_xauusd_row(id, price, fxpro, average, dukscopy, ftroanda, fxcm, myfxbook, saxobank):
    db.session.add(
        XauusdSequencial(id=id, price=price, fxpro=fxpro, average=average, dukscopy=dukscopy,
                         ftroanda=ftroanda, fxcm=fxcm, myfxbook=myfxbook, saxobank=saxobank)
    )
    db.session.commit()
