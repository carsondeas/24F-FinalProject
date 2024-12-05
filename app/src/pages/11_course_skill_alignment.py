import streamlit as st
import requests

API_BASE = "http://web-api:4000"

st.set_page_config(page_title="Course Skill Alignment", page_icon="📚", layout="wide")

st.title("Course Skill Alignment")

# Fetch Courses
def fetch_courses():
    try:
        response = requests.get(f"{API_BASE}/courses/courses")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching courses: {e}")
        return []

# Fetch Co-op Skills
def fetch_co_op_skills():
    try:
        response = requests.get(f"{API_BASE}/coops/co_ops")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching co-op skills: {e}")
        return []

# Fetch Data
courses = fetch_courses()
co_ops = fetch_co_op_skills()

# Display Course Skill Alignment
st.subheader("Course Skill vs. Industry Demands")
for course in courses:
    st.write(f"**Course:** {course['name']}")
    course_skills = course['description'].split(",")  # Assuming skills are listed in description
    matching_co_ops = [
        co_op for co_op in co_ops if any(skill in co_op['skills'] for skill in course_skills)
    ]
    if matching_co_ops:
        st.write("**Relevant Co-op Roles:**")
        for co_op in matching_co_ops:
            st.write(f"- {co_op['title']} at {co_op['company']}")
    else:
        st.write("No relevant co-op roles found.")
