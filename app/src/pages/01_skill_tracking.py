import streamlit as st
import requests
import pandas as pd
import altair as alt

# Set the API base URL
API_BASE = "http://web-api:4000"  # Ensure this matches your Docker setup

# Page configuration
st.set_page_config(
    page_title="Skill Tracking and Trends",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Alex's Skills")


def fetch_and_display_skills(nuid):
    """
    Fetch a student's skills and proficiency levels from the API and display them
    as a table and a bar chart in Streamlit.

    Args:
        nuid (int): The student's unique ID (NUID).
    """
    try:
        # Fetch skills data from the API
        response = requests.get(f"{API_BASE}/students/{nuid}/details")
        response.raise_for_status()
        skills_data = response.json()
        
        if not skills_data:
            st.warning(f"No skills found for student with NUID {nuid}.")
            return

        # Convert skills data to a DataFrame
        df = pd.DataFrame(skills_data)

        # Create a bar chart for proficiency levels
        st.subheader("Skills Proficiency Chart")
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("proficiencyLevel:Q", title="Proficiency Level"),
            y=alt.Y("skill_name:O", title="Skill", sort="-x"),
            color=alt.Color("proficiencyLevel:Q", scale=alt.Scale(scheme="blues")),
            tooltip=["skill_name", "proficiencyLevel"]
        ).properties(
            width=600,
            height=400,
        )

        st.altair_chart(chart, use_container_width=True)

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching user skills: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

user_id = 1  # Example logged-in user
user_skills = fetch_and_display_skills(user_id)
# Fetch all available skills
def fetch_all_skills():
    try:
        response = requests.get(f"{API_BASE}/skills/all")
        response.raise_for_status()
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching students: {e}")
        return []
    
# Fetch all available skills
def fetch_all_user_skills(nuid):
    try:
        response = requests.get(f"{API_BASE}/students/{nuid}/details")
        response.raise_for_status()
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching students: {e}")
        return []

# Add a new skill for the user
def add_user_skill(user_id, skill_data):
    """
    Adds a new skill for the user.
    
    Args:
        user_id (int): User's ID.
        skill_data (dict): Dictionary containing skillID and proficiencyLevel.
    """
    try:
        response = requests.post(f"{API_BASE}/students/{user_id}/skillsadd", json=skill_data)
        response.raise_for_status()
        st.success(f"Skill '{skill_data['skillID']}' with proficiency level {skill_data['proficiencyLevel']} added successfully!")
    except Exception as e:
        st.error(f"Error adding skill: {e}")

# Update user skills
def update_user_skills(user_id, skill_data):
    """
    Updates an existing skill for the user.
    
    Args:
        user_id (int): User's ID.
        skill_data (dict): Dictionary containing skillID and proficiencyLevel.
    """
    try:
        response = requests.put(f"{API_BASE}/students/{user_id}/skillsupdate", json=skill_data)
        response.raise_for_status()
        st.success(f"Skill '{skill_data['skillID']}' updated to proficiency level {skill_data['proficiencyLevel']}!")
    except Exception as e:
        st.error(f"Error updating skills: {e}")

# Fetch all available skills
all_skills = fetch_all_skills()
all_user_skills = fetch_all_user_skills(user_id)
# Extract skill names for the user
user_skill_names = [us["skill_name"] for us in all_user_skills]

# Update user skills with proficiency levels
st.subheader("Update Your Skills")

# Create a dictionary to store proficiency levels for all selected skills
proficiency_levels = {}

# Display multiselect for skills
selected_skills = st.multiselect(
    "Select Skills",
    user_skill_names,
)

# Dynamically display sliders for proficiency levels and call update skills
if selected_skills:
    st.subheader("Set Proficiency Levels")
    
    # Create sliders for each selected skill and collect updated proficiency levels
    for skill_name in selected_skills:
        proficiency_levels[skill_name] = st.slider(
            f"Proficiency for {skill_name}",
            min_value=1,
            max_value=5,
            value=next(
                (us["proficiencyLevel"] for us in all_user_skills if us["skill_name"] == skill_name),
                3  # Default to 3 if no existing proficiency level is found
            ),
            step=1
        )

    # Handle form submission for updating skills
    if st.button("Update Skills"):
        for skill_name, proficiency_level in proficiency_levels.items():
            # Find the corresponding skillID
            skill_id = next((skill["skillId"] for skill in all_skills if skill["name"] == skill_name), None)
            
            # Prepare the payload for updating the skill
            payload = {
                "NUID": int(user_id),  # Replace with the actual NUID variable
                "SkillID": skill_id,
                "ProficiencyLevel": proficiency_level
            }

            # Call the update API
            try:
                response = requests.put(f"{API_BASE}/students/updateskill", json=payload)
                response.raise_for_status()
                st.success(f"Skill '{skill_name}' updated successfully to level {proficiency_level}!")
            except requests.exceptions.RequestException as e:
                st.error(f"Error updating skill '{skill_name}': {e}")

# Subheader for adding new skills
st.subheader("Add New Skills")

# Fetch all skills that the user does not currently have
available_skills = [skill["name"] for skill in all_skills if skill["name"] not in user_skill_names]

# Multiselect for new skills
new_skills = st.multiselect(
    "Select Skills to Add",
    available_skills,
    help="Select skills you want to add."
)

# Dynamically display sliders for proficiency levels for new skills
new_proficiency_levels = {}
if new_skills:
    st.subheader("Set Proficiency Levels for New Skills")
    for skill_name in new_skills:
        new_proficiency_levels[skill_name] = st.slider(
            f"Proficiency for {skill_name}",
            min_value=1,
            max_value=5,
            value=3,  # Default proficiency level
            step=1
        )

    # Handle form submission for adding new skills
    if st.button("Add Skills"):
        for skill_name, proficiency_level in new_proficiency_levels.items():
            # Find the corresponding skillID
            skill_id = next((skill["skillId"] for skill in all_skills if skill["name"] == skill_name), None)
            
            # Prepare the payload for adding the skill
            payload = {
                "NUID": int(user_id),  # Replace with the actual NUID variable
                "SkillID": skill_id,
                "ProficiencyLevel": proficiency_level
            }

            # Call the add API
            try:
                response = requests.post(f"{API_BASE}/students/addskill", json=payload)
                response.raise_for_status()
                st.success(f"Skill '{skill_name}' added successfully with proficiency level {proficiency_level}!")
            except requests.exceptions.RequestException as e:
                st.error(f"Error adding skill '{skill_name}': {e}")

# Subheader for removing specific skills
st.subheader("Remove Selected Skills for a Student")

# Fetch all skills for the user
user_skills = fetch_all_user_skills(user_id)

# Multiselect to choose skills to delete
if user_skills:
    skill_options = {skill["skill_name"]: skill["skillID"] for skill in user_skills}
    selected_skills = st.multiselect(
        "Select Skills to Remove",
        options=skill_options.keys(),
        help="Choose the skills you want to delete."
    )

    # Handle deletion
    if st.button("Remove Selected Skills"):
        skill_ids_to_delete = [skill_options[skill_name] for skill_name in selected_skills]

        # Prepare payload
        payload = {
            "SkillIDs": skill_ids_to_delete
        }

        # Send DELETE request
        try:
            response = requests.delete(f"{API_BASE}/students/{user_id}/skillsdelete", json=payload)
            response.raise_for_status()
            st.success(f"Selected skills removed successfully!")
        except requests.exceptions.RequestException as e:
            st.error(f"Error removing selected skills: {e}")
else:
    st.info("No skills available to remove.")


