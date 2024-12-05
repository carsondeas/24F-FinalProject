import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')


# Welcome Message
st.title(f"Welcome Advisor Bobby")
st.write('')
st.write('')
st.write("### What would you like to do today?")

# Navigation Buttons
if st.button('Student Profiles',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/4_studentProfile.py')

if st.button('Company Profiles',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/4_companyProfile')
