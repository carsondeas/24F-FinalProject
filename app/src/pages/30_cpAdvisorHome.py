import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()

# Define a Back Button
if st.button("Back"):
    # Logic for the back button
    st.write("Navigating back...")
    # Redirect or reset the page state
    st.switch_page('Home.py')  # Redirect to Home page

# Welcome Message
st.title(f"Welcome Advisor Bobby")
st.write('')
st.write('')
st.write("### What would you like to do today?")

# Navigation Buttons
if st.button('Student Profiles',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/31_studentProfile.py')

if st.button('Company Profiles',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/32_companyProfile.py')

if st.button('View Skill Trends',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/33_skillTrends.py')