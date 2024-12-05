from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

departments = Blueprint('departments', __name__)

@departments.route('/details', methods=['GET'])
def get_all_departments():
    query = '''
        SELECT departmentID, name
        FROM Department
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

@departments.route('/<int:department_id>', methods=['GET'])
def get_department_details(department_id):
    query = '''
       SELECT D.departmentID, D.name
        FROM Departments D
        LEFT JOIN Professors P ON D.departmentID = P.departmentID
        LEFT JOIN Course C ON P.professorID = C.professorID
        WHERE D.departmentID = %s
        GROUP BY D.departmentID, D.name;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (department_id,))
    data = cursor.fetchone()
    if data:
        return make_response(jsonify(data), 200)
    else:
        return make_response("Department not found", 404)