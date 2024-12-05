import streamlit as st
import altair as alt
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Industry and Skill Trends",
    page_icon="📊",
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

st.title("Industry and Skill Trends")

# Section: View Industry Trends
st.subheader("Industry Trends")
industries = ["Technology", "Healthcare", "Finance", "Engineering"]
selected_industry = st.selectbox("Select an Industry", industries)

# Placeholder for skill data (Replace with API data)
skills_data = pd.DataFrame({
    "Skill": ["Python", "SQL", "React", "Leadership"],
    "Frequency": [50, 40, 30, 20],
})
st.write(f"Skills in {selected_industry} Industry")
bar_chart = alt.Chart(skills_data).mark_bar().encode(
    x=alt.X("Frequency", title="Number of Jobs Requiring Skill"),
    y=alt.Y("Skill", sort="-x", title="Skill"),
    color=alt.Color("Frequency", scale=alt.Scale(scheme="blues")),
    tooltip=["Skill", "Frequency"],
)
st.altair_chart(bar_chart, use_container_width=True)

# Section: View Emerging Skills
st.subheader("Emerging Skills")
emerging_skills = skills_data.sort_values(by="Frequency", ascending=False).head(3)
st.markdown("\n".join([f"- **{row['Skill']}**: {row['Frequency']} occurrences" for _, row in emerging_skills.iterrows()]))
