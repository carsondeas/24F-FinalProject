# The imports 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Department table
class Department(db.Model):
    __tablename__ = 'Department'
    departmentID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    
# Professor table
class Professor(db.Model):
    __tablename__ = 'Professor'
    professorID = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    name = db.Column(db.String(255))
    departmentID = db.Column(db.Integer, db.ForeignKey('Department.departmentID'))

# Course Table
class Course(db.Model):
    __tablename__ = 'Course'
    courseID = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    name = db.Column(db.String(255))
    professorID = db.Column(db.Integer, db.ForeignKey('Professor.professorID'))


