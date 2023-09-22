import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

st.title('Plot sin(x)')
#st.button('Hit me')

x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15) #, color="pink"
st.pyplot(fig)



  
