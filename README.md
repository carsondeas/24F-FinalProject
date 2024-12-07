# SkillSeeker
By: Jon, Carson, Tyler, Jay, and Ian

SkillSeeker is an innovative application designed to help individuals explore, track, and develop their skills. Whether you're looking to learn a new craft, sharpen your coding abilities, or set personal development goals, SkillSeeker provides you with a structured pathway and the resources you need to grow.


## Getting Started

Clone the repository:
    git clone https://github.com/username/skillseeker.git

Navigate to project director:
    cd SkillSeeker

Create and start docker containers defined in docker-compose.yaml:
    docker compose up

This should launch the docker containers and the SQL database will be populated.
To view the Streamlit app on your local host go to your browser and type
    localhost:8501

This will bring you to the home page of SkillSeeker


# Prerequisites

Python - Required to run the backend server.

Streamlit - Required to run the frontend application.

SQL - Used for data storage.

Docker - Required if you want to run the application using Docker containers.

# Usage

Explore Skills: Browse through categories to find skills you're interested in learning.

Set Goals: Create personal milestones and set deadlines to keep your learning journey on track.

Track Progress: Visualize your progress with dynamic charts and status indicators.

Match with Co-Ops: Based on your skill set, find co-op opportunities that match your abilities and interests.

Skill Insights for Professors and Employers: Professors can access aggregated skill gap data, and employers can update skill requirements in real-time to find suitable candidates.

## Features

Skill Exploration: Discover new skills across a variety of categories, from technology and business to creative arts and personal growth.
Skill Tracking: Track your progress for each skill, set milestones, and receive reminders to help you stay on course.
Learning Pathways: Get personalized recommendations and learning pathways for different skills, tailored to your goals and experience level.

## Current Project Components

Currently, there are three major components which will each run in their own Docker Containers:

- Streamlit App in the `./app` directory
- Flask REST api in the `./api` directory
- SQL files for the database in the `./database-files` directory

## Project Architecture

SkillSeeker is built using a modern, scalable architecture to ensure a smooth and responsive user experience. Below is an overview of the main components:

# 1. Backend (API)

The backend server is implemented in Python using Flask as the web framework.

It provides RESTful APIs that handle operations related to users, skills, learning pathways, and progress tracking.

The database is implemented using SQL Database to store user data, skill information, milestones, and community posts.

Key endpoints include:

/api/coop
/api/courses
/api/Professor
/api/skill
/api/student

# 2. Frontend Application

The frontend is built using Streamlit, which provides an intuitive and interactive user interface for displaying data and managing user interactions.

Streamlit makes it easy to create forms, dashboards, and interactive components to explore skills and track progress in real-time.

Components such as skill cards, progress charts, and community features are designed to offer a user-friendly and engaging experience.

The use of Streamlit allows for quick deployment and a simplified structure, making it easy to modify and extend the application.

# 3. Database

SQL Database 'skillseeker' serves as the primary database. Information regarding professors, students, skills, coops, 
industries, and co-op advisors are stored here for use in our data-driven application.

# 4. Containerization and Deployment

Docker is used to containerize the application, ensuring consistent environments during development, testing, and production.

The docker-compose.yaml file defines the services required for the application, including the backend API, frontend UI, and SQL Database database.

This setup allows for seamless orchestration of services, making deployment and scaling easier.

# 5. Database Design and User Stories

The database design incorporates entities such as Users, Skills, Co-Ops, Professors, and Employers to capture the relationships and requirements identified in our user stories.

User stories for various personas have shaped the data model, ensuring that the database supports key features such as skill tracking, co-op matching, and analytics.

Relational Database Queries: Specific SQL queries are used to meet user requirements, such as viewing frequently requested skills, adding skills to profiles, updating proficiency levels, and finding students with specific competencies.



We hope you enjoy using SkillSeeker and that it helps you achieve your learning goals!