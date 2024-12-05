from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

courses = Blueprint('courses', __name__)

@courses.route('/courses', methods=['GET'])
def get_courses():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT courseID, name, description, professorID FROM Course')
    the_data = cursor.fetchall()
    the_response = make_response(jsonify(the_data))
    the_response.status_code = 200
    return the_response

@courses.route('/courses', methods=['POST'])
def create_course():
    current_app.logger.info('POST /courses route')
    data = request.json
    query = 'INSERT INTO Course (name, description, professorID) VALUES (%s, %s, %s)'
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['name'], data['description'], data['professorID']))
    db.get_db().commit()
    return 'Course created!', 201

@courses.route('/courses/<courseID>', methods=['DELETE'])
def delete_course(courseID):
    current_app.logger.info(f'DELETE /courses/{courseID} route')
    query = 'DELETE FROM Course WHERE courseID = %s'
    cursor = db.get_db().cursor()
    cursor.execute(query, (courseID,))
    db.get_db().commit()
    return 'Course deleted!', 200