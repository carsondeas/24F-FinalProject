from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

students = Blueprint('students', __name__)

@students.route('/studentsgetall', methods=['GET'])
def get_students():
    query = 'SELECT NUID, name, email, GPA, major FROM Student'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

# Find student average proficiency level for each skill
@students.route('/skills_avg_proficiency', methods=['GET'])
def get_students_avg_proficiency():
    query = '''
        SELECT 
            S.name AS skillName,
            AVG(SS.proficiencyLevel) AS avgProficiencyLevel
        FROM Student_Skill SS
        JOIN Skill S ON SS.skillID = S.skillID
        GROUP BY S.name
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify([dict(row) for row in data]), 200)

# Add a new student
@students.route('/add', methods=['POST'])
def add_student():
    data = request.json
    query = '''
        INSERT INTO Student (name, email, GPA, major)
        VALUES (%s, %s, %s, %s)
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (data['name'], data['email'], data['GPA'], data['major']))
    db.get_db().commit()
    return make_response("Student added successfully", 201)

@students.route('/<int:NUID>/details', methods=['GET'])
def get_student_details(NUID):
    query = '''
        SELECT Skill.name AS skill_name, Student_Skill.proficiencyLevel, Skill.skillID
        FROM Student_Skill
        JOIN Skill ON Student_Skill.skillID = Skill.skillID
        WHERE Student_Skill.NUID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (NUID,))
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

@students.route('/addskill', methods=['POST'])
def add_skill_for_student():
    """
    Add a new skill for a student.
    """
    # Collecting data from the request object
    the_data = request.json

    # Extracting the variables
    NUID = the_data.get('NUID')  # Student ID
    SkillID = the_data.get('SkillID')  # Skill ID
    ProficiencyLevel = the_data.get('ProficiencyLevel')  # Proficiency Level

    # Validate input
    if not all([NUID, SkillID, ProficiencyLevel]):
        return {"error": "NUID, SkillID, and ProficiencyLevel are required."}, 400

    # Constructing the query
    query = '''
        INSERT INTO Student_Skill (NUID, skillID, proficiencyLevel) 
        VALUES (%s, %s, %s)
    '''

    # Executing and committing the query
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (NUID, SkillID, ProficiencyLevel))
        db.get_db().commit()

        return {"message": "Skill added successfully."}, 201
    except Exception as e:
        db.get_db().rollback()
        current_app.logger.error(f"Error adding skill: {e}")
        return {"error": f"An error occurred: {str(e)}"}, 500



@students.route('/updateskill', methods=['PUT'])
def update_skill_for_student():
    """
    Add a new skill for a student.
    """
    # Collecting data from the request object
    the_data = request.json

    # Extracting the variables
    NUID = the_data.get('NUID')  # Student ID
    SkillID = the_data.get('SkillID')  # Skill ID
    ProficiencyLevel = the_data.get('ProficiencyLevel')  # Proficiency Level

    # Validate input
    if not all([NUID, SkillID, ProficiencyLevel]):
        return {"error": "NUID, SkillID, and ProficiencyLevel are required."}, 400

    # Check if the skill already exists for the student
    query_check = '''
        SELECT * FROM Student_Skill
        WHERE NUID = %s AND skillID = %s
    '''
    query_update = '''
        UPDATE Student_Skill
        SET proficiencyLevel = %s
        WHERE NUID = %s AND skillID = %s
    '''
    query_insert = '''
        INSERT INTO Student_Skill (NUID, skillID, proficiencyLevel)
        VALUES (%s, %s, %s)
    '''

    try:
        cursor = db.get_db().cursor()
        cursor.execute(query_check, (NUID, SkillID))
        existing_skill = cursor.fetchone()

        if existing_skill:
            # Skill exists, update proficiency level
            cursor.execute(query_update, (ProficiencyLevel, NUID, SkillID))
            message = "Skill updated successfully."
        else:
            # Skill does not exist, insert new skill
            cursor.execute(query_insert, (NUID, SkillID, ProficiencyLevel))
            message = "Skill added successfully."

        db.get_db().commit()
        return {"message": message}, 200

    except Exception as e:
        db.get_db().rollback()
        current_app.logger.error(f"Error adding or updating skill: {e}")
        return {"error": f"An error occurred: {str(e)}"}, 500

# Update student attributes from the database
@students.route('/<int:NUID>/update', methods=['PUT'])
def update_student(NUID):
    """
    Update a student's details, such as name, email, GPA, or major.
    """
    data = request.json

    # Check if at least one field is provided for the update
    allowed_fields = ['name', 'email', 'GPA', 'major']
    updates = {field: data[field] for field in allowed_fields if field in data}

    if not updates:
        return {"error": "No valid fields provided for update. Allowed fields: name, email, GPA, major."}, 400

    # Build the SQL query dynamically based on the fields to be updated
    update_clauses = ", ".join([f"{field} = %s" for field in updates.keys()])
    query = f"UPDATE Student SET {update_clauses} WHERE NUID = %s"

    # Add values for the placeholders in the query
    values = list(updates.values()) + [NUID]

    # Execute the update query
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, values)
        db.get_db().commit()
        return {"message": "Student details updated successfully."}, 200
    except Exception as e:
        db.get_db().rollback()
        current_app.logger.error(f"Error updating student {NUID}: {e}")
        return {"error": f"An error occurred while updating the student: {str(e)}"}, 500

# Remove a student from the database
@students.route('/<NUID>', methods=['DELETE'])
def delete_student(NUID):
    try:
        # Check if the student exists
        check_query = 'SELECT * FROM Student WHERE NUID = %s'
        cursor = db.get_db().cursor()
        cursor.execute(check_query, (NUID,))
        student = cursor.fetchone()
        
        if not student:
            return make_response({"error": f"Student with NUID {NUID} does not exist."}, 404)
        
        # Delete the student
        delete_query = 'DELETE FROM Student WHERE NUID = %s'
        cursor.execute(delete_query, (NUID,))
        db.get_db().commit()
        
        return make_response({"message": f"Student with NUID {NUID} removed successfully."}, 200)
    
    except Exception as e:
        db.get_db().rollback()  # Rollback any changes in case of error
        current_app.logger.error(f"Error deleting student with NUID {NUID}: {e}")
        return make_response({"error": "An error occurred while deleting the student."}, 500)

@students.route('/<int:NUID>/skillsdelete', methods=['DELETE'])
def delete_selected_user_skills(NUID):
    """
    Remove selected skills associated with a specific user.
    """
    # Get the list of skills to delete from the request body
    skill_ids = request.json.get('SkillIDs', [])

    if not skill_ids:
        return make_response("No skills specified for deletion.", 400)

    try:
        query = 'DELETE FROM Student_Skill WHERE NUID = %s AND skillID IN ({})'.format(
            ', '.join(['%s'] * len(skill_ids))
        )
        cursor = db.get_db().cursor()
        cursor.execute(query, (NUID, *skill_ids))
        db.get_db().commit()
        return make_response("Selected skills removed successfully.", 200)
    except Exception as e:
        db.get_db().rollback()
        current_app.logger.error(f"Error removing selected skills for user {NUID}: {e}")
        return make_response(f"An error occurred: {e}", 500)
