from backend.blueprints.app import db
from backend.blueprints.task_time.models import Task_time

class Task(db.Model):
    __tablename__ = "tasks"

    tsk_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    template = db.Column(db.Boolean, nullable=False)
    weekdays = db.Column(db.Integer, nullable=False)
    usr_id = db.Column(db.Integer, db.ForeignKey("users.usr_id"))

    taskTimes = db.relationship("Task_time", backref="Task")

    def __init__(
        self,
        name: str,
        description: str,
        color: str,
        template: bool,
        weekdays: int,
        usr_id: int,
    ):
        self.name = name
        self.description = description
        self.color = color
        self.template = template
        self.weekdays = weekdays
        self.usr_id = usr_id

    def __repr__(self):
        return f"<name: {self.name}, description: {self.description}, color: {self.color}, template: {self.template}, weekdays: {self.weekdays}>"

    def get_tsk_id(self):
        return self.tsk_id

    def get_weekdays(self):
        return self.get_weekdays

    def set_get_weekdays(self, get_weekdays):
        self.get_weekdays = get_weekdays

    def get_template(self):
        return self.template

    def set_template(self, template):
        self.template = template

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
