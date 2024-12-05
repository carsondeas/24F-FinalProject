import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Student Profiles",
    page_icon="🎓",
    layout="wide",
)

# Add navigation buttons
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("← Back"):
        st.write("Navigating back...")
        st.experimental_rerun()  # Replace with navigation logic
with col2:
    st.text_input("Search")  # Placeholder for search functionality
with col3:
    if st.button("🏠 Home"):
        st.write("Navigating to Home...")  # Replace with navigation logic

st.title("Student Profiles")

# Input fields for student details
st.text_input("Name")
st.selectbox("Major", ["Computer Science", "Business", "Engineering", "Other"])
st.selectbox("Year", ["Freshman", "Sophomore", "Junior", "Senior", "Graduate"])
st.multiselect("Skills/Proficiency", ["Python", "SQL", "Data Analysis", "Project Management"])

if st.button("View Full Profile"):
    st.write("Displaying full student profile...")  # Replace with actual logic

# Skill Gap Analysis
st.subheader("Skill Gap Analysis")
missing_skills = st.multiselect("Missing Skills", ["Python", "SQL", "Machine Learning", "Leadership"])
if st.button("Analyze Skills"):
    st.write(f"Missing skills: {', '.join(missing_skills)}")  # Replace with actual analysis logic

# Development Plan
st.subheader("Development Plan")
skills_to_improve = st.multiselect("Skills to Improve", ["Python", "SQL", "Data Analysis", "Project Management"])
recommended_resources = st.text_area("Recommended Resources", "E.g., Courses, Books, Mentors")

if st.button("Generate Plan"):
    st.write("Development plan generated!")  # Replace with actual plan logic
