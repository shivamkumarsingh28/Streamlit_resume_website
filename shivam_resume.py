import streamlit as st
from streamlit_option_menu import option_menu


import navbar, Intro, Project


selected =navbar.streamlit_menu()
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


if selected == "Intro":
    Intro.Intro()
if selected == "Project":
    selected=Project.horizontal_menu()
    if selected == "Home":
        st.title(f"You have selected {selected}")

    if selected == "Projects":
        st.title(f"You have selected {selected}")

    if selected == "Contact":
        st.title(f"You have selected {selected}")
if selected == "Education":
    st.title(f"You have selected {selected}")
if selected == "Experience":
    st.title(f"You have selected {selected}")
if selected == "Achievement":
    st.title(f"You have selected {selected}")
if selected == "Other":
    st.title(f"You have selected {selected}")