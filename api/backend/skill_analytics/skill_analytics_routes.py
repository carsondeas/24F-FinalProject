from flask import Blueprint, jsonify, make_response
from backend.db_connection import db

skills_analytics = Blueprint('skills_analytics', __name__)

# Get aggregated data on trending skills or skill gaps
@skills_analytics.route('/skills/analytics', methods=['GET'])
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
