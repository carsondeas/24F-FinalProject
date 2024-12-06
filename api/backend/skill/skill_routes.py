from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

skills = Blueprint('skills', __name__)

@skills.route('/all', methods=['GET'])
def get_all_skills():
    query = '''
        SELECT DISTINCT Skill.name ,Skill.skillId
        FROM Skill
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

@skills.route('/add', methods=['POST'])
def add_skill():
    data = request.json
    query = 'INSERT INTO Skills (skill) VALUES (%s)'
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['skill'],))
    db.get_db().commit()
    return make_response("Skill added successfully", 201)

@skills.route('/<string:skill_name>', methods=['GET'])
def get_skill_by_name(skill_name):
    query = '''
        SELECT Skill.skillId 
        FROM Skill 
        WHERE Skill.name = %s'''
    cursor = db.get_db().cursor()
    cursor.execute(query, (skill_name,))
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

@skills.route('/skills/analytics', methods=['GET'])
def get_skills_analytics():
    query = '''
        SELECT 
            J.industry,
            J.role,
            S.skill,
            COUNT(*) AS demand_count
        FROM JobPostings J
        LEFT JOIN JobSkills JS ON J.id = JS.job_id
        LEFT JOIN Skills S ON JS.skill_id = S.id
        GROUP BY J.industry, J.role, S.skill
        ORDER BY demand_count DESC
        LIMIT 20
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    trending_skills = cursor.fetchall()

    query = '''
        SELECT 
            J.industry,
            J.role,
            S.skill,
            COUNT(*) AS gap_count
        FROM JobPostings J
        LEFT JOIN JobSkills JS ON J.id = JS.job_id
        LEFT JOIN Skills S ON JS.skill_id = S.id
        LEFT JOIN StudentSkills SS ON S.id = SS.skill_id
        WHERE SS.skill_id IS NULL
        GROUP BY J.industry, J.role, S.skill
        ORDER BY gap_count DESC
        LIMIT 20
    '''
    cursor.execute(query)
    skill_gaps = cursor.fetchall()

    data = {
        "trending_skills": trending_skills,
        "skill_gaps": skill_gaps
    }
    return make_response(jsonify(data), 200)
