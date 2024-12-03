import streamlit as st
import requests
import json

# Set the page configuration to wide
st.set_page_config(
    page_title="Skill Tracking and Trends",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# API base URL
API_BASE = "http://localhost:4000"  # Ensure your Flask API is running on this address and port

st.title("Skill Tracking and Trends")

# Job Filter Dropdown
job_filter = st.selectbox(
    "Job Filter", 
    ["Software Developer", "Data Scientist", "Marketing Analyst"]
)

# Fetch company matches from API
def fetch_company_matches(job_filter):
    try:
        endpoint = f"{API_BASE}/companies?job_filter={job_filter.replace(' ', '_')}"
        response = requests.get(endpoint)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.ConnectionError:
        st.error("Unable to connect to the API. Please ensure the Flask server is running on port 4000.")
        return []
    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP error occurred: {e}")
        return []
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return []

# Fetch user skills from API
def fetch_user_skills(user_id):
    try:
        endpoint = f"{API_BASE}/skills?user_id={user_id}"
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        st.error("Unable to connect to the API. Please ensure the Flask server is running.")
        return []
    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP error occurred: {e}")
        return []
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return []

# Fetch trending skills from API
def fetch_trending_skills(job_filter):
    try:
        endpoint = f"{API_BASE}/trending_skills?job_filter={job_filter.replace(' ', '_')}"
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        st.error("Unable to connect to the API. Please ensure the Flask server is running.")
        return []
    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP error occurred: {e}")
        return []
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return []

# Fetch data dynamically
st.write("Fetching data from the API...")
company_matches = fetch_company_matches(job_filter)
user_skills = fetch_user_skills(user_id=1)  # Assume a logged-in user with ID 1
trending_skills = fetch_trending_skills(job_filter)

# Display Company Matches
st.subheader("Company Matches")
if company_matches:
    for company in company_matches:
        st.write(f"**{company['name']}** - Match Score: {company['score']}")
else:
    st.write("No company matches found.")

# Display User Skills
st.subheader("Your Skills")
if user_skills:
    for skill in user_skills:
        st.write(f"**{skill['name']}** - Proficiency: {skill['proficiency']}")
else:
    st.write("No skills found for the selected user.")

# Add Skill (for demonstration, no backend connected yet)
st.text_input("Add a New Skill (Not Implemented)")

# Display Trending Skills
st.subheader("Trending Skills")
if trending_skills:
    for skill in trending_skills:
        st.write(f"**{skill['name']}** - Popularity: {skill['popularity']}%")
else:
    st.write("No trending skills found.")

# Update user skill dynamically
def update_user_skill(skill_name, proficiency):
    try:
        endpoint = f"{API_BASE}/skills"
        data = {"user_id": 1, "skill_name": skill_name, "proficiency": proficiency}
        response = requests.put(endpoint, json=data)
        response.raise_for_status()
        st.success("Skill updated successfully!")
    except requests.exceptions.ConnectionError:
        st.error("Unable to connect to the API. Please ensure the Flask server is running.")
    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP error occurred: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

# Section to update skill
if user_skills:
    st.subheader("Update Skill")
    skill_name = st.selectbox("Select Skill to Update", [skill['name'] for skill in user_skills])
    proficiency = st.slider("Proficiency Level", 0, 10, 5)
    if st.button("Update Skill"):
        update_user_skill(skill_name, proficiency)
else:
    st.write("No skills available to update.")
