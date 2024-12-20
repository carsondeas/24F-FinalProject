from flask import Flask
from backend.db_connection import db
from backend.Professor.professor_routes import professors
from backend.courses.course_routes import courses
from backend.student.student_routes import students
from backend.skill.skill_routes import skills
from backend.coop.coop_routes import coops
import os
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    # Load environment variables
    load_dotenv()

    # Secret key for signing cookies and other security purposes
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Database configurations
    app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER').strip()
    app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_ROOT_PASSWORD').strip()
    app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST').strip()
    app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('DB_PORT'))
    app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME').strip()

    # Initialize the database object with the settings
    app.logger.info('Initializing the database connection...')
    db.init_app(app)

    # Register the routes from each Blueprint
    app.logger.info('Registering blueprints with the Flask app object...')
    app.register_blueprint(skills, url_prefix='/skills')
    app.register_blueprint(coops, url_prefix='/coops')
    app.register_blueprint(professors, url_prefix='/professors')
    app.register_blueprint(courses, url_prefix='/courses')
    app.register_blueprint(students, url_prefix='/students')

    # Return the app object
    return app
