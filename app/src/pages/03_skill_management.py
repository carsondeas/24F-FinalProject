import streamlit as st
import requests
import pandas as pd
import altair as alt

# Set the API base URL
API_BASE = "http://web-api:4000"

# Page configuration
st.set_page_config(
    page_title="Skill Management",
    page_icon="⚙️",
    layout="wide",
)

st.title("Skill Management")

# Fetch all available skills
def fetch_all_skills():
    try:
        response = requests.get(f"{API_BASE}/skills/all")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching all skills: {e}")
        return []

# Fetch all skills for a user
def fetch_user_skills(nuid):
    try:
        response = requests.get(f"{API_BASE}/students/{nuid}/details")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching user skills: {e}")
        return []

# Add a skill for a user
def add_skill(user_id, skill_id, proficiency_level):
    payload = {"SkillID": skill_id, "ProficiencyLevel": proficiency_level}
    try:
        response = requests.post(f"{API_BASE}/students/{user_id}/skillsadd", json=payload)
        response.raise_for_status()
        st.success(f"Skill added successfully with proficiency level {proficiency_level}!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error adding skill: {e}")

# Update a user's skill proficiency level
def update_skill(user_id, skill_id, proficiency_level):
    payload = {"SkillID": skill_id, "ProficiencyLevel": proficiency_level}
    try:
        response = requests.put(f"{API_BASE}/students/{user_id}/skillsupdate", json=payload)
        response.raise_for_status()
        st.success(f"Skill updated successfully to proficiency level {proficiency_level}!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error updating skill: {e}")

# Remove skills for a user
def remove_skills(user_id, skill_ids):
    payload = {"SkillIDs": skill_ids}
    try:
        response = requests.delete(f"{API_BASE}/students/{user_id}/skillsdelete", json=payload)
        response.raise_for_status()
        st.success("Selected skills removed successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"Error removing skills: {e}")

# Main Section
user_id = 1  # Example user ID
all_skills = fetch_all_skills()
user_skills = fetch_user_skills(user_id)

# Update Skills Section
st.subheader("Update Your Skills")
if user_skills:
    user_skill_options = {skill["skill_name"]: skill["skillID"] for skill in user_skills}
    selected_skill = st.selectbox("Select a Skill to Update", options=list(user_skill_options.keys()))
    new_proficiency = st.slider("Select New Proficiency Level", min_value=1, max_value=5, step=1)
    if st.button("Update Skill"):
        update_skill(user_id, user_skill_options[selected_skill], new_proficiency)

# Add New Skills Section
st.subheader("Add New Skills")
available_skills = [skill for skill in all_skills if skill["name"] not in [s["skill_name"] for s in user_skills]]
if available_skills:
    add_skill_name = st.selectbox("Select a Skill to Add", [skill["name"] for skill in available_skills])
    add_proficiency = st.slider("Select Proficiency Level", min_value=1, max_value=5, step=1, key="add_slider")
    if st.button("Add Skill"):
        skill_id_to_add = next(skill["skillID"] for skill in available_skills if skill["name"] == add_skill_name)
        add_skill(user_id, skill_id_to_add, add_proficiency)

# Remove Skills Section
st.subheader("Remove Skills")
if user_skills:
    remove_skill_names = st.multiselect(
        "Select Skills to Remove",
        options=[skill["skill_name"] for skill in user_skills]
    )
    if st.button("Remove Selected Skills"):
        skill_ids_to_remove = [skill["skillID"] for skill in user_skills if skill["skill_name"] in remove_skill_names]
        remove_skills(user_id, skill_ids_to_remove)
