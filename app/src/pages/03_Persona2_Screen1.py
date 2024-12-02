import streamlit as st
import pandas as pd
import plotly.express as px

# Set the page configuration to wide
st.set_page_config(
    page_title="Skill Trends",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Skill Trends and Industry Skills")

# Dropdown for industry selection
industry = st.selectbox(
    "Industry Skill Trends for:",
    ["Data Science", "Investment Banking", "Marketing Analytics"]
)

# Sample skill data for each industry
industry_skills = {
    "Data Science": {"Python": 9, "R": 8, "Machine Learning": 8, "SQL": 7, "Statistics": 7},
    "Investment Banking": {"Financial Literacy": 10, "Excel": 10, "PowerPoint": 9, "Networking": 8, "Data Analysis": 7},
    "Marketing Analytics": {"SEO": 9, "Google Analytics": 8, "Content Creation": 8, "Data Visualization": 7, "SQL": 6},
}

# Display skills for the selected industry
skills = industry_skills[industry]
st.subheader(f"{industry} Industry Skills")
for skill, score in skills.items():
    st.write(f"**{skill}**: {score}")

# Radar chart for skill categories
st.subheader("Skill Proficiency Radar Chart")
categories = list(skills.keys())
values = list(skills.values())

fig = px.line_polar(
    r=values + [values[0]],
    theta=categories + [categories[0]],
    line_close=True,
    title="Skill Proficiency",
    range_r=[0, 10],
)
st.plotly_chart(fig)

# Dropdown and form for courses
st.subheader("Update Courses")
course = st.selectbox("Select a Course", ["ACCT 2301", "CS 3200", "MKTG 3301"])
st.text_input("Skill to Add", key="new_skill")
if st.button("Save"):
    st.success("Course updated successfully!")
