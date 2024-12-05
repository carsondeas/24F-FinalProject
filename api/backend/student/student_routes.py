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



# Remove a student from the database
@students.route('/<NUID>', methods=['DELETE'])
def delete_student(NUID):
    query = 'DELETE FROM Student WHERE NUID = %s'
    cursor = db.get_db().cursor()
    cursor.execute(query, (NUID,))
    db.get_db().commit()
    return make_response("Student removed successfully", 200)