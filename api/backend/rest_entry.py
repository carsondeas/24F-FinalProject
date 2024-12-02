from flask import Flask
from backend.db_connection import db
from backend.departments.department_routes import departments
from backend.professors.professor_routes import professors
from backend.courses.course_routes import courses
from backend.students.student_routes import students
import os
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    # Load environment variables
    load_dotenv()

    # Secret key for signing cookies and other security purposes
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

    # Database configurations
    app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER', 'root').strip()
    app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_ROOT_PASSWORD', '').strip()
    app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST', 'localhost').strip()
    app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('DB_PORT', 3306))
    app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME', 'skillseeker').strip()

    # Initialize the database object with the settings
    app.logger.info('Initializing the database connection...')
    db.init_app(app)

    # Register the routes from each Blueprint
    app.logger.info('Registering blueprints with the Flask app object...')
    app.register_blueprint(departments, url_prefix='/departments')
    app.register_blueprint(professors, url_prefix='/professors')
    app.register_blueprint(courses, url_prefix='/courses')
    app.register_blueprint(students, url_prefix='/students')

    # Return the app object
    return app
