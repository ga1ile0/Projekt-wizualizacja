import streamlit as st
import pandas as pd


def woj_page(name_of_csv):

    st.subheader("Noclegi według województw (7 nocy): ")
    st.write("")

    df = pd.read_csv(f'{name_of_csv}')
    df.index = ['koszt', 'ocena', 'komfort']

    st.dataframe(df, hide_index=False)
    st.write("")

    woj_df = pd.DataFrame(df.loc['koszt'])
    woj_df = woj_df.round(1).astype(int)
    st.dataframe(woj_df.style.highlight_min(axis=0, color='green').highlight_max(axis=0, color='red'))
    st.write("")

    st.line_chart(woj_df)
    st.write("")
    st.bar_chart(woj_df)


def city_page(name_of_csv):
    st.subheader("Noclegi według 20 najpopularniejszych miast (7 nocy): ")
    st.write("")

    df = pd.read_csv(f'{name_of_csv}')
    df.index = ['koszt', 'ocena', 'komfort']

    st.dataframe(df, hide_index=False)
    st.write("")

    woj_df = pd.DataFrame(df.loc['koszt'])
    woj_df = woj_df.round(1).astype(int)
    st.dataframe(woj_df.style.highlight_min(axis=0, color='green').highlight_max(axis=0, color='red'))
    st.write("")

    st.line_chart(woj_df)
    st.write("")
    st.bar_chart(woj_df)


st.title("Wakacje w Polsce")
st.write("")

page_names = ['1 dorosły', '2 dorosłych', '2 dorosłych, 1 dziecko', '2 dorosłych, 2 dzieci']

page = st.sidebar.radio('Wybierz opcję:', page_names)
st.write("")

csv_files = ['average.csv']
city_files = ['av_cities1.csv', 'av_cities2.csv', 'av_cities2_1.csv', 'av_cities2_2.csv']


if page == page_names[0]:
    woj_page(csv_files[0])
    city_page(city_files[0])

elif page == page_names[1]:
    woj_page(csv_files[0])##1
    city_page(city_files[1])

elif page == page_names[2]:
    woj_page(csv_files[0])##2
    city_page(city_files[2])

elif page == page_names[3]:
    woj_page(csv_files[0])##3
    city_page(city_files[3])




