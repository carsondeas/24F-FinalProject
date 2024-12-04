from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

students = Blueprint('students', __name__)

@students.route('/students', methods=['GET'])
def get_students():
    query = 'SELECT NUID, name, email, GPA, major FROM Student'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

# Add a new student
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

@students.route('/students/<NUID>/details', methods=['GET'])
def get_student_details(NUID):
    query = '''
        SELECT S.NUID, S.name, S.email, S.GPA, S.major, SK.skill
        FROM Student S
        LEFT JOIN StudentSkills SK ON S.NUID = SK.NUID
        WHERE S.NUID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (NUID,))
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

# Update a student's skills or profile
@students.route('/students/<NUID>', methods=['PUT'])
def update_student(NUID):
    data = request.json
    cursor = db.get_db().cursor()
    
    if 'skills' in data:
        cursor.execute('DELETE FROM StudentSkills WHERE NUID = %s', (NUID,))
        for skill in data['skills']:
            cursor.execute('INSERT INTO StudentSkills (NUID, skill) VALUES (%s, %s)', (NUID, skill))
    
    if 'profile' in data:
        query = '''
            UPDATE Student 
            SET name = %s, email = %s, GPA = %s, major = %s
            WHERE NUID = %s
        '''
        cursor.execute(query, (data['profile']['name'], data['profile']['email'], 
                               data['profile']['GPA'], data['profile']['major'], NUID))
    
    db.get_db().commit()
    return make_response("Student updated successfully", 200)

# Remove a student from the database
@students.route('/students/<NUID>', methods=['DELETE'])
def delete_student(NUID):
    query = 'DELETE FROM Student WHERE NUID = %s'
    cursor = db.get_db().cursor()
    cursor.execute(query, (NUID,))
    db.get_db().commit()
    return make_response("Student removed successfully", 200)