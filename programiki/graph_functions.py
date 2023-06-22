import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import seaborn as sns
import plotly.express as px
from PIL import Image


miasta = {
    "Jelenia Góra": "Jelenia",
    "Nowy Targ": "Nowy",
    "Zielona Góra": "Zielona",
    "Białka Tatrzańska": "Białka",
    "Bukowina Tatrzańska": "Bukowina",
    "Szklarska Poręba": "Szklarska"
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
        "av_woj2_2.csv" : "../woj2_2/",
        "av_morze1.csv" : "../morze1/",
        "av_morze2.csv" : "../morze2/",
        "av_morze2_1.csv" : "../morze2_1/",
        "av_morze2_2.csv" : "../morze2_2/",
        "av_gory1.csv" : "../gory1/",
        "av_gory2.csv" : "../gory2/",
        "av_gory2_1.csv" : "../gory2_1/",
        "av_gory2_2.csv" : "../gory2_2/",
        "av_mazury1.csv": "../mazury1/",
        "av_mazury2.csv": "../mazury2/",
        "av_mazury2_1.csv": "../mazury2_1/",
        "av_mazury2_2.csv": "../mazury2_2/"

    }
    return folder_name[name_of_csv]


def display_image(city_name, name_of_csv):

    dt = data_type(name_of_csv)[:5]
    if dt == "../mo":
        dt = "../morze_zdj"
    elif dt == "../ma":
        dt = "../mazury_zdj"
    elif dt == "../go":
        dt = "../gory_zdj"
    elif dt == "../po":
        dt = "../popularne_miasta_zdj"
    elif dt == "../wo":
        dt = "../wojewodztwa_zdj"

    c_name = ""
    if city_name in miasta:
        c_name = miasta[city_name]
    else:
        c_name = city_name

    file_path = dt + "/" + c_name + '.jpg'

    col1, col2, col3 = st.columns([1, 15, 1])
    image = Image.open(file_path)

    with col1:
        st.write(' ')
    with col2:
        st.image(image, width=600)
    with col3:
        st.write(' ')


def scatter_morze(city_name, name_of_csv):
    threshold = 5
    file_path = data_type(name_of_csv) + city_name + '.csv'
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


def scatter_gory(city_name, name_of_csv):
    threshold = 5
    file_path = ''
    if city_name in miasta:
        file_path = data_type(name_of_csv) + miasta[city_name] + '.csv'
    else:
        file_path = data_type(name_of_csv) + city_name + '.csv'
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


def scatter_mazury(city_name, name_of_csv):
    threshold = 5
    file_path = data_type(name_of_csv) + city_name + '.csv'
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


def piechart_zaczynamy():
    data = {
        'destination': ['Morze', 'Góry', 'Jeziora', 'Inne'],
        'volume': [42, 22, 19, 17]
    }

    df = pd.DataFrame(data)

    # Hide the table by creating an empty placeholder
    table_placeholder = st.empty()

    fig = px.pie(df, names='destination', values='volume', title='Plany Polaków na wakacje',
                 height=300, width=200)

    fig.update_layout(margin=dict(l=20, r=20, t=30, b=0))

    # Replace the placeholder with the pie chart
    table_placeholder.plotly_chart(fig, use_container_width=True)

    st.markdown("Żródło: pot.gov.pl")


