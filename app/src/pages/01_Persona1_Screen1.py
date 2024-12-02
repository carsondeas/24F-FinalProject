import streamlit as st
import requests

API_BASE = "http://localhost:4000/api"  # Replace with your Flask API base URL

st.title("Skill Tracking / Trends")

# Job Filter Dropdown
job_filter = st.selectbox("Job Filter", ["Software Developer", "Data Scientist", "Other"])

# Fetch and Display Company Matches
st.subheader("Company Matches")
company_matches = [{"name": "Google", "score": 94}, {"name": "Jane Street", "score": 83}, {"name": "Apple", "score": 75}]
for company in company_matches:
    st.write(f"**{company['name']}** - Match Score: {company['score']}")

# User Skills
st.subheader("Your Skills")
user_skills = [{"name": "Python", "score": 8}, {"name": "Java", "score": 7}, {"name": "Leadership", "score": 3},
               {"name": "Discipline", "score": 5}, {"name": "JavaScript", "score": 5}, {"name": "React", "score": 2},
               {"name": "SQL", "score": 2}]

for skill in user_skills:
    st.write(f"**{skill['name']}** - Proficiency: {skill['score']}")

# Add Skill
st.text_input("Add Skill")

# Trending Skills
st.subheader("Trending Skills")
trending_skills = [{"name": "React", "popularity": 70}, {"name": "Python", "popularity": 30}]
for trend in trending_skills:
    st.write(f"**{trend['name']}** - Popularity: {trend['popularity']}%")
