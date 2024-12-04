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

# Company Selection
company_name = st.selectbox("Select Company", ["Microsoft", "Google", "Apple", "Amazon", "IBM"])
co_op_role = st.selectbox(
    "Select Co-Op Role",
    ["Software Developer Intern", "Data Analyyst Intern", "Machine Learning Intern"]
)

# Fetch company-specific skills from API
def fetch_coop_skills(company, co_op):
    try:
        response = requests.get(f"{API_BASE}/companies/{company}/coops/{co_op}/skills")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching skills for {company} and {co_op}: {e}")
        return []
    
# Fetch student-specific skills from API
def fetch_student_skills(student_id):
    try:
        response = requests.get(f"{API_BASE}/students/{student_id}/skills")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching student skills: {e}")
        return []
    
# User ID placeholder
student_id = 1 # Example logged-in student

# Get skills data
coop_skills = fetch_coop_skills(company_name, co_op_role)
student_skills = fetch_student_skills(student_id)

# Skill Comparison Table
st.subheader("Skill Comparison")
if coop_skills and student_skills:
    comparison_data = []
    for student_skill in student_skills:
        # Find matching skill in company co-op skills
        matching_skill = next(
            (skill for skill in coop_skills if skill["name"] == student_skill["name"]), None
        )
        comparison_data.append(
            {
                "Student Skill": student_skill["name"]
                "Student Proficiency": student_skill["proficiency"],
                "Required Skill": matching_skill["name"] if mathcing_skill else "N/A",
                "Required Proficiency": matching_skill["proficiency"] if matching_skill else "N/A",
            }
        )
    st.table(comparison_data)
else:
    st.warning("No skills available for comparison.")

# User Comments Section
st.subheader("User Comments")
st.text_area("Leave a comment")
