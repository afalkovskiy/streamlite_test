from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st
import plotly_express as px
import numpy as np
st.set_page_config(layout="wide")
st.title('Test plots')

nCol = 6

x1 = np.linspace(1, 10, 200)
subt = ['title1', 'title2', 'title3', 'title4', 'title5', 'title6']

fig = make_subplots(rows=1, cols=nCol, shared_yaxes=True, subplot_titles=subt)

for i in range(nCol):
    y1 = np.sin(x1 * (i+1))
    fig.add_trace(
        go.Scatter(x = y1, y = x1),
        row=1, col=i+1
    )

    fig.layout.annotations[i].update(text="Subtitle " + str(i+1))
    fig.update_yaxes(title_text='yaxes title', mirror=True, showgrid=True, range=[10,0], row=1, col=i+1)


fig.update_layout(height=800, width=800, title_text="Side By Side Subplots")
# fig.update_layout(title_text="Side By Side Subplots")
# fig.layout.annotations[2].update(text="Stackoverflow")
# fig.show()
st.plotly_chart(fig, theme="streamlit", use_container_width=True)


