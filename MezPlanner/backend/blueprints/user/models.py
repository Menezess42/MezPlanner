# Sqlalchemy converts the models class in to a DB table
from backend.blueprints.app import db
from flask_login import UserMixin

# from datetime import datetime


class User(db.Model, UserMixin):
    """
    User model, to create the database table and
    use as an object
    """

    __tablename__ = "Users"
    usr_id = db.Column(db.Integer, pirmary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    createdat = db.Column(db.DateTime, nullable=False)

    # Relationships => class where user is a foreign key
    tasks = db.relationship("Task", backref="User")
    intervals = db.relationship("Interval", backref="User")
    wallets = db.relationship("Wallet", backref="User")

    def __init__(self, name, password, email, birthday, createdat):
        self.name = name
        self.password = password
        self.email = email
        self.birthday = birthday
        self.createdat=createdat

    def __repr__(self):
        return f"<User: {self.name}, Email: {self.email}, Birthday: {self.birthday}, CreatedAt: {self.createdat}>"

    def get_usr_id(self):
        return self.usr_id

    def get_tasks(self):
        return self.tasks

    def set_tasks(self, tasks):
        self.tasks = tasks

    def get_intervals(self):
        return self.intervals

    def set_intervals(self, intervals):
        self.intervals = intervals

    def get_wallets(self):
        return self.wallets

    def set_wallets(self, wallets):
        self.wallets = wallets

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_birthday(self):
        return self.birthday

    def set_birthday(self, birthday):
        self.birthday = birthday

    def get_createdat(self):
        return self.createdat
