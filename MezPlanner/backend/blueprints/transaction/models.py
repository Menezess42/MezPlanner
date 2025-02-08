from backend.blueprints.app import db
from datetime import datetime


class Transaction(db.Model):

    __tablename__ = "transactions"

    trans_id = db.Column(db.Integer, primary_key=True)
    walet_id = db.Column(db.Integer, db.ForeignKey("wallets.walet_id"))
    stock_id = db.Column(db.Integer, db.ForeignKey("stocks.stock_id"))
    qtde = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    trans_date = db.Column(db.DateTime, nullable=False)
    total_value = db.Column(db.Float, nullable=False)
    trans_type = db.Column(db.Boolean, nullable=False)

    def __init__(
        self,
        walet_id: int,
        stok_id: int,
        qtde: int,
        price: float,
        trans_date: datetime,
        trans_type: bool,
    ):
        """trans_type assums 0=Sell and 1=Buy"""
        self.walet_id = walet_id
        self.stok_id = stok_id
        self.qtde = qtde
        self.price = price
        self.trans_date = trans_date
        self.total_value = qtde * price
        self.trans_type = trans_type

    def get_trans_type(self):
        return self.trans_type

    def set_trans_type(self, trans_type):
        self.trans_type = trans_type

    def get_total_value(self):
        return self.total_value

    def set_total_value(self, total_value):
        self.total_value = total_value

    def get_trans_date(self):
        return self.trans_date

    def set_trans_date(self, trans_date):
        self.trans_date = trans_date

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_qtde(self):
        return self.qtde

    def set_qtde(self, qtde):
        self.qtde = qtde

    def get_stok_id(self):
        return self.stok_id

    def set_stok_id(self, stok_id):
        self.stok_id = stok_id

    def get_walet_id(self):
        return self.walet_id

    def set_walet_id(self, walet_id):
        self.walet_id = walet_id

