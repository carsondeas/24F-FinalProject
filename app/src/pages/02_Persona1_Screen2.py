import streamlit as st

# Set page configuration to wide
st.set_page_config(
    page_title="Skill Comparison with Company",
    page_icon="📊",
    layout="wide",  # Set the layout to wide
    initial_sidebar_state="expanded"  # Sidebar initially expanded
)

st.title("Skill Comparison with Company")

# Company Selection
company_name = st.selectbox("Select Company", ["Google", "Jane Street", "Apple"])

# Define company-specific skills
company_skills_data = {
    "Google": [
        {"name": "Python", "score": 8},
        {"name": "React", "score": 7},
        {"name": "Team Work", "score": 9},
        {"name": "Discipline", "score": 8},
        {"name": "Eagerness to Learn", "score": 10},
        {"name": "Java", "score": 8},
        {"name": "Cloud Computing", "score": 7}
    ],
    "Jane Street": [
        {"name": "Python", "score": 9},
        {"name": "Java", "score": 8},
        {"name": "Leadership", "score": 10},
        {"name": "Discipline", "score": 7},
        {"name": "Data Analysis", "score": 8},
        {"name": "C++", "score": 9},
        {"name": "Statistics", "score": 10}
    ],
    "Apple": [
        {"name": "Swift", "score": 9},
        {"name": "Objective-C", "score": 8},
        {"name": "Leadership", "score": 7},
        {"name": "Discipline", "score": 6},
        {"name": "Eagerness to Learn", "score": 8},
        {"name": "UI/UX Design", "score": 10},
        {"name": "Problem Solving", "score": 9}
    ]
}

# Define user skills
user_skills = [
    {"name": "Python", "score": 8},
    {"name": "Java", "score": 7},
    {"name": "Leadership", "score": 3},
    {"name": "Discipline", "score": 5},
    {"name": "JavaScript", "score": 5},
    {"name": "React", "score": 2},
    {"name": "SQL", "score": 2}
]

# Fetch company-specific skills based on selection
company_skills = company_skills_data.get(company_name, [])

# Skill Comparison Table
st.subheader("Skill Comparison")
comparison_data = []
for user_skill, company_skill in zip(user_skills, company_skills):
    comparison_data.append(
        {
            "User Skill": user_skill["name"],
            "User Score": user_skill["score"],
            "Company Skill": company_skill["name"],
            "Company Score": company_skill["score"]
        }
    )

st.table(comparison_data)

# Add Skill (Optional)
st.text_input("Add Skill")

# User Comments Section
st.subheader("User Comments")
st.text_area("Leave a comment")
