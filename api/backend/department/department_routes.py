from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

departments = Blueprint('departments', __name__)

@departments.route('/departments', methods=['GET'])
def get_all_departments():
    query = 'SELECT id, name FROM Departments'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

@departments.route('/departments/<int:department_id>', methods=['GET'])
def get_department_details(department_id):
    query = '''
        SELECT D.id, D.name, 
               GROUP_CONCAT(DISTINCT P.name) AS professors, 
               GROUP_CONCAT(DISTINCT C.name) AS courses
        FROM Departments D
        LEFT JOIN Professors P ON D.id = P.department_id
        LEFT JOIN Courses C ON D.id = C.department_id
        WHERE D.id = %s
        GROUP BY D.id, D.name
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (department_id,))
    data = cursor.fetchone()
    if data:
        return make_response(jsonify(data), 200)
    else:
        return make_response("Department not found", 404)