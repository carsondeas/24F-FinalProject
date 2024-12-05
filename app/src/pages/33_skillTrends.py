import streamlit as st
import requests
import pandas as pd
import altair as alt

# Set the API base URL (replace with your actual API endpoint)
API_BASE = "http://web-api:4000"

# Set the page configuration
st.set_page_config(
    page_title="Company Profiles",
    page_icon="🏢",
    layout="wide",
)

# Function to fetch all companies and roles
def fetch_all_companies():
    try:
        response = requests.get(f"{API_BASE}/coops/getall")
        response.raise_for_status()
        return response.json()  # Returns a list of companies
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching company data: {e}")
        return []

# Fetch all companies
companies = fetch_all_companies()

# Add navigation buttons
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("← Back"):
        st.write("Navigating back...")
        st.switch_page('pages/30_cpAdvisorHome.py')
with col3:
    if st.button("🏠 Home"):
        st.write("Navigating to Home...") 
        st.switch_page('Home.py')

# Prepare a list of unique company names for the dropdown
unique_companies = list({industry['industry'] for industry in companies})
unique_companies.sort()

# Page layout
st.title("Industry Skill Trends")

# Skill Trends by Industry
st.subheader("Skill Trends by Industry")

# Step 1: Extract unique industries from the companies data
if companies:
    unique_industries = list({company['industry'] for company in companies})
    unique_industries.sort()  # Sort industries alphabetically

    # Step 2: Add a dropdown to select an industry
    selected_industry = st.selectbox(
        "Select an Industry",
        options=["Select an Industry"] + unique_industries,
        help="Choose an industry to view skill trends."
    )

    # Step 3: Filter companies based on the selected industry
    if selected_industry and selected_industry != "Select an Industry":
        filtered_companies = [company for company in companies if company['industry'] == selected_industry]

        # Step 4: Prepare skill data for the selected industry
        skill_counts = {}
        for company in filtered_companies:
            skills = company.get('skillName', '')
            if skills:
                for skill in skills.split(', '):  # Assuming skills are comma-separated
                    skill_counts[skill] = skill_counts.get(skill, 0) + 1

        # Convert the skill data to a DataFrame for visualization
        skill_data = pd.DataFrame(list(skill_counts.items()), columns=["Skill", "Frequency"])

        if not skill_data.empty:
            # Step 5: Display the skill trends as a pie chart
            pie_chart = alt.Chart(skill_data).mark_arc().encode(
                theta=alt.Theta("Frequency", type="quantitative"),
                color=alt.Color("Skill", type="nominal"),
                tooltip=["Skill", "Frequency"]
            ).properties(
                title=f"Skill Trends for {selected_industry}"
            )
            st.altair_chart(pie_chart, use_container_width=True)

            # Step 6: Display emerging skills
            st.subheader("Emerging Skills")
            emerging_skills = skill_data.sort_values(by="Frequency", ascending=False).head(3)
            st.markdown("\n".join([
                f"- **{row['Skill']}**: {row['Frequency']} occurrences"
                for _, row in emerging_skills.iterrows()
            ]))
        else:
            st.warning(f"No skills data available for the {selected_industry} industry.")
    else:
        st.info("Select an industry to view skill trends.")
else:
    st.warning("No companies data available.")

