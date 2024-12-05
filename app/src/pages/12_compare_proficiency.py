import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Compare Proficiency Levels", page_icon="📊", layout="wide")

# Base API URL
API_BASE = "http://web-api:4000"

# Page Title
st.title("Compare Average Proficiency Levels")

# Fetch Student Skills Data
@st.cache_data
def fetch_student_skills():
    try:
        response = requests.get(f"{API_BASE}/students/skills_avg_proficiency") 
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except Exception as e:
        st.error(f"Error fetching student skills data: {e}")
        return pd.DataFrame()

# Fetch Co-op Skills Data
@st.cache_data
def fetch_coop_skills():
    try:
        response = requests.get(f"{API_BASE}/coops/skills_avg_proficiency")
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except Exception as e:
        st.error(f"Error fetching co-op skills data: {e}")
        return pd.DataFrame()

# Data Processing
student_skills_df = fetch_student_skills()
coop_skills_df = fetch_coop_skills()

# Validate Data
if student_skills_df.empty or coop_skills_df.empty:
    st.warning("No data available for comparison.")
else:
    # Rename and process student skills
    student_skills_df = student_skills_df[["skillName", "avgProficiencyLevel"]].rename(
        columns={"skillName": "skill", "avgProficiencyLevel": "student_avg_proficiency"}
    )

    # Rename and process co-op skills
    coop_skills_df = coop_skills_df[["skillName", "avgProficiencyLevel"]].rename(
        columns={"skillName": "skill", "avgProficiencyLevel": "coop_avg_proficiency"}
    )

    # Merge both dataframes on skill
    comparison_df = pd.merge(
        student_skills_df, coop_skills_df, on="skill", how="outer", suffixes=("_student", "_coop")
    ).fillna(0)

    # Display comparison data
    st.markdown("### Proficiency Comparison Table")
    st.dataframe(comparison_df)

    # Visualization
    st.markdown("### Proficiency Comparison Chart")
    plt.figure(figsize=(14, 8))

    # Melt the dataframe
    melted_df = comparison_df.melt(
        id_vars="skill", var_name="Group", value_name="Proficiency"
    )

    # Make sure 'skill' column contains strings and handle NaN values in 'Proficiency'
    melted_df["skill"] = melted_df["skill"].astype(str)
    melted_df["Proficiency"] = pd.to_numeric(melted_df["Proficiency"], errors="coerce").fillna(0)
    
    sns.barplot(
        data=melted_df,
        x="skill",
        y="Proficiency",
        hue="Group",
    )
    plt.title("Student vs. Co-op Average Proficiency Levels")
    plt.xticks(rotation=45, ha="right")
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
    plt.tight_layout()
    st.pyplot(plt)