import streamlit as st
import pandas as pd
from graph_functions import scatter_city, scatter_woj, scatter_morze, scatter_gory, scatter_mazury, display_image


def common_plots(name_of_csv):
    df = pd.read_csv(f'{name_of_csv}')
    df.index = ['koszt', 'ocena', 'komfort']

    loc_df = pd.DataFrame(df.loc['koszt'])

    st.subheader("Średni koszt noclegu")

    col1, col2 = st.columns([5, 2])

    with col1:
        genre1, genre2 = st.tabs(["Wykres Słupkowy", "Wykres Liniowy"])

        with genre1:
            st.line_chart(loc_df)
            st.write("")
        with genre2:
            st.bar_chart(loc_df)
            st.write("")
    with col2:
        loc_df = loc_df.round(1).astype(int)
        st.dataframe(loc_df.style.highlight_min(axis=0, color='green').highlight_max(axis=0, color='red'))

    max = loc_df.idxmax()
    min = loc_df.idxmin()

    max_name = max.loc['koszt']
    min_name = min.loc['koszt']

    #print(loc_df.iloc[max]['koszt'])

    st.write(f'''
        Powyżej znajduje się wykres pokazujący, jak rozkładają się średnie ceny
        w poszczególnych miejscach.
        
        
        **{max_name}** - miejsce, w którym zapłacimy najwięcej
        
        **{min_name}** - miejsce, w którym zapłacimy najmniej
    ''')

    st.divider()
    st.write("")
    st.subheader("Średni koszt, ocena oraz komfort noclegu")
    st.write("")

    st.dataframe(df, hide_index=False)
    st.write("")
    st.write('''
        Użytkownicy portalu Booking.com oprócz zwykłej oceny obiektu, mogą również
        ocenić poziom komfortu w obiekcie. Pomimo tego, że te dane dotyczą w istocie tego samego,
        to czasami występują dosyć spore rozbieżności.          
    ''')
    st.write("")


def morze_page(name_of_csv):

    st.subheader("Pobyt nad Morzem")
    st.divider()
    st.write("")

    miasta = ('Darłowo', 'Dębki', 'Gdańsk', 'Gdynia', 'Hel', 'Jarosławiec', 'Jastrzębia', 'Karwia', 'Kopalino', 'Kołobrzeg', 'Mielno', 'Międzyzdroje', 'Pobierowo', 'Rewal', 'Rowy', 'Sopot', 'Stegna', 'Trzęsacz', 'Ustka', 'Ustronie', 'Władysławowo', 'Łeba', 'Świnoujście')
    option = st.selectbox('Miasto', miasta)
    st.write("")

    display_image(option, name_of_csv)
    st.divider()

    st.write('''
        Słońce, plaża, gorący piasek, szum fal. Pobyt nad morzem może być doskonałym sposobem
        na oderwanie się od codzienności. Nie bez przyczyny wybiera go aż **42%** Polaków. 

        Poniżej przedstawiamy listę popularnych nadmorskich miejsc, z której warto
        skorzystać szukając noclegu nad polskim morzem, mając na uwadze określony budżet.  

    ''')

    st.divider()
    common_plots(name_of_csv)
    st.divider()

    st.subheader("Stosunek oceny użytkowników do ceny noclegu")
    st.write("")
    scatter_morze(option, name_of_csv)
    st.write('''
        Czasem myślimy, że jeśli wydamy na coś więcej pieniędzy, to na pewno
        to coś będzie lepsze. Nie zawsze to prawda. Chociaż często.
        
        Powyżej znajduje się porównanie ocen użytkowników, do cen za pobyt 
        w danym obiekcie.
    ''')
    st.divider()


def gory_page(name_of_csv):

    st.subheader("Wyjazd w góry")
    st.divider()
    st.write("")

    miasta1 = ('Białka Tatrzańska', 'Bielsko-Biała', 'Brenna', 'Bukowina Tatrzańska', 'Jelenia Góra', 'Karpacz', 'Krynica-Zdrój', 'Kudowa-Zdrój', 'Nowy Targ', 'Nowy Sącz', 'Solina', 'Szczawnica',
              'Szczyrk', 'Szklarska Poręba', 'Ustroń', 'Wałbrzych', 'Wisła', 'Zakopane', 'Żywiec')
    option = st.selectbox('Miasto', miasta1)
    st.write("")

    display_image(option, name_of_csv)
    st.divider()

    st.write(''' 
            Dla osób kochających kontakt z naturą oraz aktywny sposób na odpoczynek,
            najlepszym sposobem na połączenie tych dwóch rzeczy jest wyjazd w piękne, 
            polskie góry.

            Poniżej znajduje się analiza kosztów związanych z takim wyjazdem.
        ''')

    st.divider()

    common_plots(name_of_csv)
    st.divider()

    st.subheader("Stosunek oceny użytkowników do ceny noclegu")
    st.write("")
    scatter_gory(option, name_of_csv)
    st.write('''
            Czasem myślimy, że jeśli wydamy na coś więcej pieniędzy, to na pewno
            to coś będzie lepsze. Nie zawsze to prawda. Chociaż często.

            Powyżej znajduje się porównanie ocen użytkowników, do cen za pobyt 
            w danym obiekcie.
        ''')
    st.divider()


def mazury_page(name_of_csv):
    st.subheader("Wakacje na mazurach")
    st.divider()
    st.write("")

    miasta = ('Ełk', 'Giżycko', 'Iława', 'Mikołajki', 'Mrągowo', 'Olsztyn', 'Ostróda', 'Ruciane-Nida')
    option = st.selectbox('Miasto', miasta)
    st.write("")

    display_image(option, name_of_csv)
    st.divider()

    st.write(''' 
               
           ''')

    st.divider()

    common_plots(name_of_csv)
    st.divider()

    st.subheader("Stosunek oceny użytkowników do ceny noclegu")
    st.write("")
    scatter_mazury(option, name_of_csv)
    st.write('''
            Czasem myślimy, że jeśli wydamy na coś więcej pieniędzy, to na pewno
            to coś będzie lepsze. Nie zawsze to prawda. Chociaż często.

            Powyżej znajduje się porównanie ocen użytkowników, do cen za pobyt 
            w danym obiekcie.
        ''')
    st.divider()


def woj_page(name_of_csv):
    st.subheader("Noclegi według województw")
    st.divider()
    st.write("")

    wojewodztwa = ('dolnośląskie', 'kujawsko-pomorskie', 'lubelskie', 'lubuskie', 'łódzkie', 'małopolskie', 'mazowieckie', 'opolskie', 'podkarpackie', 'podlaskie', 'pomorskie', 'śląskie', 'świętokrzyskie', 'warmińsko-mazurskie', 'wielkopolskie', 'zachodniopomorskie')
    option1 = st.selectbox('Województwo', wojewodztwa)
    st.write("")

    display_image(option1, name_of_csv)
    st.divider()

    st.write(''' 
              
           ''')

    st.divider()

    common_plots(name_of_csv)
    st.divider()

    st.subheader("Stosunek oceny użytkowników do ceny noclegu")
    st.write("")
    scatter_woj(option1, name_of_csv)
    st.write('''
            Czasem myślimy, że jeśli wydamy na coś więcej pieniędzy, to na pewno
            to coś będzie lepsze. Nie zawsze to prawda. Chociaż często.

            Powyżej znajduje się porównanie ocen użytkowników, do cen za pobyt 
            w danym obiekcie.
        ''')
    st.divider()


def city_page(name_of_csv):
    st.subheader("Noclegi w ciekawych polskich miastach")
    st.divider()
    st.write("")

    miasta = ('Bydgoszcz', 'Gdańsk', 'Gliwice', 'Jelenia Góra', 'Kraków', 'Lublin', 'Nowy Targ', 'Olsztyn', 'Opole', 'Przemyśl', 'Sandomierz', 'Sanok', 'Szczecin', 'Toruń', 'Wadowice', 'Warszawa', 'Wrocław', 'Zamość', 'Zielona Góra', 'Łódź' )
    option1 = st.selectbox('Miasto', miasta)
    st.write("")

    display_image(option1, name_of_csv)
    st.divider()

    st.write(''' 
        Dla miłośników zwiedzania zabytków oraz architektury ciekawą opcją
        może być spędzenie wakacji w jednym z miast, które oferuje takie atrakcje.
        
        Poniżej znajdują się odznaczające na tle innych, polskie warte zwiedzenia miasta.
            ''')

    st.divider()

    common_plots(name_of_csv)
    st.divider()

    st.subheader("Stosunek oceny użytkowników do ceny noclegu")
    st.write("")
    scatter_city(option1, name_of_csv)
    st.write('''
            Nie zawsze więcej znaczy lepiej - Powyżej znajduje się porównanie 
            ocen użytkowników, do cen za pobyt w danym obiekcie. 
        ''')
    st.divider()


def ch_option(csv_names, display_function):
    pages_names = ['1 dorosły', '2 dorosłych', '2 dorosłych, 1 dziecko', '2 dorosłych, 2 dzieci']
    page = st.sidebar.radio('Wybierz opcję:', pages_names)

    for i in range(4):
        if page == pages_names[i]:
            display_function(csv_names[i])
            break




