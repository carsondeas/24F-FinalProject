from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Department(db.Model):
    __tablename__ = 'Department'
    departmentID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))