import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Company Profiles",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Company Profiles")

# Company Search Section
st.subheader("Search Company Profiles")
company_name = st.text_input("Student ID:")
role_department = st.selectbox("Role/Department:", ["Software Engineering", "Data Science", "Marketing", "Finance"])
location = st.text_input("Location:")
if st.button("View Full Profile"):
    st.success("Displaying company profile... (Mock Data)")

# Initialize skill data in session state
if "skills" not in st.session_state:
    st.session_state.skills = {}

# Display and manage skills at the bottom
st.subheader("Add or Update Skills")
with st.form("add_update_skills_form"):
    new_skill_name = st.text_input("Skill Name:")
    new_skill_value = st.slider("Proficiency Level (0-100):", 0, 100, 50)
    submitted = st.form_submit_button("Add/Update Skill")
    if submitted:
        if new_skill_name:
            st.session_state.skills[new_skill_name] = new_skill_value
            st.success(f"Skill '{new_skill_name}' added/updated successfully!")
        else:
            st.error("Please enter a valid skill name.")

# Display Current Skills
st.subheader("Current Skills")
if st.session_state.skills:
    for skill, value in st.session_state.skills.items():
        st.write(f"**{skill}**: {value}")
else:
    st.write("No skills added yet. Add some skills to see them here!")

# Skill Trends Section
st.subheader("Skill Trends")
if st.session_state.skills:
    # Radar Chart for skill trends
    categories = list(st.session_state.skills.keys())
    values = list(st.session_state.skills.values())

    fig = px.line_polar(
        r=values + [values[0]],  # Close the chart loop
        theta=categories + [categories[0]],  # Close the chart loop
        line_close=True,
        title="Skill Trends",
        range_r=[0, 100],
    )
    st.plotly_chart(fig)
else:
    st.write("Add skills to visualize the Skill Trends chart.")

