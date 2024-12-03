import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import HomeNav

HomeNav()

st.write("# About SkillSeeker")

st.markdown (
    """
    ### **What is SkillSeeker?**
    In today’s fast-evolving job market, **SkillSeeker** is a powerful, data-driven platform designed to bridge the information gap for in-demand skills. 
    It helps students better prepare for their careers by informing them about the specific skills employers seek.

    **SkillSeeker** simplifies the co-op and job application process by providing access to a comprehensive database of skills for potential employees and employers.
    With this application, users can better understand the real demands of the industries they wish to enter, allowing for informed career planning and preparation.
    """
        )
