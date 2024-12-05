import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Manage Co-op Positions",
    page_icon="📄",
    layout="wide",
)

# Back Button
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("← Back"):
        st.write("Navigating back...")
        st.switch_page('pages/20_employer_home.py')
with col3:
    if st.button("🏠 Home"):
        st.write("Navigating to Home...") 
        st.switch_page('Home.py')


st.title("Manage Co-op Positions")

# Section: Add a New Co-op Position
st.subheader("Add a New Co-op Position")
job_title = st.text_input("Job Title")
department = st.text_input("Department")
description = st.text_area("Job Description")
skills = st.multiselect("Required Skills", ["Python", "SQL", "React", "Leadership"])
if st.button("Add Co-op Position"):
    if job_title and department and description:
        st.success(f"Co-op Position '{job_title}' added successfully!")
    else:
        st.error("Please fill in all fields to add the position.")

# Section: Update Skills for a Position
st.subheader("Update Skills for a Position")
positions = st.selectbox("Select a Position to Update", ["Backend Engineer", "Frontend Engineer", "Data Analyst"])
updated_skills = st.multiselect("Update Required Skills", ["Python", "SQL", "React", "Leadership"], default=skills)
if st.button("Update Skills"):
    st.success(f"Skills for '{positions}' updated successfully!")

# Section: Remove Outdated Skills
st.subheader("Remove Outdated Skills")
skills_to_remove = st.multiselect("Select Skills to Remove", ["Python", "SQL", "React", "Leadership"])
if st.button("Remove Skills"):
    st.success("Outdated skills removed successfully!")
