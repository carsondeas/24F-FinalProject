import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Skill Gaps",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Skill Gap & Preparedness Tracker")

# Dropdown for course selection
selected_course = st.selectbox("Select a Course:", ["CS 3200", "ACCT 2301", "MKTG 3301"])

# Skill Gap Data
matched_skills = [{"Skill": "Excel", "Proficiency": 8}, {"Skill": "Forecasting", "Proficiency": 7}]
gap_skills = [{"Skill": "Team Work", "Gap": 4}, {"Skill": "Discipline", "Gap": 2}]

st.subheader("Top Skills Matched")
for skill in matched_skills:
    st.write(f"**{skill['Skill']}**: {skill['Proficiency']}")

st.subheader("Biggest Gaps")
for skill in gap_skills:
    st.write(f"**{skill['Skill']}**: {skill['Gap']}")

# Company Skills
st.subheader("Company Skills")
sector = st.selectbox("Select Sector:", ["Finance", "Technology", "Marketing"])
if sector == "Finance":
    company_skills = [
        {"Skill": "Excel", "Proficiency": 8},
        {"Skill": "Financial Literacy", "Proficiency": 8},
        {"Skill": "Team Work", "Proficiency": 6},
    ]
elif sector == "Technology":
    company_skills = [
        {"Skill": "Python", "Proficiency": 9},
        {"Skill": "Data Structures", "Proficiency": 8},
        {"Skill": "Problem Solving", "Proficiency": 7},
    ]
else:
    company_skills = [
        {"Skill": "SEO", "Proficiency": 8},
        {"Skill": "Content Creation", "Proficiency": 8},
        {"Skill": "Data Analysis", "Proficiency": 7},
    ]

for skill in company_skills:
    st.write(f"**{skill['Skill']}**: Proficiency {skill['Proficiency']}")

# Generate Report Button
if st.button("Generate Report"):
    st.success("PDF Report Generated!")
