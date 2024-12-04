import streamlit as st
import requests

API_BASE = "http://web-api:4000"

st.set_page_config(page_title="Co-op Role Matching", page_icon="💼", layout="wide")

st.title("Co-op Role Matching")

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

# Match Roles
st.subheader("Matching Co-op Roles")
matched_co_ops = [
    co_op for co_op in co_ops
    if any(skill in [us["skill"] for us in user_skills] for skill in co_op["skills"])
]

if matched_co_ops:
    st.write("### Recommended Co-op Roles")
    for co_op in matched_co_ops:
        st.write(f"- {co_op['title']} at {co_op['company']}")
else:
    st.write("No matching roles found.")
