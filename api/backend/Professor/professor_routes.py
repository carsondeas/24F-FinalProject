from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

# Create a new Blueprint object for professors
professors = Blueprint('professors', __name__)

# ------------------------------------------------------------
# Get all professors from the system
@professors.route('/professors', methods=['GET'])
def get_professors():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT professorID, name, email, departmentID FROM Professor''')

    the_data = cursor.fetchall()
    the_response = make_response(jsonify(the_data))
    the_response.status_code = 200
    return the_response

# ------------------------------------------------------------
# Update professor info for professor with a particular professorID
@professors.route('/professors', methods=['PUT'])
def update_professor():
    current_app.logger.info('PUT /professors route')
    prof_info = request.json
    prof_id = prof_info['professorID']
    name = prof_info['name']
    email = prof_info['email']
    department_id = prof_info['departmentID']

    query = '''UPDATE Professor 
               SET name = %s, email = %s, departmentID = %s 
               WHERE professorID = %s'''
    data = (name, email, department_id, prof_id)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    return 'Professor updated!'

# ------------------------------------------------------------
# Get professor detail for professor with a particular professorID
@professors.route('/professors/<professorID>', methods=['GET'])
def get_professor(professorID):
    current_app.logger.info(f'GET /professors/{professorID} route')
    cursor = db.get_db().cursor()
    cursor.execute(
        '''SELECT professorID, name, email, departmentID 
           FROM Professor 
           WHERE professorID = %s''', 
        (professorID,)
    )

    the_data = cursor.fetchall()
    the_response = make_response(jsonify(the_data))
    the_response.status_code = 200
    return the_response

# ------------------------------------------------------------
# Example prediction route for professors (hypothetical ML model)
@professors.route('/professors/prediction/<var01>/<var02>', methods=['GET'])
def predict_professor_value(var01, var02):
    current_app.logger.info(f'var01 = {var01}')
    current_app.logger.info(f'var02 = {var02}')

    # Call a hypothetical ML model (replace with your implementation)
    from backend.ml_models.model01 import predict
    return_val = predict(var01, var02)
    return_dict = {'result': return_val}

    the_response = make_response(jsonify(return_dict))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
