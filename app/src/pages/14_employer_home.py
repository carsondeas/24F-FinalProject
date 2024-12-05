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
st.title("Welcome, Employer!")
st.subheader("Explore trends, analyze skill gaps, and access top skill insights to better prepare your students.")

# Add spacing for better layout
st.write("")
st.write("")

# Navigation options with streamlined buttons
st.write("### What would you like to do today?")

if st.button("Manage Co-op Postions and Skills",
             type='primary',
             use_container_width=True):
    st.switch_page('pages/15_employer_pg1.py')

if st.button("Search and Match Students",
             type='primary',
             use_container_width=True):
    st.switch_page('pages/16_employer_pg2.py')

if st.button("View Industry and Skill Trends",
             type='primary',
             use_container_width=True):
    st.switch_page('pages/17_employer_pg3.py')
