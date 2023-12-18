import streamlit as st
from PIL import Image

def Intro():
    image = Image.open('dp1.jpg')
    st.image(image, width=150)

    st.write('''
  # Shivam kumar singh resume.
  ''')


