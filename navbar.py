import streamlit as st
from streamlit_option_menu import option_menu

def streamlit_menu():
    with st.sidebar:
        selected = option_menu(
            menu_title="Shivam resume",  # required
            options=["Intro", "Project", "Education", "Experience", "Achievement", "Other"],  # required
            icons=["house", "browser-chrome", "book","degree","medal", "envolpe"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
        )
    return selected