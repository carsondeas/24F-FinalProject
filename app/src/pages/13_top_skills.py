import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page configuration
st.set_page_config(page_title="Top Skills for Co-ops", page_icon="🏆", layout="wide")

# Base API URL
API_BASE = "http://web-api:4000"

# Page Title
st.title("Top Skills for Co-op Roles")

# Add navigation buttons
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("← Back"):
        st.write("Navigating back...")
        st.switch_page('pages/10_Professor_Home.py')
with col3:
    if st.button("🏠 Home"):
        st.write("Navigating to Home...") 
        st.switch_page('Home.py')

# Fetch Co-op Skills Data
@st.cache_data
def fetch_top_coop_skills():
    try:
        response = requests.get(f"{API_BASE}/coops/top_skills")
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except Exception as e:
        st.error(f"Error fetching co-op skills data: {e}")
        return pd.DataFrame()

# Data Processing
coop_skills_df = fetch_top_coop_skills()

# Validate Data
if coop_skills_df.empty:
    st.warning("No data available for top skills.")

else:
    # Top 10 Skills by Demand
    top_skills_df = coop_skills_df.groupby("skillName")["demandCount"].sum().reset_index()
    top_skills_df = top_skills_df.sort_values(by="demandCount", ascending=False).head(10)

    # Display top skills table
    st.markdown("### Top 10 Skills by Demand")
    st.dataframe(top_skills_df)

    # Visualization
    st.markdown("### Visualization of Top Skills")
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_skills_df, x="demandCount", y="skillName", palette="coolwarm")
    plt.title("Top 10 In-Demand Skills for Co-op Roles")
    plt.xlabel("Demand Count")
    plt.ylabel("Skill")
    plt.tight_layout()
    st.pyplot(plt)

    # Skills by Industry
    st.markdown("### Skills Demand by Industry")
    industry_skills_df = coop_skills_df.groupby(["industry", "skillName"])["demandCount"].sum().reset_index()
    pivot_df = industry_skills_df.pivot(index="skillName", columns="industry", values="demandCount").fillna(0)

    st.dataframe(pivot_df)

    # Visualization: Stacked Bar Chart
    st.markdown("### Stacked Bar Chart: Top Skills by Industry")
    pivot_long = pivot_df.reset_index().melt(id_vars="skillName", var_name="industry", value_name="demand")

    palette = sns.color_palette("Paired", n_colors=pivot_long["skillName"].nunique())

    plt.figure(figsize=(12, 8))
    sns.barplot(
        data=pivot_long,
        x="industry",
        y="demand",
        hue="skillName",
        dodge=False,
        palette=palette
    )
    plt.title("Top Skills Demand by Industry")
    plt.xlabel("Industry")
    plt.ylabel("Demand Count")
    plt.xticks(rotation=45)
    st.pyplot(plt)