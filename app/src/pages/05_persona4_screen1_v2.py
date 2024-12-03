import streamlit as st

st.set_page_config(
    page_title="Student Profiles",
    page_icon="👨‍🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Student Profiles")

# Student Search Section
st.subheader("Search Student Profiles")
student_name = st.text_input("Name:")
major = st.selectbox("Major:", ["Computer Science", "Finance", "Marketing", "Engineering"])
year = st.selectbox("Year:", ["Freshman", "Sophomore", "Junior", "Senior"])
skills = st.multiselect("Skills/Proficiency:", ["Python", "Excel", "Team Work", "SQL", "Leadership"])
if st.button("View Full Profile"):
    st.success("Displaying student profile... (Mock Data)")

# Skill Gap Analysis Section
st.subheader("Skill Gap Analysis")
missing_skills = st.multiselect("Missing Skills:", ["Machine Learning", "Data Visualization", "Public Speaking"])
if st.button("Analyze Gaps"):
    st.write("Skill Gap Analysis Completed (Mock Data)")

# Development Plan Section
st.subheader("Development Plan")
skills_to_improve = st.multiselect("Skills to Improve:", ["Team Work", "Discipline", "Public Speaking"])
recommended_resources = st.text_area("Recommended Resources:", "1. LinkedIn Learning\n2. Coursera\n3. DataCamp")
if st.button("Generate Plan"):
    st.success("Development Plan Generated!")

