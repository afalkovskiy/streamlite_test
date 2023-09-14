import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.random(10,2),
columns=['x','y'])
st.area_chart(df)
