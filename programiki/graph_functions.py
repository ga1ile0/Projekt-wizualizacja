import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
import streamlit as st
import numpy as np

miasta = {
    "Jelenia Góra" : "Jelenia",
    "Nowy Targ" : "Nowy",
    "Zielona Góra" : "Zielona"
}

def data_type(name_of_csv):
    folder_name = {
        "av_cities1.csv": "../popularne_miasta_1os/",
        "av_cities2.csv": "../popularne_miasta_2os/",
        "av_cities2_1.csv": "../popularne_miasta_2+1/",
        "av_cities2_2.csv": "../popularne_miasta_2+2/",
        "av_woj1.csv" : "../woj1/",
        "av_woj2.csv" : "../woj2/",
        "av_woj2_1.csv" : "../woj2_1/",
        "av_woj2_2.csv" : "../woj2_2/"
    }
    return folder_name[name_of_csv]




def scatter_city(city_name, name_of_csv):
    threshold = 5
    file_path = ''
    if city_name in miasta:
        file_path = data_type(name_of_csv) + miasta[city_name] + '.csv'
    else:
        file_path = data_type(name_of_csv) + city_name + '.csv'
    fig, ax = plt.subplots()

    df = pd.read_csv(file_path, index_col = 0)
    x_values = df['Cost']
    y_values = df['Rating']
    #filtering loner dots
    x_zscores = np.abs((x_values - np.mean(x_values)) / np.std(x_values))
    y_zscores = np.abs((y_values - np.mean(y_values)) / np.std(y_values))
    filtered_x_values = []
    filtered_y_values = []
    for x, y, x_zscore, y_zscore in zip(x_values, y_values, x_zscores, y_zscores):
        if x_zscore < threshold and y_zscore < threshold:
            filtered_x_values.append(x)
            filtered_y_values.append(y)
    dot_size = 10
    ax.scatter(filtered_x_values, filtered_y_values, s=dot_size)
    ax.set_xlabel('Cena')
    ax.set_ylabel('Ocena')
    st.pyplot(fig)

def scatter_woj(woj_name, name_of_csv):
    threshold = 3
    file_path = data_type(name_of_csv) + woj_name + '.csv'
    fig, ax = plt.subplots()

    df = pd.read_csv(file_path, index_col=0)
    x_values = df['Cost']
    y_values = df['Rating']
    # filtering loner dots
    x_zscores = np.abs((x_values - np.mean(x_values)) / np.std(x_values))
    y_zscores = np.abs((y_values - np.mean(y_values)) / np.std(y_values))
    filtered_x_values = []
    filtered_y_values = []
    for x, y, x_zscore, y_zscore in zip(x_values, y_values, x_zscores, y_zscores):
        if x_zscore < threshold and y_zscore < threshold:
            filtered_x_values.append(x)
            filtered_y_values.append(y)
    dot_size = 10
    ax.scatter(filtered_x_values, filtered_y_values, s=dot_size)
    ax.set_xlabel('Cena')
    ax.set_ylabel('Ocena')
    st.pyplot(fig)

