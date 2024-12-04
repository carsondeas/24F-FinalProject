from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Create a new Blueprint object for professors
professors = Blueprint('professors', __name__)

# Get all professors in the database
@professors.route('/professors', methods=['GET'])
def get_all_professors():
    query = 'SELECT id, name, department_id FROM Professors'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)


# Get detailed information about a specific professor by their ID

@professors.route('/professors/<int:professor_id>', methods=['GET'])
def get_professor_by_id(professor_id):
    query = '''
        SELECT P.id, P.name, D.name AS department, GROUP_CONCAT(C.name) AS courses
        FROM Professors P
        LEFT JOIN Departments D ON P.department_id = D.id
        LEFT JOIN Courses C ON P.id = C.professor_id
        WHERE P.id = %s
        GROUP BY P.id, P.name, D.name
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (professor_id,))
    data = cursor.fetchone()
    if data:
        return make_response(jsonify(data), 200)
    else:
        return make_response("Professor not found", 404)