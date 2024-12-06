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

st.title("Match With Canidates")


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
def fetch_job_skills(jobID):
    try:
        response = requests.get(f"{API_BASE}/coops/job_skills/{jobID}")  # Adjust the endpoint as needed
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
        response = requests.get(f"{API_BASE}/skills/{skill_name}")  # Adjust the endpoint as needed
        response.raise_for_status()
        skill_data = response.json()
        return skill_data.get('skillId')
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching skill id: {e}")
        return []

# Fetch job roles from the API
def fetch_all_students():
    try:
        response = requests.get(f"{API_BASE}/students/geteverything")  
        response.raise_for_status()
        
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching all students : {e}")
        return []

# Function to create a mailto link
def create_mailto_link(name, email):
    subject = f"Hello {name}"
    body = f"Dear {name},%0A%0AI would like to connect with you regarding an opportunity."
    return f'<a href="mailto:{email}?subject={subject}&body={body}">{email}</a>'

# Fetch all companies
companies = fetch_all_companies()

# Expandable section for job and skill management
st.subheader("Filter By Company")

# Searchable selectbox for Company Name
company_name = st.selectbox(
    "Company Name",
    options=[""] + companies,
    format_func=lambda x: x if x else "Type to search...",
)

st.subheader(f"Choose by Jobs '{company_name}'")

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
# Gets job skills of the selected job and converts to df
job_skills = fetch_job_skills(selected_job)
job_skills_df = pd.DataFrame(job_skills)

# Gets all studetns and their skills and converts to df
all_students = fetch_all_students()
all_students_df = pd.DataFrame(all_students)

# Check if the job_skills_df is empty
if job_skills_df.empty:
    st.write("No skills in this role.")
else:
    # Perform an inner join on 'Skill Name' and 'Proficiency Level'
    matching_students = pd.merge(
        all_students_df,
        job_skills_df,
        left_on=["Skill Name", "Proficiency Level"],
        right_on=["Skill Name", "Proficiency Level"],
        how="inner"
    )

    # Select only the desired columns
    result_df = matching_students[["Name", "NUID", "Email"]]

    # Drop duplicates in case students appear multiple times
    result_df = result_df.drop_duplicates()

    # Add mailto links to the result DataFrame
    result_df["Email"] = result_df.apply(lambda row: create_mailto_link(row["Name"], row["Email"]), axis=1)

    # Search Candidates button
    if st.button("Search Candidates"):
        if result_df.empty:
            st.write("No matching candidates found.")
        else:
            # Format the table for display in Streamlit
            st.markdown(
                """
                <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
                    <h3>Matching Candidates</h3>
                    {table}
                </div>
                """.format(table=result_df.to_html(escape=False, index=False)),
                unsafe_allow_html=True
            )
