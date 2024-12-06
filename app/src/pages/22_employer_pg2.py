import streamlit as st
import pandas as pd
import requests

# Flask API Base URL
API_BASE = "http://web-api:4000"

# Set page configuration
st.set_page_config(
    page_title="Search and Match Students",
    page_icon="🔍",
    layout="wide",
)

# Back Button
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("← Back"):
        st.write("Navigating back...")
        st.experimental_set_query_params(page='employer_home')  # Replace with your navigation logic
with col3:
    if st.button("🏠 Home"):
        st.write("Navigating to Home...")
        st.experimental_set_query_params(page='home')  # Replace with your navigation logic

st.title("Search and Match Students")

# Section: Filter Students by Skills
st.subheader("Find Candidates")

# Fetch majors from API
try:
    response = requests.get(f"{API_BASE}/students/studentsgetall")
    response.raise_for_status()
    majors_data = response.json()
    majors = ["All"] + list(set(student["major"] for student in majors_data))
except requests.exceptions.RequestException as e:
    st.error(f"Error fetching majors: {e}")
    majors = ["All"]

# Dropdown for filtering by major
major = st.selectbox("Filter by Major", majors)

# Fetch skills from API
try:
    response = requests.get(f"{API_BASE}/skills/all")
    response.raise_for_status()
    skills_data = response.json()
    available_skills = [skill["name"] for skill in skills_data]
except requests.exceptions.RequestException as e:
    st.error(f"Error fetching skills: {e}")
    available_skills = []

# Multiselect for filtering by skills
skills_required = st.multiselect("Required Skills", available_skills)

# Slider for proficiency level
proficiency_required = st.slider("Minimum Proficiency Level", min_value=1, max_value=5, value=3)

# Search button
if st.button("Search Candidates"):
    if skills_required:
        try:
            # Prepare payload
            payload = {
                "major": major if major != "All" else None,
                "skills": skills_required,
                "proficiency": proficiency_required,
            }

            # Call the API to fetch filtered candidates
            response = requests.get(f"{API_BASE}/students/filter", json=payload)
            response.raise_for_status()
            candidates_data = response.json()

            if candidates_data:
                # Convert data to DataFrame for display
                candidates_df = pd.DataFrame(candidates_data)
                st.table(candidates_df)
            else:
                st.warning("No candidates found matching the criteria.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error searching for candidates: {e}")
    else:
        st.warning("Please select at least one skill.")

# Pagination Buttons
col1, col2, col3 = st.columns([2, 6, 2])
with col1:
    if st.button("Previous"):
        st.write("Previous page...")  # Placeholder for pagination logic
with col3:
    if st.button("Next"):
        st.write("Next page...")  # Placeholder for pagination logic
