from app import db


# Define Models
class XauusdSequencial(db.Model):
    __tablename__ = 'xauusd_sequencial'
    id = db.Column(db.Float, primary_key=True)
    price = db.Column(db.Float)
    fxpro = db.Column(db.Float)
    average = db.Column(db.Float)
    dukscopy = db.Column(db.Float)
    ftroanda = db.Column(db.Float)
    fxcm = db.Column(db.Float)
    myfxbook = db.Column(db.Float)
    saxobank = db.Column(db.Float)
