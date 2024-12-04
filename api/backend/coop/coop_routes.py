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

@coops.route('/name', methods=['GET'])
def get_all_co_ops_name():
    query = '''
        SELECT C.jobTitle, C.companyName
        FROM CoOp C
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

@coops.route('/coops/<int:coop_id>', methods=['GET'])
def get_coop_by_id(coop_id):
    query = '''
        SELECT C.id, C.title, C.company, C.description, GROUP_CONCAT(S.skill) as skills
        FROM CoOps C
        LEFT JOIN CoOpSkills CS ON C.id = CS.coop_id
        LEFT JOIN Skills S ON CS.skill_id = S.id
        WHERE C.id = %s
        GROUP BY C.id, C.title, C.company, C.description
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (coop_id,))
    data = cursor.fetchone()
    if data:
        return make_response(jsonify(data), 200)
    else:
        return make_response("Co-op opportunity not found", 404)

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


@coops.route('/coops/<int:coop_id>', methods=['PUT'])
def update_coop(coop_id):
    data = request.json
    cursor = db.get_db().cursor()

    # Update the coop opportunity details
    if 'title' in data or 'company' in data or 'description' in data:
        query = '''
            UPDATE CoOps
            SET title = %s, company = %s, description = %s
            WHERE id = %s
        '''
        cursor.execute(query, (data.get('title'), data.get('company'), data.get('description'), coop_id))

    # Update the skills associated with the coop
    if 'skills' in data:
        # Remove existing skills
        cursor.execute('DELETE FROM CoOpSkills WHERE coop_id = %s', (coop_id,))
        # Add new skills
        for skill_id in data['skills']:
            query = 'INSERT INTO CoOpSkills (coop_id, skill_id) VALUES (%s, %s)'
            cursor.execute(query, (coop_id, skill_id))

    db.get_db().commit()
    return make_response("Co-op opportunity updated successfully", 200)

# Remove a coop opportunity from the database
@coops.route('/coops/<int:coop_id>', methods=['DELETE'])
def delete_coop(coop_id):
    cursor = db.get_db().cursor()

    # Remove associated skills first
    cursor.execute('DELETE FROM CoOpSkills WHERE coop_id = %s', (coop_id,))
    # Remove the coop itself
    query = 'DELETE FROM CoOps WHERE id = %s'
    cursor.execute(query, (coop_id,))
    
    db.get_db().commit()
    return make_response("Co-op opportunity removed successfully", 200)