from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

departments = Blueprint('departments', __name__)

@departments.route('/departments', methods=['GET'])
def get_departments():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT departmentID, name FROM Department')
    data = cursor.fetchall()
    response = make_response(jsonify(data))
    response.status_code = 200
    return response

@departments.route('/departments', methods=['POST'])
def create_departments():
    current_app.logger.info('POST /departments route')
    data = request.json
    query = 'INSERT INTO Department (name) VALUES (%s)'
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['name'],))
    db.get_db().commit()
    return 'Department created!', 201

@departments.route('/departments/<departmentID>', methods=['DELETE'])
def delete_department(departmentID):
    current_app.logger.info(f'DELETE /departments/{departmentID} route')
    query = 'DELETE FROM Department WHERE departmentID = %s'
    cursor = db.get_db().cursor()
    cursor.execute(query, (departmentID,))
    db.get_db().commit()
    return 'Department deleted!', 200