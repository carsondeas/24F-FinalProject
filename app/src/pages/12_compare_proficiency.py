import streamlit as st
import requests

API_BASE = "http://web-api:4000"

st.set_page_config(page_title="Skill Gap Analytics",
                   page_icon="📉",
                   layout="wide")

st.title("Skill Gap Analytics")

# Fetch Skill Gap Data
def fetch_skill_gaps():
    try:
        response = requests.get(f"{API_BASE}/skills/analytics")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching skill gap data: {e}")
        return []

# Display Skill Gaps
skill_gaps = fetch_skill_gaps()

st.subheader("Skill Gap Analysis")
if skill_gaps:
    for gap in skill_gaps.get("skill_gaps", []):
        st.write(f"- **Skill:** {gap['skill']}, **Industry:** {gap['industry']}, **Demand Count:** {gap['gap_count']}")
else:
    st.write("No skill gap data available.")
