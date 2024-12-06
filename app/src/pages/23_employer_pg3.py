import streamlit as st
import requests

# Set the API base URL
API_BASE = "http://web-api:4000"

# Page configuration
st.set_page_config(
    page_title="Add New Co-op",
    page_icon="🏢",
    layout="wide",
)

st.title("Add a New Co-op Opportunity")


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
        response = requests.get(f"{API_BASE}/coops/getall")  # Update to match your endpoint
        response.raise_for_status()
        data = response.json()
        return list({item["companyName"] for item in data})  # Extract unique company names
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
def fetch_job_skills(job_title):
    try:
        response = requests.get(f"{API_BASE}/coops/job_skills/{job_title}")  # Adjust the endpoint as needed
        response.raise_for_status()
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching skills for job {job_title}: {e}")
        return []

# Fetch all companies
companies = fetch_all_companies()


# Input fields for co-op details
st.subheader("Co-op Details")

# Searchable selectbox for Company Name
company_name = st.selectbox(
    "Company Name",
    options=[""] + companies,
    format_func=lambda x: x if x else "Type to search...",
)
job_title = st.text_input("Job Title", placeholder="Enter job title")
industry = st.text_input("Industry", placeholder="Enter industry")



# Add Co-op button
if st.button("Add Co-op"):
    if not job_title or not company_name or not industry:
        st.error("Please fill in all co-op details.")
    else:
        payload = {
            "jobTitle": job_title,
            "companyName": company_name,
            "industry": industry,
        }
        try:
            response = requests.post(f"{API_BASE}/coops/addrole", json=payload)
            response.raise_for_status()
            st.success(f"Co-op '{job_title}' at '{company_name}' added successfully!")
        except requests.exceptions.RequestException as e:
            st.error(f"Error adding new co-op: {e}")

# Expandable section for job and skill management
st.title("Manage Jobs and Skills")
st.subheader(f"Manage Jobs for '{company_name}'")

# Fetch jobs for the selected company
jobs = fetch_jobs_by_company(company_name)
job_names = [job["jobTitle"] for job in jobs]
# Create a mapping of job names to job IDs
job_mapping = {job["jobTitle"]: job["jobID"] for job in jobs}  # Assuming jobs have 'jobTitle' and 'id'
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
    st.subheader(f"Add Skills for Job: {selected_job_id}")
    associated_skills = fetch_job_skills(selected_job_id)
    associated_skill_names = [skill['Job Title'] for skill in associated_skills]
    available_skills = [skill for skill in skill_names if skill not in associated_skill_names]

    # Fetch skills
    skills = fetch_all_skills()

    # Multiselect for skills
    selected_skills = st.multiselect(
        "Select Skills to Add",
        options=available_skills,
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
    if st.button("Add Skills"):
        if not skill_proficiency:
            st.error("Please select at least one skill and set proficiency levels.")
        else:
            try:
                # Prepare payload
                payload = {
                    "jobTitle": selected_job,
                    "skills": [{"name": skill, "proficiency": level} for skill, level in skill_proficiency.items()]
                }
                response = requests.post(f"{API_BASE}/coops/add_skill", json=payload)
                response.raise_for_status()
                st.success(f"Skills added to job '{selected_job}' successfully!")
            except requests.exceptions.RequestException as e:
                st.error(f"Error adding skills: {e}")