import streamlit as st
from streamlit_option_menu import option_menu


import navbar, Intro, component


selected =navbar.streamlit_menu()
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


if selected == "Intro":
    Intro.Intro()
    
    component.Summary("## Summary" )
if selected == "Project":
    selected=navbar.horizontal_menu()
    if selected == "Python":
        # Intro.Summary("## Python")
        component.Project("## Python",12,13,14)
    if selected == "Php":
        # Intro.Summary("## Java")
        component.Project("## Php",15,16,17)
    if selected == "Java":
        # Intro.Summary("## Php")
        component.Project("## Java",18,19,20)
    if selected == "JavaScript":
        # Intro.Summary("## JavaScript")
        component.Project("## JavaScript",21,22,23)

if selected == "Education":
    component.Education("## Education", 0, 1, 2)
if selected == "Experience":
    component.Education("## Experience", 3,4,5)
if selected == "Achievement":
    component.Education("## Achievement",6,7,8)

if selected == "Other":
    component.Education("## Other",9,10,11)
