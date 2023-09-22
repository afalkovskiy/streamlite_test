import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

st.title('Plot sin(x)')
#st.button('Hit me')

x = np.arange(0, 4*np.pi, 0.1)
sinx = np.sin(x)
cosx = np.cos(x)

chart_data = pd.DataFrame(
   {
       "x": x,
       "sin": sinx,
       "cos": cosx,
   }
)

st.line_chart(chart_data, x="x", y="sin", y="cos" )

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15) #, color="pink"
st.pyplot(fig)



  
