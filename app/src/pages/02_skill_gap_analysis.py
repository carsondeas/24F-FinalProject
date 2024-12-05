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
        coops = response.json()
        if not coops:
            st.warning("No co-op opportunities found.")
            return []
        return coops
    except Exception as e:
        st.error(f"Error fetching co-ops: {e}")
        return []

def fetch_skills_for_job(job_title):
    try:
        # Use the updated path parameter route
        response = requests.get(f"{API_BASE}/coops/job_skills/{job_title}")
        response.raise_for_status()
        job_skills = response.json()
        
        if not job_skills:
            st.warning(f"No skills found for Job ID {job_title}.")
            return pd.DataFrame()

        # Convert skills data to a DataFrame
        df = pd.DataFrame(job_skills)
        df.columns = ["Job Title", "Company Name", "Industry", "Skill Name", "Proficiency Level"]
        return df
    
    except Exception as e:
        st.error(f"Error fetching skills for job: {e}")
        return pd.DataFrame()



# Fetch all available skills
def fetch_all_user_skills(NUID):
    try:
        response = requests.get(f"{API_BASE}/students/{NUID}/details")
        response.raise_for_status()
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching students: {e}")
        return []



# User ID (example user)
user_id = 1

# Fetch data
user_skills = fetch_all_user_skills(user_id)
co_ops = fetch_co_ops()
required_skills_df = pd.DataFrame()


# Skill Gap Analysis Section
st.subheader("Skill Gap Analysis")

if co_ops:
    # Populate job IDs for selection
    job_ids = [co_op["jobTitle"] for co_op in co_ops]
    selected_job = st.selectbox("Select a Job Title (by Job ID)", job_ids)

    if selected_job:
        # Button to fetch and display job skills
        if st.button("Show Required Skills for Selected Job"):
            required_skills_df = fetch_skills_for_job(selected_job)

           # Check if the DataFrame is not empty
            if not required_skills_df.empty:
                # Display the results
                st.write("### Required Skills for the Selected Job")
                st.table(required_skills_df)
            else:
                st.write("No skills found for the selected job.")

        # Create DataFrame for user skills
        user_skills_df = pd.DataFrame(user_skills)
        # Initialize missing_skills at the start
        missing_skills = []
        
        # Check for empty DataFrame
        if user_skills_df.empty:
            st.warning("No user skills found.")
        elif required_skills_df.empty:
            st.warning("No required skills found.")
        else:
            # Analyze skill gaps
            user_skill_names = user_skills_df["skill_name"].tolist()  # Ensure column name matches
            required_skill_names = required_skills_df["Skill Name"].tolist()  # Ensure column name matches
            missing_skills = [skill for skill in required_skill_names if skill not in user_skill_names]

        # Display the user's skills
        st.write("### Your Skills")
        user_skills_df = user_skills_df.reset_index(drop=True)
        st.table(user_skills_df.style.hide(axis="index"))
        # Display the missing skills
        st.write("### Missing Skills")
        if missing_skills:
            # Convert missing skills to strings before joining
            st.write(", ".join(map(str, missing_skills)))
        else:
            st.write("You have all the required skills!")  

else:
    st.write("No job titles available for analysis.")
