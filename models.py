from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_pk(db):
    return db.Column(db.Integer, primary_key=True)


class Stock(db.Model):

    id = get_pk(db)
    code = db.Column(db.String(5), unique=True)
    name = db.Column(db.String(100), nullable=True, unique=True)
    desc = db.Column(db.Text(convert_unicode=True))
    first_listed = db.Column(db.DateTime, nullable=True)
    last_listed = db.Column(db.DateTime, nullable=True)


class StockKeyStats(db.Model):

    id = get_pk(db)
    stock = db.Column(db.Integer, db.ForeignKey('stock.id'))
    date = db.Column(db.DateTime, nullable=False)
    earnings = db.Column(db.Numeric)
    roe = db.Column(db.Numeric)
    book_value = db.Column(db.Numeric)
    pe = db.Column(db.Numeric)
    market_cap = db.Column(db.Numeric)
    shares_outstanding = db.Column(db.BigInteger)
    total_debt_ratio = db.Column(db.Numeric)
