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
# Define a Back Button
if st.button("Back"):
    # Logic for the back button
    st.write("Navigating back...")
    # Redirect or reset the page state (Example: Use navigation logic here)
    st.switch_page('pages/00_Student_Home.py')  # Reload the page

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

if st.button('Skill Management',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/04_skill_management.py')