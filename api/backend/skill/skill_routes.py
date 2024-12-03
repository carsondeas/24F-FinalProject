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