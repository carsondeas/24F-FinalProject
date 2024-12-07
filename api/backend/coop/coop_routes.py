from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

coops = Blueprint('coops', __name__)


@coops.route('/getall', methods=['GET'])
def get_all_co_ops():
    query = '''
    SELECT C.jobID,  C.jobTitle, C.companyName,  C.industry, 
    GROUP_CONCAT(S.name SEPARATOR ', ') AS skillName
    FROM CoOp C
    LEFT JOIN (
        SELECT DISTINCT jobID, skillID FROM CoOp_Skill) 
        CS ON C.jobID = CS.jobID
        LEFT JOIN Skill S ON CS.skillID = S.skillID
        GROUP BY C.jobID, C.jobTitle, C.companyName, C.industry;

    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify([dict(row) for row in data]), 200)

# Find coop average proficiency level for each skill
@coops.route('/skills_avg_proficiency', methods=['GET'])
def get_coops_avg_proficiency():
    query = '''
        SELECT 
            S.name AS skillName,
            AVG(CoOp_Skill.proficiencyLevel) AS avgProficiencyLevel,
            COUNT(*) AS demandCount
        FROM CoOp_Skill
        JOIN Skill S ON CoOp_Skill.skillID = S.skillID
        GROUP BY S.name
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify([dict(row) for row in data]), 200)

@coops.route('/top_skills', methods=['GET'])
def get_top_skills():
    """
    Fetch the top skills required for co-op roles, grouped by industry and demand count.
    """
    query = '''
        SELECT 
            S.name AS skillName,
            COUNT(CS.jobID) AS demandCount,
            C.industry
        FROM Skill S
        JOIN CoOp_Skill CS ON S.skillID = CS.skillID
        JOIN CoOp C ON CS.jobID = C.jobID
        GROUP BY S.name, C.industry
        ORDER BY demandCount DESC;
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query)
        data = cursor.fetchall()

        # Format data into a list of dictionaries
        top_skills = [dict(row) for row in data]
        return make_response(jsonify(top_skills), 200)
    except Exception as e:
        current_app.logger.error(f"Error fetching top skills: {e}")
        return make_response({"error": "Failed to fetch top skills."}, 500)

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


@coops.route('/job_skills/<int:jobID>', methods=['GET'])
def get_job_skills_by_id(jobID):
    query = '''
        SELECT 
            CoOp.jobTitle AS "Job Title",
            CoOp.companyName AS "Company Name",
            CoOp.industry AS "Industry",
            Skill.name AS "Skill Name",
            CoOp_Skill.proficiencyLevel AS "Proficiency Level"
        FROM CoOp
        JOIN CoOp_Skill ON CoOp.jobID = CoOp_Skill.jobID
        JOIN Skill ON CoOp_Skill.skillID = Skill.skillID
        WHERE CoOp.jobID = %s;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (jobID,))
    data = cursor.fetchall()
    
    if not data:
        return make_response(jsonify({"message": "No skills found for the specified job ID"}), 404)
    
    return make_response(jsonify(data), 200)

@coops.route('/job_skills/<string:jobTitle>', methods=['GET'])
def get_job_skills_by_title(jobTitle):
    query = '''
        SELECT 
            CoOp.jobTitle AS "Job Title",
            CoOp.companyName AS "Company Name",
            CoOp.industry AS "Industry",
            Skill.name AS "Skill Name",
            CoOp_Skill.proficiencyLevel AS "Proficiency Level"
        FROM CoOp
        JOIN CoOp_Skill ON CoOp.jobID = CoOp_Skill.jobID
        JOIN Skill ON CoOp_Skill.skillID = Skill.skillID
        WHERE CoOp.jobTitle = %s;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (jobTitle,))
    data = cursor.fetchall()
    
    if not data:
        return make_response(jsonify({"message": "No skills found for the specified job ID"}), 404)
    
    return make_response(jsonify(data), 200)


@coops.route('/co_ops/<int:coop_id>', methods=['GET'])
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


@coops.route('/addrole', methods=['POST'])
def add_co_op():
    try:
        # Extract data from the incoming request
        data = request.json
        job_title = data.get('jobTitle')
        company_name = data.get('companyName')
        industry = data.get('industry')

        # Validate required fields
        if not job_title or not company_name or not industry:
            return make_response(jsonify({"error": "Missing required fields"}), 400)

        # Insert the new co-op into the CoOp table
        query = '''
            INSERT INTO CoOp (jobTitle, companyName, industry)
            VALUES (%s, %s, %s)
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query, (job_title, company_name, industry))
        db.get_db().commit()

        # Return success response
        return make_response(jsonify({"message": "Co-op opportunity added successfully"}), 201)

    except Exception as e:
        db.get_db().rollback()  # Rollback transaction in case of error
        return make_response(jsonify({"error": str(e)}), 500)

@coops.route('/<int:coop_id>', methods=['PUT'])
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

@coops.route('/add_skill', methods=['POST'])
def add_skill():
    data = request.json
    query = 'INSERT INTO CoOp_Skill (skillID, jobID, proficiencyLevel) VALUES (%s, %s, %s)'
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['skillID'], data['jobID'], data['proficiencyLevel']))
    db.get_db().commit()
    return make_response("Skill added successfully", 201)

@coops.route('/update_skill', methods=['PUT'])
def update_skill():
    data = request.json

    # Extracting the variables
    SkillID = data.get('skillID')
    JobID = data.get('jobID')
    ProficiencyLevel = data.get('proficiencyLevel')

    if not (SkillID and JobID and ProficiencyLevel is not None):  # Validate input
        return make_response("Missing required fields", 400)

    # Correct query syntax
    query = 'UPDATE CoOp_Skill SET proficiencyLevel = %s WHERE jobID = %s AND skillID = %s'
    cursor = db.get_db().cursor()

    try:
        # Correct order of arguments for the query
        cursor.execute(query, (ProficiencyLevel, JobID, SkillID))
        db.get_db().commit()
        return make_response("Skill updated successfully", 200)
    except Exception as e:
        db.get_db().rollback()
        return make_response(f"Error updating skill: {e}", 500)

@coops.route('/job_roles', methods=['GET'])
def get_job_roles():
    query = '''
        SELECT DISTINCT j.jobTitle AS job_role, GROUP_CONCAT(s.name) AS skills
        FROM CoOp j
        JOIN CoOp_Skill cs ON j.jobID = cs.jobID
        JOIN Skill s ON cs.skillID = s.skillID
        GROUP BY j.jobTitle
    '''
    cursor = db.get_db().cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # Convert comma-separated skills into a list for each job role
        formatted_results = [
            {"job_role": row["job_role"], "skills": row["skills"].split(",")}
            for row in results
        ]
        return make_response(jsonify(formatted_results), 200)
    except Exception as e:
        current_app.logger.error(f"Error fetching job roles: {e}")
        return make_response({"error": "Failed to fetch job roles."}, 500)
