import streamlit as st
import pandas as pd
import requests

# Base API URL
API_BASE = "http://localhost:4000"

# Page configuration
st.set_page_config(
    page_title="Sarah's Skill Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Dashboard Header
st.title("Sarah's Dashboard for Skill Trends and Gaps")

# Fetch all departments
def fetch_departments():
    try:
        response = requests.get(f"{API_BASE}/departments")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching departments: {e}")
        return []

# Fetch department details by ID
def fetch_department_details(department_id):
    try:
        response = requests.get(f"{API_BASE}/departments/{department_id}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching department details: {e}")
        return {}

# Select a department
departments = fetch_departments()
if departments:
    department_options = {dept['name']: dept['id'] for dept in departments}
    selected_department_name = st.selectbox("Select a Department", list(department_options.keys()))
    selected_department_id = department_options[selected_department_name]

    # Fetch and display department details
    if st.button("Show Department Details"):
        department_details = fetch_department_details(selected_department_id)
        if department_details:
            st.write("### Department Details")
            st.write(f"**Name:** {department_details['name']}")
            st.write(f"**Professors:** {department_details.get('professors', 'None')}")
            st.write(f"**Courses:** {department_details.get('courses', 'None')}")
else:
    st.write("No departments available.")

# Section 2: Courses and Associated Skills
st.subheader("Courses and Associated Skills")
if st.button("View Courses"):
    try:
        response = requests.get(f"{API_BASE}/courses")
        response.raise_for_status()
        courses = response.json()
        courses_df = pd.DataFrame(courses)
        st.table(courses_df)
    except Exception as e:
        st.error(f"Error fetching courses: {e}")

# Section 3: Skill Gaps in Profiles
st.subheader("Skill Gaps in Profiles")
selected_course = st.selectbox("Select a Course", ["ACC 2301", "CS 3200", "NAZ CORE"])
if st.button("Analyze Skill Gaps"):
    try:
        response = requests.get(f"{API_BASE}/courses/{selected_course}/skill_gaps")
        response.raise_for_status()
        gap_data = response.json()
        gap_df = pd.DataFrame(gap_data)
        st.write("Skill Gaps for Selected Course")
        st.table(gap_df)
    except Exception as e:
        st.error(f"Error fetching skill gaps: {e}")

# Section 4: Update or Add Skills
st.subheader("Manage Skills")
manage_action = st.radio("Select Action", ["Update Skill", "Add Skill"])
if manage_action == "Update Skill":
    selected_skill = st.selectbox("Select a Skill to Update", ["Excel", "Teamwork", "Discipline"])
    new_proficiency = st.slider("Select New Proficiency Level", 1, 5, 3)
    if st.button("Update Skill"):
        try:
            response = requests.put(
                f"{API_BASE}/skills/{selected_skill}",
                json={"proficiency_level": new_proficiency}
            )
            response.raise_for_status()
            st.success("Skill updated successfully!")
        except Exception as e:
            st.error(f"Error updating skill: {e}")
elif manage_action == "Add Skill":
    new_skill_name = st.text_input("Skill Name")
    new_skill_level = st.slider("Proficiency Level", 1, 5, 3)
    if st.button("Add Skill"):
        try:
            response = requests.post(
                f"{API_BASE}/skills",
                json={"name": new_skill_name, "proficiency_level": new_skill_level}
            )
            response.raise_for_status()
            st.success("Skill added successfully!")
        except Exception as e:
            st.error(f"Error adding skill: {e}")
