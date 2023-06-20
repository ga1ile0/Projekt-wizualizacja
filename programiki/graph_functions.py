import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
import streamlit as st

def data_type(name_of_csv):
    folder_name = {
        "av_cities1.csv": "../popularne_miasta_1os/",
        "av_cities2.csv": "../popularne_miasta_2os/",
        "av_cities2_1.csv": "../popularne_miasta_2+1/",
        "av_cities2_2.csv": "../popularne_miasta_2+2/",
    }
    return folder_name[name_of_csv]




def scatter(city_name, name_of_csv):

    file_path = data_type(name_of_csv) + city_name + '.csv'
    fig, ax = plt.subplots();

    df = pd.read_csv(file_path, index_col = 0)
    x_values = df['Cost']
    y_values = df['Rating']
    dot_size = 10;
    ax.scatter(x_values, y_values, s=dot_size)
    st.pyplot(fig)