import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Skill Gaps",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Skill Gap & Preparedness Tracker")

# Define data for each course
course_data = {
    "CS 3200": {
        "matched_skills": [{"Skill": "SQL", "Proficiency": 9}, {"Skill": "Python", "Proficiency": 8}],
        "gap_skills": [{"Skill": "Data Visualization", "Gap": 3}, {"Skill": "Machine Learning", "Gap": 4}],
        "company_skills": [
            {"Skill": "Python", "Proficiency": 9},
            {"Skill": "Data Structures", "Proficiency": 8},
            {"Skill": "Problem Solving", "Proficiency": 7},
        ],
    },
    "ACCT 2301": {
        "matched_skills": [{"Skill": "Excel", "Proficiency": 10}, {"Skill": "Financial Analysis", "Proficiency": 8}],
        "gap_skills": [{"Skill": "Leadership", "Gap": 4}, {"Skill": "Public Speaking", "Gap": 3}],
        "company_skills": [
            {"Skill": "Excel", "Proficiency": 10},
            {"Skill": "Financial Literacy", "Proficiency": 9},
            {"Skill": "Leadership", "Proficiency": 8},
        ],
    },
    "MKTG 3301": {
        "matched_skills": [{"Skill": "SEO", "Proficiency": 8}, {"Skill": "Content Creation", "Proficiency": 7}],
        "gap_skills": [{"Skill": "Analytics Tools", "Gap": 3}, {"Skill": "Storytelling", "Gap": 2}],
        "company_skills": [
            {"Skill": "SEO", "Proficiency": 9},
            {"Skill": "Content Creation", "Proficiency": 8},
            {"Skill": "Marketing Strategy", "Proficiency": 7},
        ],
    },
}

# Dropdown for course selection
selected_course = st.selectbox("Select a Course:", list(course_data.keys()))

# Get data for the selected course
course_skills = course_data[selected_course]

# Display matched skills
st.subheader("Top Skills Matched")
for skill in course_skills["matched_skills"]:
    st.write(f"**{skill['Skill']}**: {skill['Proficiency']}")

# Display skill gaps
st.subheader("Top Skills Lacking")
for skill in course_skills["gap_skills"]:
    st.write(f"**{skill['Skill']}**: {skill['Gap']}")

# Display company skills
st.subheader("Company Skills")
for skill in course_skills["company_skills"]:
    st.write(f"**{skill['Skill']}**: Proficiency {skill['Proficiency']}")

# Generate Report Button
if st.button("Generate Report"):
    st.success(f"PDF Report for {selected_course} Generated!")
