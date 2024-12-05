import streamlit as st
import requests
import pandas as pd
import altair as alt

API_BASE = "http://web-api:4000"

st.set_page_config(
    page_title="Progress Tracking",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Progress Tracking")

# Fetch Progress Data
def fetch_progress_data(nuid_id):
    try:
        response = requests.get(f"{API_BASE}/students/{nuid_id}/details")
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
    # Convert progress data to a DataFrame
    df = pd.DataFrame(progress_data)

    # Check if the DataFrame has the necessary columns
    if "skill_name" in df.columns and "proficiencyLevel" in df.columns:
        # Create an Altair bar chart for visualization
        st.subheader("Skills Proficiency Chart")
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("proficiencyLevel:Q", title="Proficiency Level"),
            y=alt.Y("skill_name:O", title="Skill", sort="-x"),
            color=alt.Color("proficiencyLevel:Q", scale=alt.Scale(scheme="blues")),
            tooltip=["skill_name", "proficiencyLevel"]
        ).properties(
            width=700,
            height=400
        )

        st.altair_chart(chart, use_container_width=True)

        # Display raw progress data as a table
        st.subheader("Detailed Progress Data")
        st.table(df[["skill_name", "proficiencyLevel"]])
    else:
        st.error("Unexpected data format: Missing required columns ('skill_name', 'proficiencyLevel').")
else:
    st.write("No progress data found.")