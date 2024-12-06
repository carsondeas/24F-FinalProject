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

# Function to fetch all companies
def fetch_all_companies():
    try:
        response = requests.get(f"{API_BASE}/coops/name")  # Update to match your endpoint
        response.raise_for_status()
        data = response.json()
        return list({item["companyName"] for item in data})  # Extract unique company names
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching company names: {e}")
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
