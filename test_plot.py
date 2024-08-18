from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st
import plotly_express as px

st.title('Test plots')


fig = make_subplots(rows=1, cols=2, shared_yaxes=True)

fig.add_trace(
    go.Scatter(x=[1, 2, 3, 4], y=[4, 5, 6, 85]),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
    row=1, col=2
)

fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")
# fig.show()
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

fig1 = make_subplots(rows=2, cols=2, start_cell="bottom-left")

fig1.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
              row=1, col=1)

fig1.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
              row=1, col=2)

fig1.add_trace(go.Scatter(x=[300, 400, 500], y=[600, 700, 800]),
              row=2, col=1)

fig1.add_trace(go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]),
              row=2, col=2)

fig1.update_layout(height=600, width=800, title_text="Multiple subplots")
# fig.show()
st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
