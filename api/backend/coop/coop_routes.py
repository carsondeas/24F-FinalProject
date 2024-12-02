from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

coops = Blueprint('coops', __name__)

@coops.route('/coops', methods=['GET'])
def get_coops():
    query = 'SELECT jobID, jobTitle, companyName, industry FROM CoOp'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    response = make_response(jsonify(data))
    response.status_code = 200
    return response

@coops.route('/coops', methods=['POST'])
def add_coop():
    data = request.json
    query = '''
        INSERT INTO CoOp (jobTitle, companyName, industry)
        VALUES (%s, %s, %s)
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['jobTitle'], data['companyName'], data['industry']))
    db.get_db().commit()
    return make_response("CoOp added successfully", 201)
