import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

st.title('Plot sin(x)')
#st.button('Hit me')
st.subheader("f(x) = A*sin(B(x+C) + D")
a = st.slider('Select a value of a from [-10, 10]', value=1., min_value=-10., max_value=10.)
st.write("a = ", a)

x = np.arange(0, 4*np.pi, 0.1)
sinx = a * np.sin(x)
cosx = np.cos(x)

chart_data = pd.DataFrame(
   {
       "x": x,
       "sin": sinx,
       "cos": cosx
   }
)

st.line_chart(chart_data, x="x", y=["sin","cos"] )

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15) #, color="pink"
st.pyplot(fig)



  
