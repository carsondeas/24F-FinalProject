from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Create a new Blueprint object for professors
professors = Blueprint('professors', __name__)

# Get all professors in the database
@professors.route('/professors', methods=['GET'])
def get_all_professors():
    query = 'SELECT id, name, department_id FROM Professors'
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return make_response(jsonify(data), 200)

# Add a professor
@professors.route('/professors', methods=['POST'])
def add_professor():
    """
    Add a new professor to the database.
    """
    the_data = request.json
    current_app.logger.info(f"Adding professor: {the_data}")

    query = '''
        INSERT INTO Professor (name, email, departmentID)
        VALUES (%s, %s, %s)
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (
            the_data['name'],
            the_data['email'],
            the_data['departmentID']
        ))
        db.get_db().commit()

        response = make_response("Professor added successfully", 201)
    except Exception as e:
        db.get_db().rollback()
        current_app.logger.error(f"Error adding professor: {e}")
        response = make_response({"error": str(e)}, 500)
    
    return response

# Update a professor
@professors.route('/<int:professorID>/update', methods=['PUT'])
def update_professor(professorID):
    """
    Update an existing professor's details.
    """
    the_data = request.json
    current_app.logger.info(f"Updating professor {professorID}: {the_data}")

    query = '''
        UPDATE Professor
        SET name = COALESCE(%s, name),
            email = COALESCE(%s, email),
            departmentID = COALESCE(%s, departmentID)
        WHERE professorID = %s
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (
            the_data.get('name'),
            the_data.get('email'),
            the_data.get('departmentID'),
            professorID
        ))
        db.get_db().commit()

        if cursor.rowcount == 0:
            response = make_response("Professor not found", 404)
        else:
            response = make_response("Professor updated successfully", 200)
    except Exception as e:
        db.get_db().rollback()
        current_app.logger.error(f"Error updating professor: {e}")
        response = make_response({"error": str(e)}, 500)

    return response


# Delete a professor
@professors.route('/<int:professorID>', methods=['DELETE'])
def delete_professor(professorID):
    """
    Delete a professor by their ID.
    """
    query = 'DELETE FROM Professor WHERE professorID = %s'
    current_app.logger.info(f"Deleting professor with ID: {professorID}")
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (professorID,))
        db.get_db().commit()

        if cursor.rowcount == 0:
            response = make_response("Professor not found", 404)
        else:
            response = make_response("Professor deleted successfully", 200)
    except Exception as e:
        db.get_db().rollback()
        current_app.logger.error(f"Error deleting professor: {e}")
        response = make_response({"error": str(e)}, 500)

    return response

# Get detailed information about a specific professor by their ID

@professors.route('/professors/<int:professor_id>', methods=['GET'])
def get_professor_by_id(professor_id):
    query = '''
        SELECT P.id, P.name, D.name AS department, GROUP_CONCAT(C.name) AS courses
        FROM Professors P
        LEFT JOIN Departments D ON P.department_id = D.id
        LEFT JOIN Courses C ON P.id = C.professor_id
        WHERE P.id = %s
        GROUP BY P.id, P.name, D.name
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (professor_id,))
    data = cursor.fetchone()
    if data:
        return make_response(jsonify(data), 200)
    else:
        return make_response("Professor not found", 404)