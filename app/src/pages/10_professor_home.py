import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Sidebar Navigation Links
SideBarLinks()

# Welcome Message
st.title(f"Welcome Professor, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write("### What would you like to do today?")

# Navigation Buttons
if st.button('Course Skill Alignment',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/11_course_skill_alignment.py')

if st.button('Skill Gap Analytics',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/12_skill_gap_analytics.py')

if st.button('Skill Trends Analytics',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/14_skill_trends_analytics.py')
