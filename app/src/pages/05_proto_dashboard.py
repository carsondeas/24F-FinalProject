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
        departments = response.json()
        # Ensure unique departments based on departmentID
        unique_departments = {dept['departmentID']: dept for dept in departments}.values()
        return list(unique_departments)
    except Exception as e:
        st.error(f"Error fetching departments: {e}")
        return []

# Fetch department details by ID
def fetch_department_details(department_id):
    try:
        response = requests.get(f"{API_BASE}/departments/{department_id}")
        response.raise_for_status()
        department_details = response.json()
        if not department_details:
            st.warning("No details found for this department.")
            return {}
        return department_details
    except Exception as e:
        st.error(f"Error fetching department details: {e}")
        return {}

# Fetch departments
departments = fetch_departments()
if departments:
    department_options = {dept['name']: dept['departmentID'] for dept in departments}  # Adjust key for ID if needed
    selected_department_name = st.selectbox("Select a Department", list(department_options.keys()))
    selected_department_id = department_options[selected_department_name]

# Show Department Details Button
    if st.button("Show Department Details"):
        department_details = fetch_department_details(selected_department_id)

        if department_details:
            # Ensure expected fields are present in the API response
            department_name = department_details.get('department_name', 'Unknown Name')
            professors = department_details.get('professors', [])
            courses = department_details.get('courses', [])

            # Display the department details
            st.write("### Department Details")
            st.write(f"**Name:** {department_name}")
            st.write(f"**Professors:** {', '.join(professors) if professors else 'None'}")
            st.write(f"**Courses:** {', '.join(courses) if courses else 'None'}")
        else:
            st.write("No details found for the selected department.")
else:
    st.warning("No departments available to select.")

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
