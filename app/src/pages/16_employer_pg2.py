import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Search and Match Students",
    page_icon="🔍",
    layout="wide",
)

# Navigation buttons
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("← Back"):
        st.write("Navigating back...")
        st.switch_page('pages/14_employer_home') 
with col3:
    if st.button("🏠 Home"):
        st.write("Navigating to Home...")  
    st.switch_page('Home.py')

st.title("Search and Match Students")

# Section: Filter Students by Skills
st.subheader("Find Candidates")
major = st.selectbox("Filter by Major", ["All", "Computer Science", "Business", "Engineering"])
skills_required = st.multiselect("Required Skills", ["Python", "SQL", "Leadership"])
proficiency_required = st.slider("Minimum Proficiency Level", min_value=1, max_value=5, value=3)

if st.button("Search Candidates"):
    st.write(f"Searching candidates with skills: {', '.join(skills_required)} and proficiency ≥ {proficiency_required}...")
    # Placeholder for candidate results
    students = pd.DataFrame({
        "Name": ["Alice Green", "Bob Smith"],
        "GPA": [3.8, 3.6],
        "Skills": ["Python, SQL", "Leadership, SQL"],
        "Year": ["Junior", "Senior"],
    })
    st.table(students)

# Pagination
col1, col2, col3 = st.columns([2, 6, 2])
with col1:
    if st.button("Previous"):
        st.write("Previous page...")
with col3:
    if st.button("Next"):
        st.write("Next page...")
