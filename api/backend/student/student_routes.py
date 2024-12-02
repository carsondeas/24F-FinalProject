from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

students = Blueprint('students', __name__)

@students.route('/students', methods=['GET'])
def get_students():
    query = 'SELECT NUID, name, email, GPA, major FROM Student'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    response = make_response(jsonify(data))
    response.status_code = 200
    return response

@students.route('/students/<NUID>', methods=['GET'])
def get_student(NUID):
    query = 'SELECT NUID, name, email, GPA, major FROM Student WHERE NUID = %s'
    cursor = db.get_db().cursor()
    cursor.execute(query, (NUID,))
    data = cursor.fetchall()
    response = make_response(jsonify(data))
    response.status_code = 200
    return response

@students.route('/students', methods=['POST'])
def add_student():
    data = request.json
    query = '''
        INSERT INTO Student (name, email, GPA, major)
        VALUES (%s, %s, %s, %s)
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['name'], data['email'], data['GPA'], data['major']))
    db.get_db().commit()
    return make_response("Student added successfully", 201)
