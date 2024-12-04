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
        SELECT Skill.name AS skill_name, Student_Skill.proficiencyLevel
        FROM Student_Skill
        JOIN Skill ON Student_Skill.skillID = Skill.skillID
        WHERE Student_Skill.NUID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (NUID,))
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

@students.route('/skill', methods=['POST'])
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


@students.route('/<int:NUID>/skillsupdate', methods=['PUT'])
def update_student_skill(NUID,proficiencyLevel):
    """
    Update an existing skill for a student.

    Args:
        NUID (int): The student's unique ID.
    Request Body:
        {
            "skillID": 1,
            "proficiencyLevel": 5
        }
    """
    data = request.json
    cursor = db.get_db().cursor()

    try:
        # Check if the skill exists for the student
        cursor.execute(
            'SELECT * FROM Student_Skill WHERE NUID = %s AND skillID = %s',
            (NUID, data['skillID'])
        )
        existing_skill = cursor.fetchone()

        if not existing_skill:
            return make_response({"error": "Skill does not exist for this student."}, 404)

        # Update the proficiency level for the existing skill
        cursor.execute(
            'UPDATE Student_Skill SET proficiencyLevel = %s WHERE NUID = %s AND skillID = %s',
            (data['proficiencyLevel'], NUID, data['skillID'])
        )
        db.get_db().commit()

        return make_response({"message": "Skill updated successfully."}, 200)

    except Exception as e:
        db.get_db().rollback()
        return make_response({"error": f"An error occurred: {e}"}, 500)

    finally:
        cursor.close()


# Remove a student from the database
@students.route('/<NUID>', methods=['DELETE'])
def delete_student(NUID):
    query = 'DELETE FROM Student WHERE NUID = %s'
    cursor = db.get_db().cursor()
    cursor.execute(query, (NUID,))
    db.get_db().commit()
    return make_response("Student removed successfully", 200)