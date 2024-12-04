import streamlit as st
import requests

API_BASE = "http://web-api:4000"

st.set_page_config(
    page_title="Progress Tracking",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Progress Tracking")

# Fetch Progress Data
def fetch_progress_data(user_id):
    try:
        response = requests.get(f"{API_BASE}/students/{user_id}/details")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching progress data: {e}")
        return []

# User ID
user_id = 1

# Fetch Data
progress_data = fetch_progress_data(user_id)

# Display Progress
st.subheader("Your Skill Progress")
if progress_data:
    for skill in progress_data:
        st.write(f"{skill['skill']}: {skill['proficiency']} proficiency")
else:
    st.write("No progress data found.")
