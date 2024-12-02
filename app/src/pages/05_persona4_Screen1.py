import streamlit as st

st.set_page_config(
    page_title="Co-Op Advisory Dashboard",
    page_icon="🧑‍🏫",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Co-Op Advisor Toolkit")

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
