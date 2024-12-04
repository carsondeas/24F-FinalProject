import streamlit as st
import requests
import pandas as pd
import altair as alt

# Set the API base URL
API_BASE = "http://localhost:4000"  # Ensure this matches your Docker setup

# Page configuration
st.set_page_config(
    page_title="Skill Tracking and Trends",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fetch job titles from API
def fetch_job_titles():
    try:
        response = requests.get(f"{API_BASE}/coops/name")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching job titles: {e}")
        return []
    
# Fetch skills based on selected job
def fetch_skills_for_job(job_title):
    try:
        response = requests.get(f"{API_BASE}/skills/job", params={"jobTitle": job_title})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching skills for job title '{job_title}': {e}")
        return []

# Dropdown for selecting job titles
st.subheader("Select a Job Title")
job_titles_data = fetch_job_titles()

if job_titles_data:
    job_titles = [f"{job['companyName']} - {job['jobTitle']}" for job in job_titles_data]
    selected_job = st.selectbox("Job Titles", job_titles)
else:
    st.write("No job titles available.")

# Show skills associated with the selected job
if selected_job:
    company, job_title = selected_job.split(" - ")
    skills = fetch_skills_for_job(job_title)
    st.subheader(f"Skills Required for '{job_title}' at {company}")
    if skills:
        st.table(skills)
    else:
        st.write(f"No skills available for the selected job: {job_title}")

        

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
        st.subheader("Your Skills Proficiency Chart")
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("proficiencyLevel:Q", title="Proficiency Level"),
            y=alt.Y("skill_name:O", title="Skill", sort="-x"),
            color=alt.Color("proficiencyLevel:Q", scale=alt.Scale(scheme="blues")),
            tooltip=["skill_name", "proficiencyLevel"]
        ).properties(
            width=600,
            height=400,
            title=f"Proficiency Levels for Student NUID {nuid}"
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
            skill_id = next((skill["skillID"] for skill in all_skills if skill["name"] == skill_name), None)
            
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


