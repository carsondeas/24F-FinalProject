import streamlit as st
import requests
import pandas as pd

# Set the API base URL
API_BASE = "http://web-api:4000"

# Page configuration
st.set_page_config(
    page_title="Skill Gap Analysis",
    page_icon="📊",
    layout="wide",
)

# Back Button
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("← Back"):
        st.write("Navigating back...")
        st.switch_page('pages/00_Student_Home.py')
with col3:
    if st.button("🏠 Home"):
        st.write("Navigating to Home...") 
        st.switch_page('Home.py')

st.title("Skill Gap Analysis")

# Fetch Co-ops (Job Titles and Skills)
def fetch_co_ops():
    try:
        response = requests.get(f"{API_BASE}/coops/name")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching co-ops: {e}")
        return []

def fetch_skills_for_job(job_title):
    try:
        response = requests.get(f"{API_BASE}/coops/job_skills/{job_title}")
        response.raise_for_status()
        job_skills = response.json()
        return pd.DataFrame(job_skills, columns=["Skill Name", "Proficiency Level"])
    except Exception as e:
        return pd.DataFrame()

def fetch_all_user_skills(nuid):
    try:
        response = requests.get(f"{API_BASE}/students/{nuid}/details")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching user skills: {e}")
        return []

# User ID (example user)
user_id = 1

# Fetch data
co_ops = fetch_co_ops()
user_skills = fetch_all_user_skills(user_id)

# Page layout
if co_ops:
    company_names = list({co_op["companyName"] for co_op in co_ops})
    selected_company = st.selectbox("Select a Company", options=[""] + company_names)
    
    if selected_company:
        roles = [co_op["jobTitle"] for co_op in co_ops if co_op["companyName"] == selected_company]
        selected_role = st.selectbox("Select a Role", options=[""] + roles)
        
        if selected_role:
            # Fetch skills for the selected role
            required_skills_df = fetch_skills_for_job(selected_role)

            # Display required skills and user skills in a side-by-side comparison
            st.subheader(f"Skill Comparison: {selected_company} - {selected_role}")
            col1, col2 = st.columns(2)
            
            # Display user's skills
            with col1:
                st.markdown("**My Skills**")
                user_skills_df = pd.DataFrame(user_skills, columns=["skill_name", "proficiencyLevel"])
                user_skills_df.rename(columns={"skill_name": "Skill Name", "proficiencyLevel": "Proficiency Level"}, inplace=True)
                st.table(user_skills_df)

            # Display company-required skills
            with col2:
                st.markdown(f"**{selected_company}'s Required Skills**")
                st.table(required_skills_df)

            # Skill gap analysis
            user_skill_names = user_skills_df["Skill Name"].tolist()
            if not required_skills_df.empty:
                required_skill_names = required_skills_df["Skill Name"].tolist()
            else:
                required_skill_names = []
            missing_skills = [skill for skill in required_skill_names if skill not in user_skill_names]
            
            # Display missing skills
            st.subheader("Missing Skills")
            if missing_skills:
                st.write(", ".join(missing_skills))
            else:
                st.success("You meet all the required skills!")
else:
    st.warning("No job titles available.")
