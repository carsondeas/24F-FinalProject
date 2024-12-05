from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

departments = Blueprint('departments', __name__)

@departments.route('/details', methods=['GET'])
def get_all_departments():
    query = '''
        SELECT DISTINCT departmentID, name
        FROM Department
        ORDER BY departmentID;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

@departments.route('/<int:department_id>', methods=['GET'])
def get_department_details(department_id):
    query = '''
        SELECT 
            D.departmentID AS department_id, 
            D.name AS department_name,
            P.name AS professor_name,
            C.name AS course_name
        FROM Department D
        LEFT JOIN Professor P ON D.departmentID = P.departmentID
        LEFT JOIN Course C ON P.professorID = C.professorID
        WHERE D.departmentID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (department_id,))
    data = cursor.fetchone()
    if data:
        return make_response(jsonify(data), 200)
    else:
        return make_response("Department not found", 404)