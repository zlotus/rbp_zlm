from app import app
import os, certifi


run = app.run

if __name__ == "__main__":
    os.environ['REQUESTS_CA_BUNDLE'] = certifi.old_where()
    run(host='0.0.0.0', debug=True, port=80)