import streamlit as st
import requests

# Set the API base URL
API_BASE = "http://web-api:4000/courses"

# Page configuration
st.set_page_config(
    page_title="Course Management",
    page_icon="📚",
    layout="wide",
)

# Define a Back Button
if st.button("<- Back"):
    st.write("Navigating back...")
    st.switch_page('pages/10_Professor_Home.py')

st.title("Course Management")

# Fetch all courses assigned to the professor
def fetch_professor_courses(id):
    try:
        response = requests.get(f"{API_BASE}/{id}")
        response.raise_for_status()
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching professor courses: {e}")
        return []

# Add a new course for the professor
def add_course_to_professor(name, desc, id):
    try:
        data = {"name": name, "description": desc, "professorID": id}
        response = requests.post(f"{API_BASE}/add", json=data)
        response.raise_for_status()
        st.success(f"Course '{name}' added successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error adding course: {e}")

# Update a course description
def update_professor_course(id, course_id, desc):
    try:
        data = {"courseID": course_id, "professorID": id, "description": desc}
        response = requests.put(f"{API_BASE}/update", json=data)
        response.raise_for_status()
        st.success(f"Course with ID {course_id} updated successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error updating course: {e}")

# Remove a course
def remove_course_from_professor(id, course_id):
    try:
        response = requests.delete(f"{API_BASE}/delete/{course_id}", json={"professorID": id})
        response.raise_for_status()
        st.success(f"Course with ID {course_id} removed successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error removing course: {e}")


professor_id = 1  # Example logged-in professor

# Fetch professor's courses
professor_courses = fetch_professor_courses(professor_id)

# Section 1: Add a New Course
st.subheader("Add a New Course")
new_course_name = st.text_input("Course Name", placeholder="Enter the course name")
new_course_description = st.text_area("Course Description", placeholder="Enter a description for the course")

if st.button("Add Course"):
    if new_course_name and new_course_description:
        add_course_to_professor(new_course_name, new_course_description, professor_id)
    else:
        st.error("Please provide both a course name and description!")

# Section 2: Update Existing Course Description
st.subheader("Update Existing Course Description")
if professor_courses:
    course_options = {course["name"]: course["courseID"] for course in professor_courses}
    selected_course_name = st.selectbox("Select a Course to Update", options=list(course_options.keys()))

    if selected_course_name:
        selected_course_id = course_options[selected_course_name]
        updated_description = st.text_area("New Description", placeholder="Enter the new course description")
        
        if st.button("Update Description"):
            if updated_description:
                update_professor_course(professor_id, selected_course_id, updated_description)
            else:
                st.error("Please provide a new description!")
else:
    st.info("No courses assigned to you currently.")

# Section 3: Remove Existing Course
st.subheader("Remove a Course")
if professor_courses:
    course_options = {course["name"]: course["courseID"] for course in professor_courses}
    selected_course_to_remove = st.selectbox("Select a Course to Remove", options=list(course_options.keys()))

    if st.button("Remove Course"):
        if selected_course_to_remove:
            selected_course_id = course_options[selected_course_to_remove]
            remove_course_from_professor(professor_id, selected_course_id)
        else:
            st.error("Please select a course to remove!")
else:
    st.info("No courses assigned to you currently.")