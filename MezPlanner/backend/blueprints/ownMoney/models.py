from backend.blueprints.app import db
from datetime import datetime


class OwnMoney(db.Model):

    __tablename__ = "OwnMoney"

    own_id = db.Column(db.Integer, primary_key=True)
    walet_id = db.Column(db.Integer, db.ForeignKey("wallets.walet_id"))
    invested_value = db.Column(db.Float, nullable=False)
    invested_date = db.Column(db.DateTime, nullable=False)
    iStarted_value = db.Column(db.Boolean, nullable=True)

    def __init__(
        self,
        walet_id: int,
        invested_value: float,
        invested_date: datetime,
        iStarted_value: bool = False,
    ):
        self.walet_id = walet_id
        self.invested_value = invested_value
        self.invested_date = invested_date
        if iStarted_value:
            self.iStarted_value = iStarted_value

    def get_invested_date(self):
        return self.invested_date

    def set_invested_date(self, invested_date):
        self.invested_date = invested_date

    def get_invested_value(self):
        return self.invested_value

    def set_invested_value(self, invested_value):
        self.invested_value = invested_value

    def get_walet_id(self):
        return self.walet_id

    def set_walet_id(self, walet_id):
        self.walet_id = walet_id
