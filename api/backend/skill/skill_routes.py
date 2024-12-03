from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

skills = Blueprint('skills', __name__)

@skills.route('/skills', methods=['GET'])
def get_all_skills():
    query = 'SELECT DISTINCT skill FROM StudentSkills'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

@skills.route('/skills', methods=['POST'])
def add_skill():
    data = request.json
    query = 'INSERT INTO Skills (skill) VALUES (%s)'
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['skill'],))
    db.get_db().commit()
    return make_response("Skill added successfully", 201)

@skills.route('/skills/<int:skill_id>', methods=['GET'])
def get_skill_by_id(skill_id):
    query = 'SELECT id, skill FROM Skills WHERE id = %s'
    cursor = db.get_db().cursor()
    cursor.execute(query, (skill_id,))
    data = cursor.fetchone()
    if data:
        return make_response(jsonify(data), 200)
    else:
        return make_response("Skill not found", 404)
    
# Update details of a skill (e.g., proficiency levels)
@skills.route('/skills/<int:skill_id>', methods=['PUT'])
def update_skill(skill_id):
    data = request.json
    query = 'UPDATE Skills SET skill = %s WHERE id = %s'
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['skill'], skill_id))
    db.get_db().commit()
    return make_response("Skill updated successfully", 200)

# Mark a skill as obsolete or remove it from the database
@skills.route('/skills/<int:skill_id>', methods=['DELETE'])
def delete_skill(skill_id):
    query = 'DELETE FROM Skills WHERE id = %s'
    cursor = db.get_db().cursor()
    cursor.execute(query, (skill_id,))
    db.get_db().commit()
    return make_response("Skill removed successfully", 200)