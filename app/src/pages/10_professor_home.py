import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

# Define a Back Button
if st.button("Back"):
    # Logic for the back button
    st.write("Navigating back...")
    # Redirect to Home page
    st.switch_page('Home.py')  

# Header
st.title(f"Welcome Professor, {st.session_state['first_name']}!")
st.subheader("Explore trends, analyze skill gaps, and access top skill insights to better prepare your students.")

# Add spacing for better layout
st.write("")
st.write("")

# Navigation options with streamlined buttons
st.write("### What would you like to do today?")

if st.button("Explore Skill Trends",
             type='primary',
             use_container_width=True):
    st.switch_page('pages/11_skill_trend.py')

if st.button("Compare Proficiency Levels",
             type='primary',
             use_container_width=True):
    st.switch_page('pages/12_compare_proficiency.py')

if st.button("View Top Skills for Co-ops",
             type='primary',
             use_container_width=True):
    st.switch_page('pages/13_top_skills.py')
