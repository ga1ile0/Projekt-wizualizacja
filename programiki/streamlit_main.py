import streamlit as st
import pandas as pd
from graph_functions import scatter_city, scatter_woj


##Todo: zmienić te funkcje woj_page, city_page, dodać kolejne, dodać funkcje rysujące wykresiki itp

def woj_page(name_of_csv):
    st.subheader("Noclegi według województw: ")
    st.write("")

    df = pd.read_csv(f'{name_of_csv}')
    df.index = ['koszt', 'ocena', 'komfort']

    st.dataframe(df, hide_index=False)
    st.write("")

    woj_df = pd.DataFrame(df.loc['koszt'])
    woj_df = woj_df.round(1).astype(int)
    

    st.subheader("Średni koszt noclegu")
    genre = st.radio(
        "Wybierz rodzaj wykresu",
        ('Słupkowy', 'Liniowy')
    )
    if genre == 'Liniowy':
        st.line_chart(woj_df)
        st.write("")
    else:
        st.bar_chart(woj_df)
        st.write("")

    st.subheader("Porównanie cen i ocen ogłoszeń")
    wojewodztwa = ('dolnośląskie', 'kujawsko-pomorskie', 'lubelskie', 'lubuskie', 'łódzkie', 'małopolskie', 'mazowieckie', 'opolskie', 'podkarpackie', 'podlaskie', 'pomorskie', 'śląskie', 'świętokrzyskie', 'warmińsko-Mazurskie', 'wielkopolskie', 'zachodniopomorskie')
    option1 = st.selectbox('Województwo', wojewodztwa)
    scatter_woj(option1, name_of_csv)

def city_page(name_of_csv):
    st.subheader("Noclegi według 20 najpopularniejszych miast: ")
    st.write("")

    df = pd.read_csv(f'{name_of_csv}')
    df.index = ['koszt', 'ocena', 'komfort']

    st.dataframe(df, hide_index=False)
    st.write("")

    woj_df = pd.DataFrame(df.loc['koszt'])
    woj_df = woj_df.round(1).astype(int)


    st.subheader("Średni koszt noclegu")
    genre = st.radio(
        "Wybierz rodzaj wykresu",
        ('Słupkowy', 'Liniowy')
    )
    if genre == 'Liniowy':
        st.line_chart(woj_df)
        st.write("")
    else:
        st.bar_chart(woj_df)
        st.write("")

    st.subheader("Porównanie cen i ocen ogłoszeń")
    miasta = ('Bydgoszcz', 'Gdańsk', 'Gliwice', 'Jelenia Góra', 'Kraków', 'Lublin', 'Nowy Targ', 'Olsztyn', 'Opole', 'Przemyśl', 'Sandomierz', 'Sanok', 'Szczecin', 'Toruń', 'Wadowice', 'Warszawa', 'Wrocław', 'Zamość', 'Zielona Góra', 'Łódź' )
    option1 = st.selectbox('Miasto', miasta)
    scatter_city(option1, name_of_csv)


def ch_option(csv_names, display_function):
    pages_names = ['1 dorosły', '2 dorosłych', '2 dorosłych, 1 dziecko', '2 dorosłych, 2 dzieci']
    page = st.sidebar.radio('Wybierz opcję:', pages_names)

    for i in range(4):
        if page == pages_names[i]:
            display_function(csv_names[i])
            break




