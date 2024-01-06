import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px
import lasio as las

import matplotlib 
matplotlib.rc('xtick', labelsize=6) 
matplotlib.rc('ytick', labelsize=6) 
# import os

count = 0
wellList = []
st.set_page_config(layout="wide")


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

def create_plot2(wellnames, dfs_wells, curves_to_plot, log_curves=[]):

    num_wells = len(wellnames)

    # Count the number of tracks we need
    num_tracks = (len(curves_to_plot) + 1) * num_wells

    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = False

    # Setup the figure and axes
    fig, ax = plt.subplots(nrows=1, ncols=num_tracks, sharey=True)

    # fig.tight_layout()
    # fig.suptitle(wellname, fontsize=16)

    colorArr = ["tab:blue", "tab:orange", "tab:green"]

    for k, well_name in enumerate(wellnames):
        print("************** k = ", k)

        depth_curve = dfs_wells[k]['DEPTH']
        dataframe = dfs_wells[k]

        # Loop through each curve in curves_to_plot and create a track with that data
        for i, curve in enumerate(curves_to_plot):

            i1 = k * (len(curves_to_plot) + 1) + i

            print("num_wells = ", num_wells, "i = ", i, " k = ", k, "i1 = ", i1)

            ax[i1].plot(dataframe[curve], depth_curve, color=colorArr[i%3], linewidth=0.4,alpha=0.8)

            # Setup a few plot cosmetics
            # ax[i1].set_title(curve, fontsize=12, fontweight='bold')

            if k % 2==0:

                if i==1:
                    xtitle1 = r"$\bf{" + well_name + "}$" + ' \n' + curve
                    # xtitle1 = r"${" + well_name + "}$" + ' \n' + curve
                else:
                    xtitle1 = ' \n' + curve

            else:
                if i==1:
                    xtitle1 = r"$\bf{" + well_name + "}$" + ' \n\n' + curve
                else:
                    xtitle1 = ' \n' + ' \n' + curve

            ax[i1].set_title(xtitle1, fontsize=5)
            ax[i1].grid(which='major', color='lightgrey', linestyle='-')
            ax[i1].tick_params(axis='x', rotation=90)
            for axis in ['top', 'bottom', 'left', 'right']:
                ax[i1].spines[axis].set_linewidth(0.25)  # change width
                ax[i1].spines[axis].set_color('black')    # change color
                # ax[i1].tick_params(direction='out', length=6, width=2, colors='r',
                #     grid_color='r', grid_alpha=0.5)
                
                ax[i1].tick_params(direction='out', length=1.5, width=0.25, grid_alpha=0.5)

            # We want to pass in the deepest depth first, so we are displaying the data
            # from shallow to deep
            ax[i1].set_ylim(depth_curve.max(), depth_curve.min())

            # Only set the y-label for the first track. Hide it for the rest

            if (i == 0)&(k==0):
                # ax[i1].set_ylabel('DEPTH (m)', fontsize=12, fontweight='bold')
                ax[i1].set_ylabel('DEPTH', fontsize=5)
            else:
                if (i==len(curves_to_plot)-1)&(k==len(wellnames)-1):
                    ax[i1].yaxis.set_ticks_position('right')
                    ax[i1].yaxis.set_label_position("right")
                    ax[i1].set_ylabel('DEPTH', fontsize=5)
                else:
                    plt.setp(ax[i1].get_yticklabels(), visible = False)


            # Check to see if we have any logarithmic scaled curves
            if curve in log_curves:
                ax[i1].set_xscale('log')
                ax[i1].grid(which='minor', color='lightgrey', linestyle='-')



        # i2 = k * (len(curves_to_plot) + 1)
        # # print("num_wells = ", num_wells, "i = ", i, " k = ", k, "i1 = ", i1)
        # #
        # ax[i2].set_visible(False)
        i2 = (k + 1) * (len(curves_to_plot) + 1) - 1
        ax[i2].set_visible(False)


    # plt.tight_layout()
    plt.subplots_adjust(wspace=0.0)
    # plt.show()
    st.pyplot(fig)


st.title('Wells 2')
# st.markdown('## This is **markdown**')

st.sidebar.title('Navigation')

# Initialise empty list for dataframes
df_list = []
uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files=True)
if uploaded_files:
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        # st.sidebar.write("filename:", uploaded_file.name)
        # st.write(bytes_data)  

        count = count + 1;

        uploaded_file.seek(0)  #RZ: reset buffer to beginning each time
        string = uploaded_file.read().decode()
        las_file = las.read(string)


        well_name = las_file.well.WELL.value
        # st.subheader(well_name)

        # curves_to_plot = ['GR', 'DT', 'RHOB', 'DPSS']
        curves_to_plot =[]


        for curve in las_file.curves:
            curves_to_plot.append(curve.mnemonic)

        logarithmic_curves = []

        df = las_file.df()
        # df = df.reset_index()
        # print(list(df.columns.values))

        # create_plot(df, curves_to_plot, logarithmic_curves)

                # Create a column for the Well Name
        well_name = las_file.well.WELL.value

        print("well name: ", well_name)

        df['WELL'] = well_name

            # Make sure depth is a column rather than an index
        df = df.reset_index()
        df = df.sort_values(['WELL', 'DEPTH']).reset_index(drop=True)
        df_list.append(df)

    # Create a single dataframe with all wells
    well_df = pd.concat(df_list)   


    grouped =well_df.groupby('WELL')
    print(grouped.head())

    # Create empty lists
    dfs_wells = []
    wellnames = []

    #Split up the data by well
    for well, data in grouped:
        dfs_wells.append(data)
        wellnames.append(well)

    for i, well in enumerate(wellnames):
        print(f'Index: {i} - {well}')

    # curves_to_plot = ['GR', 'DT', 'RHOB', 'DPSS']

    logarithmic_curves = []

    well = 0

    # options = st.sidebar.multiselect(
    # 'Select well logs:',
    # ['GR', 'DT', 'RHOB', 'DPSS'],
    # ['DT', 'RHOB'])

    print(well_df)
    print("col list: " , well_df.columns.tolist())
    all_logs = []
    for log_name in well_df.columns.tolist():
        if ((log_name!='DEPTH') & (log_name!='WELL')):
            all_logs.append(log_name)

    print('log names', all_logs)  
    sel_logs = [all_logs[1], all_logs[2]]

    options = st.sidebar.multiselect('Select well logs:', all_logs, sel_logs)

    # st.write('You selected:', options)



    create_plot2(wellnames, dfs_wells, options, logarithmic_curves)


    st.sidebar.write("Number of wells: ", count)
