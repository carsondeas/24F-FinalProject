import streamlit as st
import requests
import pandas as pd

# Set the API base URL
API_BASE = "http://web-api:4000"

# Page configuration
st.set_page_config(
    page_title="Manage Professors",
    page_icon="👨‍🏫",
    layout="wide",
)

# Define a Back Button
if st.button("Back"):
    st.write("Navigating back...")
    st.switch_page("pages/30_cpAdvisorHome.py")

st.title("Manage Professors")

# Fetch all professors
@st.cache_data
def fetch_all_professors():
    try:
        response = requests.get(f"{API_BASE}/professors/professorsgetall")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching professors: {e}")
        return []

# Add a new professor
def add_professor(payload):
    try:
        response = requests.post(f"{API_BASE}/professors/add", json=payload)
        response.raise_for_status()
        st.success("Professor added successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error adding professor: {e}")

# Update a professor
def update_professor(professor_id, payload):
    try:
        response = requests.put(f"{API_BASE}/professors/{professor_id}/update", json=payload)
        response.raise_for_status()
        st.success("Professor updated successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error updating professor: {e}")

# Delete a professor
def delete_professor(professor_id):
    try:
        response = requests.delete(f"{API_BASE}/professors/{professor_id}/delete")
        response.raise_for_status()
        st.success("Professor deleted successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error deleting professor: {e}")

professors = fetch_all_professors()
professor_options = {f"{p['name']} (ID: {p['professorID']})": p['professorID'] for p in professors}

# Section: Add a New Professor
st.subheader("Add a New Professor")
with st.form("add_professor_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    department_id = st.text_input("Department ID")
    submitted = st.form_submit_button("Add Professor")
    if submitted:
        if name and email and department_id:
            add_professor({"name": name, "email": email, "departmentID": department_id})
        else:
            st.error("Please fill all required fields.")

# Section: Update an Existing Professor
st.subheader("Update an Existing Professor")
selected_professor = st.selectbox("Select a Professor to Update", options=[""] + list(professor_options.keys()))
if selected_professor:
    professor_id = professor_options[selected_professor]
    with st.form(f"update_professor_form_{professor_id}"):
        update_name = st.text_input("New Name")
        update_email = st.text_input("New Email")
        update_department_id = st.text_input("New Department ID")
        submitted = st.form_submit_button("Update Professor")
        if submitted:
            payload = {
                "name": update_name or None,
                "email": update_email or None,
                "departmentID": update_department_id or None,
            }
            update_professor(professor_id, payload)

# Section: Delete a Professor
st.subheader("Delete a Professor")
selected_professor_delete = st.selectbox("Select a Professor to Delete", options=[""] + list(professor_options.keys()))
if selected_professor_delete:
    delete_professor_id = professor_options[selected_professor_delete]
    if st.button("Delete Professor"):
        delete_professor(delete_professor_id)