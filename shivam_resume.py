import streamlit as st
from streamlit_option_menu import option_menu


import navbar, Intro, Project, component


selected =navbar.streamlit_menu()
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


if selected == "Intro":
    Intro.Intro()
    
    Intro.Summary("## Summary", 0)
if selected == "Project":
    selected=Project.horizontal_menu()
    if selected == "Python":
        # Intro.Summary("## Python")
        component.Project("## Python")
    if selected == "Java":
        # Intro.Summary("## Java")
        component.Project("## Java")
    if selected == "Php":
        # Intro.Summary("## Php")
        component.Project("## Php")
    if selected == "JavaScript":
        # Intro.Summary("## JavaScript")
        component.Project("## JavaScript")

if selected == "Education":
    component.Education("## Education")
if selected == "Experience":
    component.Education("## Experience")
if selected == "Achievement":
    component.Education("## Achievement")

if selected == "Other":
    component.Education("## Other")
