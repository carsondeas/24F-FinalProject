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

# Custom styles for better visuals
st.markdown("""
    <style>
    .back-button, .skill-management-button {
        text-align: center;
        margin: 10px auto;
    }
    .title {
        font-size: 2rem;
        font-weight: bold;
        color: #4A90E2;
    }
    .chart-container {
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Add navigation buttons in a clean layout
st.markdown('<div class="back-button">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 5])
with col1:
    if st.button("⬅ Back"):
        st.write("Navigating back...")
        st.switch_page('pages/00_Student_Home.py') # Redirect to previous page logic

# Page Title
st.markdown('<div class="title">Alex\'s Skills</div>', unsafe_allow_html=True)

# Fetch and display skills and proficiency chart
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

        # Display skills table
        st.subheader("Your Skills")
        st.table(df[["skill_name", "proficiencyLevel"]])

        # Create a bar chart for proficiency levels
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Skills Proficiency Chart")
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("proficiencyLevel:Q", title="Proficiency Level"),
            y=alt.Y("skill_name:O", title="Skill", sort="-x"),
            color=alt.Color("proficiencyLevel:Q", scale=alt.Scale(scheme="blues")),
            tooltip=["skill_name", "proficiencyLevel"]
        ).properties(
            width=800,
            height=400,
        )
        st.altair_chart(chart, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching user skills: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")


# Example logged-in user
user_id = 1
user_skills = fetch_and_display_skills(user_id)

# Fetch all available skills
def fetch_all_skills():
    try:
        response = requests.get(f"{API_BASE}/skills/all")
        response.raise_for_status()
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching skills: {e}")
        return []

# Fetch all skills for a specific user
def fetch_all_user_skills(nuid):
    try:
        response = requests.get(f"{API_BASE}/students/{nuid}/details")
        response.raise_for_status()
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching user skills: {e}")
        return []


if st.button('Manage Skills', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_skill_management.py')