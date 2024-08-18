from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st
import plotly_express as px
import numpy as np

st.title('Test plots')

nCol = 6

x1 = np.linspace(1, 10, 200)

print(x1)


fig = make_subplots(rows=1, cols=nCol, shared_yaxes=True)

for i in range(nCol):
    y1 = np.sin(x1)**i
    fig.add_trace(
        go.Scatter(x = y1, y = x1),
        row=1, col=i+1
    )


fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")
# fig.show()
st.plotly_chart(fig, theme="streamlit", use_container_width=True)


