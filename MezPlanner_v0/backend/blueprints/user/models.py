# SQLAlchemy converts the models class in to a DB Table
from flask_login import UserMixin
from app import db
from datetime import datetime


class User(db.Modles, UserMixin):
    """User model, to create the
    database table and use as an object
    """

    __tablename__ = "Users"

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    createdat = db.Column(db.DateTime, nullable=True)

    def __init__(self, username, passwd, email, birthday):
        self.username = username
        self.password = passwd
        self.email = email
        self.birthday = birthday
        self.createdat = datetime.utcnow()

    def __repr__(self):
        return f"<User: {self.username}, Email: {self.email}, Birthday: {self.birthday}, CreatedAt: {self.createdat}>"

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

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
