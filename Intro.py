import streamlit as st
from PIL import Image

import database_config

database_url = "https://docs.google.com/spreadsheets/d/1rbpLQycntZzSAyTraFm6-Nvh0kzg95xbWCWF_mBvX6k/edit?usp=sharing"
Database = database_config.SaeeAM_query(f'SELECT * FROM "{database_url}"')


def Intro():
    image = Image.open('dp1.jpg')
    st.image(image, width=150)

    st.write('''
  # Shivam kumar singh resume.
  ''')

def Summary(title, table_no=0):
    st.markdown(title, unsafe_allow_html=True)
    for summary in Database:
        if summary[table_no] !=None:
            st.info(summary[table_no])
