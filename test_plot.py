from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st
import plotly_express as px

st.title('Test plots')

nCol = 6

fig = make_subplots(rows=1, cols=nCol, shared_yaxes=True)

for i in range(nCol):
    fig.add_trace(
        go.Scatter(x=[1, 2 + i**2, 3, 4], y=[4, 15, 30, 85]),
        row=1, col=i
    )


fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")
# fig.show()
st.plotly_chart(fig, theme="streamlit", use_container_width=True)


