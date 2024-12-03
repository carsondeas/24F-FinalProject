from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

coops = Blueprint('coops', __name__)

@coops.route('/co_ops', methods=['GET'])
def get_all_co_ops():
    query = '''
        SELECT C.id, C.title, C.company, C.description, GROUP_CONCAT(S.skill) as skills
        FROM CoOps C
        LEFT JOIN CoOpSkills CS ON C.id = CS.co_op_id
        LEFT JOIN Skills S ON CS.skill_id = S.id
        GROUP BY C.id, C.title, C.company, C.description
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

# Add a new co-op opportunity to the database
@coops.route('/co_ops', methods=['POST'])
def add_co_op():
    data = request.json
    # Insert the co-op opportunity details
    query = '''
        INSERT INTO CoOps (title, company, description)
        VALUES (%s, %s, %s)
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['title'], data['company'], data['description']))
    co_op_id = cursor.lastrowid

    # Link the co-op with skills if provided
    if 'skills' in data:
        for skill_id in data['skills']:
            query = 'INSERT INTO CoOpSkills (co_op_id, skill_id) VALUES (%s, %s)'
            cursor.execute(query, (co_op_id, skill_id))
    
    db.get_db().commit()
    return make_response("Co-op opportunity added successfully", 201)