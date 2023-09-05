import streamlit as st

st.title('first streamlit 1')

st.header('This is my header')
st.text('Sentence number 1. Sentence number 2')

header = st.container()
with header:
  st.title('Welcome to my project')
  
