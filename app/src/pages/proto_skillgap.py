import streamlit as st
import requests
import pandas as pd

# Set the API base URL
API_BASE = "http://localhost:4000"

# Page configuration
st.set_page_config(
    page_title="Skill Gap Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

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
        response = requests.get(f"{API_BASE}/coops/job_skills", params={"jobTitle": job_title})
        response.raise_for_status()
        job_skills = response.json()
        
        if not job_skills:
            st.warning(f"No skills found for Job {job_title}.")
            return pd.DataFrame()

        # Convert skills data to a DataFrame
        df = pd.DataFrame(job_skills)
        df.columns = ["Skill Name", "Required Level"]
        return df
    
    except Exception as e:
        st.error(f"Error fetching skills for job: {e}")
        return pd.DataFrame()

    
    except Exception as e:
        st.error(f"Error fetching skills for job: {e}")
        return []

# Fetch User Skills using the same method as your existing code
def fetch_user_skills(nuid):
    try:
        response = requests.get(f"{API_BASE}/students/{nuid}/details")
        response.raise_for_status()
        skills_data = response.json()
        
        if not skills_data:
            st.warning(f"No skills found for student with NUID {nuid}.")
            return

        # Convert skills data to a DataFrame
        df = pd.DataFrame(skills_data)

    except Exception as e:
        st.error(f"Error fetching user skills: {e}")
        return []


# User ID (example user)
user_id = 1

# Fetch data
user_skills = fetch_user_skills(user_id)
co_ops = fetch_co_ops()

# Skill Gap Analysis Section
st.subheader("Skill Gap Analysis")
if co_ops:
    job_titles = [f"{co_op['companyName']} - {co_op['jobTitle']}" for co_op in co_ops]
    selected_job = st.selectbox("Select a Job Title", job_titles)

    if selected_job:
        company, job_title = selected_job.split(" - ")
        required_skills = fetch_skills_for_job(job_title)

        # Create dataframes for analysis
        user_skills_df = pd.DataFrame(user_skills)
        required_skills_df = pd.DataFrame(required_skills)

        # Compare user and required skills
        if not user_skills_df.empty and not required_skills_df.empty:
            user_skill_names = user_skills_df["skill_name"].tolist()
            required_skill_names = required_skills_df["name"].tolist()

            missing_skills = [skill for skill in required_skill_names if skill not in user_skill_names]

            # Display the results
            st.write("### Required Skills for the Selected Job")
            st.table(required_skills_df)

            st.write("### Your Skills")
            st.table(user_skills_df)

            st.write("### Missing Skills")
            if missing_skills:
                st.write(", ".join(missing_skills))
            else:
                st.write("You have all the required skills!")
else:
    st.write("No job titles available for analysis.")