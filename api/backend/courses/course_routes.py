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


@courses.route('/courses', methods=['PUT'])
def change_course_description():
    current_app.logger.info('PUT /courses route')
    data = request.json
    query = 'UPDATE Course SET description = %s WHERE courseID = %s AND professorID = %s'
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['description'], data['courseID'], data['professorID']))
    db.get_db().commit()
    return 'Course Description Updated!', 201


@courses.route('/courses/<courseID>', methods=['DELETE'])
def delete_course_from_professor(courseID):
    try:
        data = request.json
        current_app.logger.info(f'DELETE /courses/{courseID} route')
        query = 'DELETE FROM Course WHERE courseID = %s AND professorID = %s'
        cursor = db.get_db().cursor()
        cursor.execute(query, (courseID, data['professorID']))  # Use courseID from the URL and professorID from the body
        db.get_db().commit()
        return 'Course deleted!', 200
    except Exception as e:
        current_app.logger.error(f"Error deleting course {courseID}: {str(e)}")
        return jsonify({"error": "Failed to delete course"}), 500



@courses.route('/courses/<professorID>', methods=['GET'])
def get_professor_courses(professorID):
    try:
        cursor = db.get_db().cursor()
        query = '''
            SELECT courseID, name, description, professorID 
            FROM Course
            WHERE professorID = %s
        '''
        cursor.execute(query, (professorID,))
        the_data = cursor.fetchall()
        return jsonify(the_data), 200
    except Exception as e:
        current_app.logger.error(f"Error fetching courses for professor {professorID}: {str(e)}")
        return jsonify({"error": "Failed to fetch courses"}), 500
