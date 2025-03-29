from flask_sqlalchemy import SQLAlchemy


# this is instance of the SQLAlchemy which is it a ORM which allow you to use write SQL Quer in object not raw SQL query
db = SQLAlchemy() 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(300), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

