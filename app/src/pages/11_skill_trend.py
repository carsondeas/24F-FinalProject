import streamlit as st
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

API_BASE = "http://web-api:4000"

# Page Configuration
st.set_page_config(page_title="Skill Trends", page_icon="📈", layout="wide")

# Add navigation buttons
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("← Back"):
        st.write("Navigating back...")
        st.switch_page('pages/10_professor_home.py')
with col3:
    if st.button("🏠 Home"):
        st.write("Navigating to Home...") 
        st.switch_page('Home.py')

st.title("Skill Trends")
st.markdown("Explore trends in skill demand across industries and co-op roles.")

# Fetch Co-op Data
@st.cache_data
def fetch_coop_data():
    try:
        response = requests.get(f"{API_BASE}/coops/getall")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching co-op data: {e}")
        return []

# Prepare and Analyze Data
def process_data(data):
    """
    Processes the co-op data into a format suitable for analysis.
    """
    if not data:
        return pd.DataFrame()
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Expand skills column into individual rows
    df['skills'] = df['skillName'].str.split(', ')
    df = df.explode('skills')
    
    return df

# Fetch Data
raw_coop_data = fetch_coop_data()
coop_df = process_data(raw_coop_data)

if coop_df.empty:
    st.error("No co-op data available to display.")
else:
    # Display Summary Statistics
    st.subheader("Industry-wise Skill Demand")
    industry_skill_df = coop_df.groupby(['industry', 'skills']).size().reset_index(name='Demand Count')
    industry_skill_df = industry_skill_df.sort_values(by='Demand Count', ascending=False)
    
    st.write("Top skills across industries:")
    st.dataframe(industry_skill_df.head(10))

    # Chart: Top Industries by Skill Count
    st.subheader("Top Industries by Skill Demand")
    industry_counts = coop_df['industry'].value_counts().reset_index()
    industry_counts.columns = ['Industry', 'Count']
    st.bar_chart(industry_counts.set_index('Industry'))

    # Chart: Heatmap of Skill Demand by Industry and Role
    if not industry_skill_df.empty:
        try:
            # Pivot the data for the heatmap
            heatmap_df = industry_skill_df.pivot(index="skills", columns="industry", values="Demand Count").fillna(0)

            # Create a heatmap using Seaborn
            st.subheader("Heatmap: Skill Demand by Industry and Role")
            plt.figure(figsize=(12, 8))
            sns.heatmap(heatmap_df, annot=False, fmt="g", cmap="YlGnBu", cbar=True, linewidths=0.5)
            plt.title("Skill Demand Heatmap by Industry")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()

            # Display the plot in Streamlit
            st.pyplot(plt)
        except Exception as e:
            st.error(f"Error generating heatmap visualization: {e}")
    else:
        st.warning("No data available to generate heatmap.")
