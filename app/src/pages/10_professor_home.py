import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

# Define a Back Button
if st.button("Back"):
    # Logic for the back button
    st.write("Navigating back...")
    # Redirect or reset the page state
    st.switch_page('Home.py')  # Redirect to Home page

# Header
st.title("Welcome, Professor!")
st.subheader("Explore trends, analyze skill gaps, and access top skill insights to better prepare your students.")

# Add spacing for better layout
st.write("")
st.write("")

# Navigation options with streamlined buttons
st.write("### What would you like to do today?")

if st.button("Explore Skill Trends",
             type='primary',
             use_container_width=True):
    st.switch_page('11_skill_trend.py')

if st.button("Compare Proficiency Levels",
             type='primary',
             use_container_width=True):
    st.switch_page('12_compare_proficiency.py')

if st.button("View Top Skills for Co-ops",
             type='primary',
             use_container_width=True):
    st.switch_page('13_top_skills.py')
