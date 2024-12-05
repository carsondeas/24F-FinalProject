# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/40_About.py", label="About", icon="🧠")


#### ------------------------ Role of student ------------------------
def StudentHomeNav():
    st.sidebar.page_link(
        "pages/00_Student_Home.py", label="Student Home", icon="🎓"
    )


def SkillManangementNav():
    st.sidebar.page_link(
        "pages/03_skill_management.py", label="Manage My Skills", icon="🎯"
    )

#### ------------------------ Examples for Role of professor ------------------------
def ProfessorHomeNav():
    st.sidebar.page_link(
        "pages/10_Professor_Home.py", label="Professor Home", icon="🏫"
    )

def CourseManangementNav():
    st.sidebar.page_link(
        "pages/14_manage_courses.py", label="Manage My Courses", icon="📚"
    )



#### ------------------------ Role of co-op advisor ------------------------
def ManageStudentsNav():
    st.sidebar.page_link(
        "pages/34_manage_students.py", label="Manage Students", icon="👨‍🎓"
    )

def ManageProfessorsNav():
    st.sidebar.page_link(
        "pages/35_manage_professors.py", label="Manage Professors", icon="🧑‍🏫"
    )


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=300)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show Student Home and Manage Skill Navigation Links fir students
        if st.session_state["role"] == "student":
            StudentHomeNav()
            SkillManangementNav()
        # Show Professor Home and Manage Skill Navigation Links fir students
        if st.session_state["role"] == "professor":
            ProfessorHomeNav()
            CourseManangementNav()

    # Show navigation links for co-op advisor
        elif st.session_state["role"] == "co-op_advisor":
            ManageStudentsNav()
            ManageProfessorsNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
