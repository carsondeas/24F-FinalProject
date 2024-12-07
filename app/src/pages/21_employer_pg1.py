import streamlit as st
import pandas as pd
import requests

# Set the API base URL
API_BASE = "http://web-api:4000"

# Page configuration
st.set_page_config(
    page_title="Add New Co-op",
    page_icon="🏢",
    layout="wide",
)

# Back Button
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("← Back"):
        st.write("Navigating back...")
        st.switch_page('pages/20_employer_home.py')
with col3:
    if st.button("🏠 Home"):
        st.write("Navigating to Home...") 
        st.switch_page('Home.py')

st.title("Manage Postion Skills")


# Fetch all available skills
def fetch_all_skills():
    try:
        response = requests.get(f"{API_BASE}/skills/all")
        response.raise_for_status()
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching all skills: {e}")
        return []
# Function to fetch all companies
def fetch_all_companies():
    try:
        response = requests.get(f"{API_BASE}/coops/getall")  
        response.raise_for_status()
        data = response.json()
        return list({item["companyName"] for item in data}) 
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching company names: {e}")
        return []

def fetch_jobs_by_company(company_name):
    try:
        # Fetch all jobs from the API
        response = requests.get(f"{API_BASE}/coops/getall")
        response.raise_for_status()
        
        # Get the full list of jobs
        jobs = response.json()
        
        # Filter jobs by the given company name
        filtered_jobs = [job for job in jobs if job.get("companyName") == company_name]
        
        return filtered_jobs
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching jobs for company '{company_name}': {e}")
        return []


# Fetch skills already associated with the job
def fetch_job_skills(jobID):
    try:
        response = requests.get(f"{API_BASE}/coops/job_skills/{jobID}")  
        response.raise_for_status()
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        return []
    
def fetch_skills_for_job(job_title):
    try:
        response = requests.get(f"{API_BASE}/coops/job_skills/{job_title}")
        response.raise_for_status()
        job_skills = response.json()
        return pd.DataFrame(job_skills, columns=["Skill Name", "Proficiency Level"])
    except Exception as e:
        return pd.DataFrame()

def fetch_skill_id(skill_name):
    try:
        response = requests.get(f"{API_BASE}/skills/{skill_name}") 
        response.raise_for_status()
        skill_data = response.json()
        return skill_data.get('skillId')
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching skill id: {e}")
        return []

# Fetch all companies
companies = fetch_all_companies()


# Input fields for co-op details
st.subheader("Co-op Details")
# Expandable section for job and skill management
st.title("Manage Jobs and Skills")

# Searchable selectbox for Company Name
company_name = st.selectbox(
    "Company Name",
    options=[""] + companies,
    format_func=lambda x: x if x else "Type to search...",
)

st.subheader(f"Manage Jobs for '{company_name}'")

# Fetch jobs for the selected company
jobs = fetch_jobs_by_company(company_name)
job_names = [job["jobTitle"] for job in jobs]
# Create a mapping of job names to job IDs
job_mapping = {job["jobTitle"]: job["jobID"] for job in jobs}
# Fetch all skills
skills = fetch_all_skills()
skill_names = [skill['name'] for skill in skills]  

# Searchable dropdown for jobs
selected_job = st.selectbox(
    "Select Job",
    options=[""] + job_names,
    format_func=lambda x: x if x else "Type to search...",
    )
# Skill management after selecting a job
if selected_job:
    selected_job_id = job_mapping.get(selected_job)
    required_skills_df = fetch_skills_for_job(selected_job_id)
    st.subheader(f"Add Skills for Job: {selected_job}")
    associated_skills = fetch_job_skills(selected_job_id)
    associated_skill_names = [skill['Job Title'] for skill in associated_skills]
    available_skills = [skill for skill in skill_names if skill not in associated_skill_names]

    # Fetch skills
    skills = fetch_all_skills()

    # Multiselect for skills
    selected_skills = st.multiselect(
        "Select Skills to Add",
        options=[""] + skill_names,
        format_func=lambda x: x if x else "Type to search...",
    )

    # Add sliders for each selected skill
    skill_proficiency = {}
    if selected_skills:
        st.write("Set Proficiency Levels for Selected Skills:")
        for skill in selected_skills:
            proficiency = st.slider(
                f"Proficiency for {skill}",
                min_value=0,
                max_value=5,
                value=5,
                step=1,
                key=f"slider_{skill}"
            )
            skill_proficiency[skill] = proficiency

    # Button to add selected skills with proficiency to the job
    if st.button("Add/Update Skills"):
        try:
            # Determine if the skill needs a POST or PUT
            for skill, proficiency in skill_proficiency.items():
                if  required_skills_df.empty:
                    st.write(selected_job_id)
                    payload_add = {
                        "skillID": fetch_skill_id(skill),
                        "jobID": selected_job_id,
                        "proficiencyLevel": proficiency
                    }
                    response_add = requests.post(f"{API_BASE}/coops/add_skill", json=payload_add)
                    response_add.raise_for_status()
                    st.success(f"New skills added to job '{selected_job}' successfully!")
                elif skill in required_skills_df["Skill Name"].values:
                    payload_update = {
                        "jobID": selected_job_id,
                        "skillID": fetch_skill_id(skill),
                        "proficiencyLevel": proficiency
                    }
                    st.write(fetch_skill_id(skill))
                    response_put = requests.put(f"{API_BASE}/coops/update_skill", json=payload_update)
                    response_put.raise_for_status()
                    st.success(f"New skills added to job '{selected_job}' successfully!")
                else:
                    st.write(selected_job_id)
                    payload_add = {
                        "skillID": fetch_skill_id(skill),
                        "jobID": selected_job_id,
                        "proficiencyLevel": proficiency
                    }
                    response_add = requests.post(f"{API_BASE}/coops/add_skill", json=payload_add)
                    response_add.raise_for_status()
                    st.success(f"New skills added to job '{selected_job}' successfully!")
        except requests.exceptions.RequestException as e:
            st.error(f"Error adding skills: {e}")
    
    

    # Display required skills and user skills in a side-by-side comparison
    st.subheader(f"Skills for {selected_job}")
    col1= st.columns(1)
    # Display company-required skills
    
    st.markdown(f"**{company_name}'s Required Skills**")
    st.table(required_skills_df)
        