import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Define a Back Button
if st.button("Back"):
    # Logic for the back button
    st.write("Navigating back...")
    # Redirect or reset the page state (Example: Use navigation logic here)
    st.switch_page('Home.py')  # Reload the page

st.title(f"Welcome Student, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Skill Tracking', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_skill_tracking.py')

if st.button('Skill Gap Analysis', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_skill_gap_analysis.py')

if st.button('Manage Skills', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_skill_management.py')

