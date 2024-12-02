from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

skills = Blueprint('skills', __name__)

@skills.route('/skills', methods=['GET'])
def get_skills():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT skillID, name FROM Skill')
    the_data = cursor.fetchall()
    the_response = make_response(jsonify(the_data))
    the_response.status_code = 200
    return the_response

@skills.route('/skills', methods=['POST'])
def create_skill():
    current_app.logger.info('POST /skills route')
    data = request.json
    query = 'INSERT INTO Skill (name) VALUES (%s)'
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['name'],))
    db.get_db().commit()
    return 'Skill created!', 201

@skills.route('/skills/<skillID>', methods=['DELETE'])
def delete_skill(skillID):
    current_app.logger.info(f'DELETE /skills/{skillID} route')
    query = 'DELETE FROM Skill WHERE skillID = %s'
    cursor = db.get_db().cursor()
    cursor.execute(query, (skillID,))
    db.get_db().commit()
    return 'Skill deleted!', 200
