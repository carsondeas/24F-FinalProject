import streamlit as st

st.set_page_config(
    page_title="Co-Op Advisory Dashboard",
    page_icon="🧑‍🏫",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Co-Op Advisor skill/student/industry demand viewer")

# Define student profiles
student_profiles = {
    "Alice": {"skills": {"Python": 7, "SQL": 6, "Data Visualization": 5}},
    "Bob": {"skills": {"Excel": 9, "Financial Analysis": 8, "Leadership": 6}},
}

# Define industry demands
industry_demands = {
    "Software Engineer": {"Python": 8, "Machine Learning": 7, "Cloud Computing": 6},
    "Financial Analyst": {"Excel": 9, "Data Analysis": 8, "Leadership": 7},
}

# Dropdown for student selection
selected_student = st.selectbox("Select a Student:", list(student_profiles.keys()))


# Display student skills
st.subheader(f"{selected_student}'s Skills")
for skill, proficiency in student_profiles[selected_student]["skills"].items():
    st.write(f"**{skill}**: Proficiency {proficiency}")

# Display industry demands
st.subheader("Industry Demands")
for role, skills in industry_demands.items():
    st.write(f"**{role}**:")
    for skill, proficiency in skills.items():
        st.write(f"  - {skill}: Proficiency {proficiency}")

# Advisor insights
if st.button("Analyze Student Profile"):
    st.success(f"Analysis for {selected_student} completed! Suggest enhancing Cloud Computing and Data Analysis.")

# To remove outdated skills
st.subheader("Remove Outdated Skills")
outdated_skill = st.text_input("Enter Skill to Remove:")
if st.button("Remove Skill"):
    removed = False
    for company in company_skills_db.values():
        for role_skills in company.values():
            if outdated_skill in role_skills:
                del role_skills[outdated_skill]
                removed = True
    if removed:
        st.success(f"Removed outdated skill: {outdated_skill}")
    else:
        st.warning(f"Skill {outdated_skill} not found in the database.")