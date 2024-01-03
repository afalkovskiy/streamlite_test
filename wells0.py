print("wells0")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import plotly_express as px
import lasio as las
import os 

def create_plot(dataframe, curves_to_plot, log_curves=[]):

    print('from create_plot')
    print(dataframe)

    depth_curve = dataframe['DEPTH']

    # Count the number of tracks we need
    num_tracks = len(curves_to_plot)

    # Setup the figure and axes
    fig, ax = plt.subplots(nrows=1, ncols=num_tracks, figsize=(num_tracks*2, 10))

    # Create a super title for the entire plot
    # fig.suptitle(wellname, fontsize=20, y=1.05)
    # fig.suptitle(wellname, fontsize=16)

    # Loop through each curve in curves_to_plot and create a track with that data
    for i, curve in enumerate(curves_to_plot):

        ax[i].plot(dataframe[curve], depth_curve)

        # Setup a few plot cosmetics
        ax[i].set_title(curve, fontsize=12, fontweight='bold')
        ax[i].grid(which='major', color='lightgrey', linestyle='-')

        # We want to pass in the deepest depth first, so we are displaying the data
        # from shallow to deep
        ax[i].set_ylim(depth_curve.max(), depth_curve.min())

        # Only set the y-label for the first track. Hide it for the rest
        if i == 0:
            ax[i].set_ylabel('DEPTH (m)', fontsize=12, fontweight='bold')
        else:
            plt.setp(ax[i].get_yticklabels(), visible = False)

        # Check to see if we have any logarithmic scaled curves
        if curve in log_curves:
            ax[i].set_xscale('log')
            ax[i].grid(which='minor', color='lightgrey', linestyle='-')

    plt.tight_layout()
    # plt.show()
    st.pyplot(fig)

st.title('wells') 
st.text('This is a web app to plot well logs')
# st.markdown('## This is **markdown**')

st.sidebar.title('Navigation')
uploadedfile = st.sidebar.file_uploader('Upload your file here')
if uploadedfile:
    print("uploadedfile = ", uploadedfile)
    # df = pd.read_csv(uploaded_file)
    # st.session_state['df'] = uploaded_file

    uploadedfile.seek(0)  #RZ: reset buffer to beginning each time
    string = uploadedfile.read().decode()
    las_file = las.read(string)



    # las_file = las.read(uploaded_file)
    # df = las_file.df()
    # Create a column for the Well Name
    well_name = las_file.well.WELL.value

    print("well name: ", well_name)
    st.sidebar.header(well_name)

    df = las_file.df()
    print(df)

    curves_to_plot = ['GR', 'DT', 'RHOB', 'DPSS']

    logarithmic_curves = []

    # df = df.sort_values(['DEPTH']).reset_index(drop=True)
    df = df.reset_index()
    print(list(df.columns.values))

    create_plot(df, curves_to_plot, logarithmic_curves)
