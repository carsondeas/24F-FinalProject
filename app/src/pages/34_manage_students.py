import streamlit as st
import requests
import pandas as pd

# Set the API base URL
API_BASE = "http://web-api:4000"

# Page configuration
st.set_page_config(
    page_title="Manage Students",
    page_icon="🎓",
    layout="wide",
)

# Define a Back Button
if st.button("Back"):
    st.write("Navigating back...")
    st.switch_page("pages/30_cpAdvisorHome.py")

st.title("Manage Students")

# Fetch all students
@st.cache_data
def fetch_all_students():
    try:
        response = requests.get(f"{API_BASE}/students/studentsgetall")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching students: {e}")
        return []

# Add a new student
def add_student(payload):
    try:
        response = requests.post(f"{API_BASE}/students/add", json=payload)
        response.raise_for_status()
        st.success("Student added successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error adding student: {e}")

# Update a student
def update_student(nuid, payload):
    try:
        response = requests.put(f"{API_BASE}/students/{nuid}/update", json=payload)
        response.raise_for_status()
        st.success("Student updated successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error updating student: {e}")

# Delete a student
def delete_student(nuid):
    try:
        response = requests.delete(f"{API_BASE}/students/{nuid}")
        response.raise_for_status()
        st.success("Student deleted successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error deleting student: {e}")

students = fetch_all_students()
student_options = {f"{s['name']} (NUID: {s['NUID']})": s['NUID'] for s in students}

# Section: Add a New Student
st.subheader("Add a New Student")
with st.form("add_student_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, step=0.1)
    major = st.text_input("Major")
    submitted = st.form_submit_button("Add Student")
    if submitted:
        if name and email and major:
            add_student({"name": name, "email": email, "GPA": gpa, "major": major})
        else:
            st.error("Please fill all required fields.")

# Section: Update an Existing Student
st.subheader("Update an Existing Student")
selected_student = st.selectbox("Select a Student to Update", options=[""] + list(student_options.keys()))
if selected_student:
    nuid = student_options[selected_student]
    with st.form(f"update_student_form_{nuid}"):
        update_name = st.text_input("New Name")
        update_email = st.text_input("New Email")
        update_gpa = st.number_input("New GPA", min_value=0.0, max_value=4.0, step=0.1)
        update_major = st.text_input("New Major")
        submitted = st.form_submit_button("Update Student")
        if submitted:
            payload = {
                "name": update_name or None,
                "email": update_email or None,
                "GPA": update_gpa if update_gpa > 0 else None,
                "major": update_major or None,
            }
            update_student(nuid, payload)

# Section: Delete a Student
st.subheader("Delete a Student")
selected_student_delete = st.selectbox("Select a Student to Delete", options=[""] + list(student_options.keys()))
if selected_student_delete:
    delete_nuid = student_options[selected_student_delete]
    if st.button("Delete Student"):
        delete_student(delete_nuid)