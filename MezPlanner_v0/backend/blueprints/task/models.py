# SQLAlchemy converts the models class in to a DB Table
from backend.blueprints.app import db


class Task(db.Model):
    """Task model, to create
    the database table and use as
    an object.
    """

    __tablename__ = "Task"
    tid = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    startime = db.Column(db.DateTime, nullable=False)
    endtime = db.Column(db.DateTime, nullable=False)
    template = db.Column(db.Boolean, nullable=False)
    weekdays = db.Column(db.Integer, nullable=False)

    def __init__(self, taskname, description, startime, endtime, template, weekdays):
        self.taskname = taskname
        self.description = description
        self.startime = startime
        self.endtime = endtime
        self.template = template
        self.weekdays = weekdays

    def __repr__(self):
        return f"<Task: {self.taskname}, description: {self.description}, startime: {self.startime}, endtime: {self.endtime}, template: {self.template}, weekdays: {self.weekdays}"

    def get_taskname(self):
        return self.taskname

    def set_taskname(self, taskname):
        self.taskname = taskname

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_startime(self):
        return self.startime

    def set_startime(self, startime):
        self.startime = startime

    def get_endtime(self):
        return self.endtime

    def set_endtime(self, endtime):
        self.endtime = endtime
    def get_template(self):
        return self.template

    def set_template(self, template):
        self.template = template

    def get_weekdays(self):
        return self.weekdays

    def set_weekdays(self, weekdays):
        self.weekdays = weekdays
