import streamlit as st
import requests

# Set the API base URL
API_BASE = "http://web-api:4000"

# Set page configuration to wide
st.set_page_config(
    page_title="Skill Comparison with Company",
    page_icon="📊",
    layout="wide",  # Set the layout to wide
    initial_sidebar_state="expanded"  # Sidebar initially expanded
)

st.title("Skill Comparison with Company")

# Fetch all companies from the API
def fetch_all_companies():
    try:
        response = requests.get(f"{API_BASE}/companies")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching companies: {e}")
        return []

# Fetch all co-op roles for a selected company
def fetch_company_coops(company_name):
    try:
        response = requests.get(f"{API_BASE}/companies/{company_name}/coops")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching co-ops for {company_name}: {e}")
        return []

# Fetch co-op-specific skills from the API
def fetch_coop_skills(company_name, co_op_title):
    try:
        response = requests.get(f"{API_BASE}/companies/{company_name}/coops/{co_op_title}/skills")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching skills for {company_name} and {co_op_title}: {e}")
        return []

# Fetch the logged-in student's skills
def fetch_student_skills(student_id):
    try:
        response = requests.get(f"{API_BASE}/students/{student_id}/skills")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching student skills: {e}")
        return []

# User ID placeholder (replace with session_state when integrated)
student_id = 1  # Example logged-in student

# Step 1: Select a company
companies = fetch_all_companies()
company_names = [company["name"] for company in companies]
selected_company = st.selectbox("Select Company", company_names)

# Step 2: Select a co-op role
if selected_company:
    coops = fetch_company_coops(selected_company)
    co_op_titles = [coop["title"] for coop in coops]
    selected_co_op = st.selectbox("Select Co-Op Role", co_op_titles)

# Step 3: Fetch and compare skills
if selected_company and selected_co_op:
    coop_skills = fetch_coop_skills(selected_company, selected_co_op)
    student_skills = fetch_student_skills(student_id)

    if coop_skills and student_skills:
        st.subheader("Skill Comparison")
        comparison_data = []
        for student_skill in student_skills:
            matching_skill = next(
                (skill for skill in coop_skills if skill["name"] == student_skill["name"]), None
            )
            comparison_data.append(
                {
                    "Student Skill": student_skill["name"],
                    "Student Proficiency": student_skill["proficiency"],
                    "Required Skill": matching_skill["name"] if matching_skill else "N/A",
                    "Required Proficiency": matching_skill["proficiency"] if matching_skill else "N/A",
                }
            )
        st.table(comparison_data)
    else:
        st.warning("No skills available for comparison.")

# Add a comments section for the user to leave feedback
st.subheader("User Comments")
st.text_area("Leave a comment")