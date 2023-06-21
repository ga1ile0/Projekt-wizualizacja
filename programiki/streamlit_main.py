import streamlit as st
import pandas as pd
from graph_functions import scatter_city, scatter_woj, scatter_morze, scatter_gory, scatter_mazury


def common_plots(name_of_csv):
    df = pd.read_csv(f'{name_of_csv}')
    df.index = ['koszt', 'ocena', 'komfort']

    woj_df = pd.DataFrame(df.loc['koszt'])
    col1, col2 = st.columns([2, 1])

    with col1:
        genre1, genre2 = st.tabs(["Wykres Słupkowy", "Wykres Liniowy"])

        with genre1:
            st.line_chart(woj_df)
            st.write("")
        with genre2:
            st.bar_chart(woj_df)
            st.write("")

    with col2:
        woj_df = woj_df.round(1).astype(int)
        st.dataframe(woj_df.style.highlight_min(axis=0, color='green').highlight_max(axis=0, color='red'))

    st.write("")
    st.subheader("Średni koszt, ocena oraz komfort noclegu")
    st.write("")

    st.dataframe(df, hide_index=False)
    st.write("")
    st.write("")

def morze_page(name_of_csv):
    st.subheader("Porównanie kosztów i ocen ogłoszeń")
    st.write("")

    st.subheader("Średni koszt noclegu")
    common_plots(name_of_csv)
    st.subheader("Porównanie kosztów i ocen ogłoszeń")
    miasta = ('Darłowo', 'Dębki', 'Gdańsk', 'Gdynia', 'Hel', 'Jarosławiec', 'Jastrzębia', 'Karwia', 'Kopalino', 'Kołobrzeg', 'Mielno', 'Międzyzdroje', 'Pobierowo', 'Rewal', 'Rowy', 'Sopot', 'Stegna', 'Trzęsacz', 'Ustka', 'Ustronie', 'Władysławowo', 'Łeba', 'Świnoujście')
    option = st.selectbox('Miasto', miasta)
    scatter_morze(option, name_of_csv)

def gory_page(name_of_csv):
    st.subheader("Porównanie kosztów i ocen ogłoszeń")
    st.write("")

    st.subheader("Średni koszt noclegu")
    common_plots(name_of_csv)
    st.subheader("Porównanie kosztów i ocen ogłoszeń")
    miasta1 = ('Białka Tatrzańska', 'Bielsko-Biała', 'Brenna', 'Bukowina Tatrzańska', 'Jelenia Góra', 'Karpacz', 'Krynica-Zdrój', 'Kudowa-Zdrój', 'Nowy Targ', 'Nowy Sącz', 'Solina', 'Szczawnica',
              'Szczyrk', 'Szklarska Poręba', 'Ustroń', 'Wałbrzych', 'Wisła', 'Zakopane', 'Żywiec')
    option = st.selectbox('Miasto', miasta1)
    scatter_gory(option, name_of_csv)


def mazury_page(name_of_csv):
    st.subheader("Porównanie kosztów i ocen ogłoszeń")
    st.write("")

    st.subheader("Średni koszt noclegu")
    common_plots(name_of_csv)
    st.subheader("Porównanie kosztów i ocen ogłoszeń")
    miasta = ('Ełk', 'Giżycko', 'Iława', 'Mikołajki', 'Mrągowo', 'Olsztyn', 'Ostróda', 'Ruciane-Nida')
    option = st.selectbox('Miasto', miasta)
    scatter_mazury(option, name_of_csv)

def woj_page(name_of_csv):
    st.subheader("Noclegi według województw: ")
    st.write("")
    st.write("")

    st.subheader("Średni koszt noclegu")

    common_plots(name_of_csv)

    st.subheader("Porównanie kosztów i ocen ogłoszeń")
    wojewodztwa = ('dolnośląskie', 'kujawsko-pomorskie', 'lubelskie', 'lubuskie', 'łódzkie', 'małopolskie', 'mazowieckie', 'opolskie', 'podkarpackie', 'podlaskie', 'pomorskie', 'śląskie', 'świętokrzyskie', 'warmińsko-mazurskie', 'wielkopolskie', 'zachodniopomorskie')
    option1 = st.selectbox('Województwo', wojewodztwa)
    scatter_woj(option1, name_of_csv)


def city_page(name_of_csv):
    st.subheader("Noclegi według 20 najpopularniejszych miast: ")
    st.write("")

    common_plots(name_of_csv)

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




