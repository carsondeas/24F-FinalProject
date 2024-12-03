import streamlit as st
import requests

# Set the page configuration to wide
st.set_page_config(
    page_title="Skill Tracking and Trends",  # Title of the browser tab
    page_icon="📊",  # Icon for the browser tab
    layout="wide",  # Set the layout to wide
    initial_sidebar_state="expanded"  # Sidebar initially expanded
)
st.title("Skill Tracking / Trends")

# Job Filter Dropdown
job_filter = st.selectbox("Job Filter", ["Software Developer", "Data Scientist", "Other"])

# Dynamic Data Based on Job Filter
if job_filter == "Software Developer":
    company_matches = [{"name": "Google", "score": 94}, {"name": "Apple", "score": 88}, {"name": "Microsoft", "score": 81}]
    user_skills = [{"name": "Python", "score": 9}, {"name": "JavaScript", "score": 8}, {"name": "React", "score": 7},
                   {"name": "SQL", "score": 6}, {"name": "HTML/CSS", "score": 8}]
    trending_skills = [{"name": "React", "popularity": 75}, {"name": "JavaScript", "popularity": 60}]
elif job_filter == "Data Scientist":
    company_matches = [{"name": "Jane Street", "score": 92}, {"name": "Meta", "score": 89}, {"name": "Amazon", "score": 85}]
    user_skills = [{"name": "Python", "score": 8}, {"name": "R", "score": 7}, {"name": "Machine Learning", "score": 6},
                   {"name": "SQL", "score": 7}, {"name": "Data Visualization", "score": 8}]
    trending_skills = [{"name": "Python", "popularity": 80}, {"name": "Machine Learning", "popularity": 65}]
else:  # "Other"
    company_matches = [{"name": "Tesla", "score": 91}, {"name": "Netflix", "score": 87}, {"name": "Adobe", "score": 83}]
    user_skills = [{"name": "Problem Solving", "score": 8}, {"name": "Communication", "score": 9},
                   {"name": "Leadership", "score": 7}, {"name": "Critical Thinking", "score": 6}]
    trending_skills = [{"name": "Leadership", "popularity": 70}, {"name": "Communication", "popularity": 60}]

# Fetch and Display Company Matches
st.subheader("Company Matches")
for company in company_matches:
    st.write(f"**{company['name']}** - Match Score: {company['score']}")

# User Skills
st.subheader("Your Skills")
for skill in user_skills:
    st.write(f"**{skill['name']}** - Proficiency: {skill['score']}")

# Add Skill
st.text_input("Add Skill")

# Trending Skills
st.subheader("Trending Skills")
for trend in trending_skills:
    st.write(f"**{trend['name']}** - Popularity: {trend['popularity']}%")
