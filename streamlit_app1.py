import streamlit as st

st.title('first streamlit 1')

st.header('This is my header')
st.text('Sentence number 1. Sentence number 2')

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()
with header:
  st.title('Welcome to my project')
  st.text('The following is a description of my project')

with dataset:
  st.header('NYC taxi dataset')
  st.text('this dataset is from...')
  
with features:  
  st.header('These are the features:')

with model_training:
  st.header('Time to train the model!')
  
