import streamlit as st
import requests

# Set the API base URL
API_BASE = "http://web-api:4000"  # Ensure this matches your Docker setup

# Page configuration
st.set_page_config(
    page_title="Skill Tracking and Trends",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Skill Tracking and Trends")

# Fetch all skills from the API
def fetch_all_skills():
    try:
        response = requests.get(f"{API_BASE}/skills")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching all skills: {e}")
        return []

# Fetch a specific skill by ID
def fetch_skill_by_id(skill_id):
    try:
        response = requests.get(f"{API_BASE}/skills/{skill_id}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching skill by ID: {e}")
        return {}

# Add a new skill
def add_skill(skill_name):
    payload = {"skill": skill_name}
    try:
        response = requests.post(f"{API_BASE}/skills", json=payload)
        response.raise_for_status()
        st.success("Skill added successfully!")
    except Exception as e:
        st.error(f"Error adding skill: {e}")

# Display all skills
st.subheader("All Skills")
skills = fetch_all_skills()
if skills:
    for skill in skills:
        st.write(f"Skill: {skill[0]}")
else:
    st.write("No skills found.")

# Add a new skill section
st.subheader("Add a New Skill")
new_skill_name = st.text_input("Skill Name")
if st.button("Add Skill"):
    if new_skill_name:
        add_skill(new_skill_name)
    else:
        st.error("Please enter a skill name.")

# Fetch skill by ID
st.subheader("Fetch Skill by ID")
skill_id = st.number_input("Skill ID", min_value=1, step=1)
if st.button("Get Skill by ID"):
    skill = fetch_skill_by_id(skill_id)
    if skill:
        st.write(f"Skill ID: {skill['id']}, Skill Name: {skill['skill']}")
    else:
        st.write("No skill found for this ID.")
