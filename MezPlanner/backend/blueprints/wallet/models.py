from backend.blueprints.app import db
from datetime import datetime
from backend.blueprints.transaction.models import Transaction


class Wallet(db.Model):

    __tablename__ = "wallets"

    walet_id = db.Column(db.Integer, db.ForeignKey("wallets.walet_id"))
    walet_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    current_value = db.Column(db.Float, nullable=False)
    highest_value = db.Column(db.Float, nullable=False)
    highest_value_day = db.Column(db.DateTime, nullable=False)
    stock_value = db.Column(db.Float, nullable=False)
    own_money_value = db.Column(db.Float, nullable=False)
    credit = db.Column(db.Float, nullable=False)
    only_stock_value = db.Column(db.Float, nullable=False)
    usr_id = db.Column(db.Integer, db.ForeignKey("users.usr_id"))

    # 1 stock have N transactions
    transactions = db.relationship("Transaction", backref="Wallet")

    def __init__(
        self,
        name: str,
        current_value: float,
        highest_value: float,
        highest_value_day: datetime,
        stock_value: float,
        own_money_value: float,
        credit: float,
        only_stock_value: float,
        usr_id: int,
    ):
        self.name = name
        self.current_value = current_value
        self.highest_value = highest_value
        self.highest_value_day = highest_value_day
        self.stock_value = stock_value
        self.own_money_value = own_money_value
        self.credit = credit
        self.only_stock_value = only_stock_value
        self.usr_id = usr_id

    def __repr__(self):
        return f"<name: {self.name}, current_value: {self.current_value}, highest_value: {self.highest_value}, highest_value_day: {self.highest_value_day}, stock_value: {self.stock_value}, own_money_value: {self.own_money_value}, credit: {self.credit}, only_stock_value: {self.only_stock_value}>"

    def get_only_stock_value(self):
        return self.only_stock_value

    def set_only_stock_value(self, only_stock_value):
        self.only_stock_value = only_stock_value

    def get_credit(self):
        return self.credit

    def set_credit(self, credit):
        self.credit = credit

    def get_own_money_value(self):
        return self.own_money_value

    def set_own_money_value(self, own_money_value):
        self.own_money_value = own_money_value

    def get_stock_value(self):
        return self.stock_value

    def set_stock_value(self, stock_value):
        self.stock_value = stock_value

    def get_highest_value_day(self):
        return self.get_highest_value_day

    def set_get_highest_value_day(self, get_highest_value_day):
        self.get_highest_value_day = get_highest_value_day

    def get_highest_value(self):
        return self.highest_value

    def set_highest_value(self, highest_value):
        self.highest_value = highest_value

    def get_current_value(self):
        return self.current_value

    def set_current_value(self, current_value):
        self.current_value = current_value

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
