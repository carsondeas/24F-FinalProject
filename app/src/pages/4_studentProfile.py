import streamlit as st
import requests
import pandas as pd

# Set the API base URL
API_BASE = "http://web-api:4000"

# Page configuration
st.set_page_config(
    page_title="Student Profiles",
    page_icon="🎓",
    layout="wide",
)

# Add navigation buttons
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("← Back"):
        st.write("Navigating back...")
        st.experimental_rerun()  # Replace with navigation logic
with col3:
    if st.button("🏠 Home"):
        st.write("Navigating to Home...")  # Replace with navigation logic

st.title("Student Profiles")

# Function to fetch student profiles
def fetch_student_profiles():
    try:
        response = requests.get(f"{API_BASE}/students/studentsgetall")
        response.raise_for_status()
        return response.json()  # Returns a list of students
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching student data: {e}")
        return []

# Function to fetch student skills
def fetch_student_skills(nuid):
    try:
        response = requests.get(f"{API_BASE}/students/{nuid}/details")
        response.raise_for_status()
        return response.json()  # Returns a list of skills for the student
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching student skills: {e}")
        return []
    
# Function to fetch co-op skills
def fetch_co_ops():
    try:
        response = requests.get(f"{API_BASE}/coops/getall")
        response.raise_for_status()
        return response.json()  # Returns a list of required skills for the job
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching co-op skills: {e}")
        return []

# Function to fetch co-op skills
def fetch_co_op_skills(job_title):
    try:
        response = requests.get(f"{API_BASE}/coops/job_skills/{job_title}")
        response.raise_for_status()
        return response.json()  # Returns a list of required skills for the job
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching co-op skills: {e}")
        return []

# Fetch all students
students = fetch_student_profiles()

# Convert student data to a searchable list
student_options = [f"{student['name']} (NUID: {student['NUID']})" for student in students]

# Searchable input for student selection
selected_student = st.selectbox(
    "Select a Student",
    options=[""] + student_options,  # Add an empty default option
    help="Search for a student by name or NUID"
)

# Select a student
if selected_student:
    selected_nuid = int(selected_student.split("NUID: ")[1][:-1])


    if selected_student:
        selected_nuid = int(selected_student.split("NUID: ")[1][:-1])
        student_skills = fetch_student_skills(selected_nuid)

        # Display student details
        st.subheader("Student Details")
        st.write(f"**Name:** {selected_student.split(' (')[0]}")
        st.write(f"**NUID:** {selected_nuid}")
        st.write("**Skills:**")
        if student_skills:      
            try:
                # Create a DataFrame with the correct keys
                student_skills_df = pd.DataFrame(student_skills, columns=["skill_name", "proficiencyLevel"])
                student_skills_df.rename(columns={"skill_name": "Skill Name", "proficiencyLevel": "Proficiency Level"}, inplace=True)
            
                # Remove the default index and display the table
                st.table(student_skills_df.style.hide(axis="index"))
            except KeyError as e:
                st.error(f"Error processing skills data: Missing key {e}")
        else:
            st.warning("No skills found for the selected student.")
        # Skill Gap Analysis
        st.subheader("Skill Gap Analysis")
        co_op_roles = fetch_co_ops()
        if co_op_roles:
            job_titles = [role['jobTitle'] for role in co_op_roles]
            selected_job_title = st.selectbox("Select a Job Title for Analysis", options=[""] + job_titles)

            if selected_job_title:
                required_skills = fetch_co_op_skills(selected_job_title)

                if required_skills:
                    required_skills_df = pd.DataFrame(required_skills, columns=["Skill Name", "Proficiency Level"])
                    st.write(f"**Required Skills for {selected_job_title}:**")
                    st.table(required_skills_df)

                    # Skill gap calculation
                    student_skill_names = student_skills_df["Skill Name"].tolist() if not student_skills_df.empty else []
                    required_skill_names = required_skills_df["Skill Name"].tolist() if not required_skills_df.empty else []
                    missing_skills = [skill for skill in required_skill_names if skill not in student_skill_names]

                    st.subheader("Missing Skills")
                    if missing_skills:
                        st.write(", ".join(missing_skills))
                    else:
                        st.success("The student has all required skills!")

        else:
            st.warning("No co-op roles available for skill gap analysis.")

        # Development Plan
        st.subheader("Development Plan")
        skills_to_improve = st.multiselect("Select Skills to Improve", [skill["skill_name"] for skill in student_skills])
        recommended_resources = st.text_area("Recommended Resources", "E.g., Courses, Books, Mentors")

        if st.button("Generate Plan"):
            st.write("### Development Plan")
            st.write(f"**Skills to Improve:** {', '.join(skills_to_improve)}")
            st.write(f"**Recommended Resources:** {recommended_resources}")
else:
    st.warning("No students available.")
