import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15) #, color="pink"
st.pyplot(fig)

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

  #taxi_data = pd.read_csv('data/taxi_data.csv')
  #st.write(taxi_data.head())
  
with features:  
  st.header('These are the features:')

with model_training:
  st.header('Time to train the model!')
  
