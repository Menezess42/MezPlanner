from backend.blueprints.app import db
from datetime import date

class Interval(db.Model):
    __tablename__ = "Intervals"

    intvl_id = db.Column(db.Integer, primary_key=True)
    intvl_type = db.Column(db.String, nullable=False)
    weekdays = db.Column(db.Integer(7), nullable=False)
    valid_startdate = db.Column(db.Date, nullable=False)
    valid_endate = db.Column(db.Date, nullable=False)
    usr_id = db.Column(db.Integer, db.ForeignKey('user.usr_id'))

    def __init__(self, intvl_type: str, weekdays: int(7),valid_startdate: date, valid_endate: date, usr_id: int):
        self.intvl_type = intvl_type
        self.weekdays = weekdays
        self.valid_startdate = valid_startdate
        self.valid_endate = valid_endate
        self.usr_id = usr_id

    def __repr__(self):
        return f"<intrvl_type: {self.intrvl_type}, weekdays: {self.weekdays}, valid_startdate: {self.valid_startdate}, valid_endate: {self.valid_endate}>"

    def get_tsk_id(self):
        return self.tsk_id

    def get_valid_endate(self):
        return self.valid_endate

    def set_valid_endate(self, valid_endate):
        self.valid_endate = valid_endate

    def get_valid_stardate(self):
        return self.valid_stardate

    def set_valid_stardate(self, valid_stardate):
        self.valid_stardate = valid_stardate

    def get_weekdays(self):
        return self.weekdays

    def set_weekdays(self, weekdays):
        self.weekdays = weekdays
    
    def get_intrvl_type(self):
        return self.intrvl_type

    def set_intrvl_type(self, intrvl_type):
        self.intrvl_type = intrvl_type
