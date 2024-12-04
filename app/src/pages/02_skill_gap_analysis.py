import streamlit as st
import requests

# Set the API base URL
API_BASE = "http://web-api:4000"

# Set page configuration to wide
st.set_page_config(
    page_title="Skill Gap Analysis",
    page_icon="📊",
    layout="wide",  # Set the layout to wide
    initial_sidebar_state="expanded"  # Sidebar initially expanded
)

st.title("Skill Gap Analysis")

# Fetch Co-ops
def fetch_co_ops():
    try:
        response = requests.get(f"{API_BASE}/co_ops")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching co-ops: {e}")
        return []

# Fetch User Skills
def fetch_user_skills(user_id):
    try:
        response = requests.get(f"{API_BASE}/students/{user_id}/details")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching user skills: {e}")
        return []

# User ID
user_id = 1

# Fetch Data
user_skills = fetch_user_skills(user_id)
co_ops = fetch_co_ops()

# Skill Gap Analysis
st.subheader("Skill Gap Analysis")
selected_co_op = st.selectbox("Select Co-op Role", [co_op["title"] for co_op in co_ops])

if selected_co_op:
    co_op = next(co_op for co_op in co_ops if co_op["title"] == selected_co_op)
    required_skills = co_op["skills"]

    st.write("### Required Skills for the Selected Co-op Role")
    st.write(", ".join(required_skills))

    missing_skills = [skill for skill in required_skills if skill not in [us["skill"] for us in user_skills]]

    st.write("### Missing Skills")
    if missing_skills:
        st.write(", ".join(missing_skills))
    else:
        st.write("You have all the required skills!")