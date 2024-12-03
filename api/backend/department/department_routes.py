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
