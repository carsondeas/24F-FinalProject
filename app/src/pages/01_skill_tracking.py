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

# Job filter dropdown
job_filter = st.selectbox("Select Job Role", ["Software Developer", "Data Scientist", "Marketing Analyst"])

# Fetch user skills
def fetch_user_skills(user_id):
    try:
        response = requests.get(f"{API_BASE}/students/{user_id}/details")
        response.raise_for_status()
        skills_data = response.json()
        return [{"name": skill["skill"], "proficiency": skill.get("proficiency", "N/A")} for skill in skills_data]
    except Exception as e:
        st.error(f"Error fetching user skills: {e}")
        return []

# Fetch all available skills
def fetch_all_skills():
    try:
        response = requests.get(f"{API_BASE}/skills")
        response.raise_for_status()
        return [skill["skill"] for skill in response.json()]
    except Exception as e:
        st.error(f"Error fetching skills: {e}")
        return []

# Add a new skill for the user
def add_user_skill(user_id, skill_name):
    payload = {"skill": skill_name}
    try:
        response = requests.post(f"{API_BASE}/skills", json=payload)
        response.raise_for_status()
        st.success(f"Skill '{skill_name}' added successfully!")
    except Exception as e:
        st.error(f"Error adding skill: {e}")

# Update user profile
def update_user_skills(user_id, skills):
    payload = {"skills": skills}
    try:
        response = requests.put(f"{API_BASE}/students/{user_id}", json=payload)
        response.raise_for_status()
        st.success("User skills updated successfully!")
    except Exception as e:
        st.error(f"Error updating skills: {e}")

# Fetch data dynamically
user_id = 1  # Example logged-in user
user_skills = fetch_user_skills(user_id)
all_skills = fetch_all_skills()

# Display User Skills
st.subheader("Your Skills")
if user_skills:
    st.table(user_skills)
else:
    st.write("No skills found for the user.")

# Add a new skill
st.subheader("Add a New Skill")
new_skill_name = st.selectbox("Select a Skill to Add", [skill for skill in all_skills if skill not in [us["name"] for us in user_skills]])
if st.button("Add Skill"):
    add_user_skill(user_id, new_skill_name)

# Update User Skills
st.subheader("Update Your Skills")
selected_skills = st.multiselect("Select Skills", all_skills, default=[us["name"] for us in user_skills])
if st.button("Update Skills"):
    update_user_skills(user_id, selected_skills)
