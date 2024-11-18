from backend.blueprints.app import db
from datetime import time


class Task_time(db.Model):
    __tablename__ = "Task_times"

    tsktime_id = db.Column(db.Integer, primary_key=True)
    startime = db.Column(db.Time, nullable=False)
    endtime = db.Column(db.Time, nullable=False)
    tsk_id = db.Column(db.Integer, db.ForeignKey("task.tsk_id"))

    def __init__(self, startime: time, endtime: time, tsk_id: int):
        self.startime = startime
        self.endtime = endtime
        self.tsk_id = tsk_id

    def __repr__(self):
        return f"<startime: {self.startime}, endtime: {self.endtime}>"

    def get_tsktime_id(self):
        return self.tsktime_id

    def set_tsktime_id(self, tsktime_id):
        self.tsktime_id = tsktime_id

    def get_endtime(self):
        return self.endtime

    def set_endtime(self, endtime):
        self.endtime = endtime

    def get_startime(self):
        return self.startime

    def set_startime(self, startime):
        self.startime = startime
