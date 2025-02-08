from backend.blueprints.app import db
from backend.blueprints.transaction.models import Transaction


class Stock(db.Model):

    __tablename__ = "stocks"

    stock_id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    current_price = db.Column(db.Float, nullable=False)

    # 1 stock have N transactions
    transactions = db.relationship("Transaction", backref="Stock")

    def __init__(self, symbol: str, name: str, current_price: float):
        """constructor"""
        self.symbol = symbol
        self.name = name
        self.current_price = current_price

    def get_currentPrice(self):
        return self.current_price

    def set_currentPrice(self, currentPrice):
        self.current_price = currentPrice

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol
