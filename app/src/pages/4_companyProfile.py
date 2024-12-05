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
        st.switch_page('pages/4_cpAdvisorHome.py')
with col3:
    if st.button("🏠 Home"):
        st.write("Navigating to Home...") 
        st.switch_page('Home.py')

# Prepare a list of unique company names for the dropdown
unique_companies = list({company['companyName'] for company in companies})
unique_companies.sort()  # Sort alphabetically

# Page layout
st.title("Company Search")

# Step 1: Select a Company
selected_company_name = st.selectbox(
    "Select a Company",
    options=["Select a Company"] + unique_companies,  # Placeholder text at the top
    help="Search and select a company to view available roles."
)

# Step 2: Filter roles by selected company
if selected_company_name and selected_company_name != "Select a Company":
    # Filter roles for the selected company
    filtered_roles = [
        {
            "jobTitle": company['jobTitle'],
            "jobID": company['jobID'],
            "skillName": company.get('skillName', '')
        }
        for company in companies if company['companyName'] == selected_company_name
    ]

    # Prepare a list of job titles
    role_titles = [role['jobTitle'] for role in filtered_roles]

    # Step 3: Select a Role
    selected_role_title = st.selectbox(
        "Select a Role",
        options=["Select a Role"] + role_titles,
        help="Select a role to view job details."
    )

    # Step 4: Display job details and chart for the selected role
    if selected_role_title and selected_role_title != "Select a Role":
        # Find the selected role details
        selected_role = next((role for role in filtered_roles if role['jobTitle'] == selected_role_title), None)

        if selected_role:
            st.subheader(f"Details for {selected_role_title}")
            st.write(f"**Company:** {selected_company_name}")
            st.write(f"**Role Title:** {selected_role['jobTitle']}")
            st.write(f"**Skills Required:** {selected_role.get('skillName', 'None')}")
            st.markdown("---")

            # Step 5: Display skills as a bar chart
            # Extract skills and proficiency levels (mocked for demonstration)
            skills = selected_role.get('skillName', '').split(', ')
            proficiency_levels = [3 for _ in skills]  # Mocked proficiency levels (adjust if your API provides levels)

            # Create a DataFrame for the chart
            skill_data = pd.DataFrame({
                "Skill": skills,
                "Proficiency Level": proficiency_levels
            })

            # Display the bar chart
            st.subheader("Skills Proficiency Chart")
            chart = alt.Chart(skill_data).mark_bar().encode(
                x=alt.X("Proficiency Level:Q", title="Proficiency Level"),
                y=alt.Y("Skill:O", title="Skill", sort="-x"),
                color=alt.Color("Proficiency Level:Q", scale=alt.Scale(scheme="blues")),
                tooltip=["Skill", "Proficiency Level"]
            ).properties(
                width=600,
                height=400,
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.warning("No matching role found.")
else:
    st.info("Select a company to view roles.")
# Example button for switching pages
st.markdown('<div class="skill-management-button">', unsafe_allow_html=True)
if st.button("🔧 Go to Industry Skill Trends"):
    st.switch_page('pages/4_skillTrends.py')  # Replace with navigation logic
st.markdown('</div>', unsafe_allow_html=True)
