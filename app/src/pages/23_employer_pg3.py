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
