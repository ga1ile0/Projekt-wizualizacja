import streamlit as st
from graph_functions import piechart_zaczynamy
from PIL import Image

st.title("Wakacje w Polsce")
st.divider()

col1, col2, col3 = st.columns([1, 15, 1])
image = Image.open("/Projekt-wizualizacja/tytułowa.jpeg")

with col1:
    st.write(' ')
with col2:
    st.image(image, width=600)
with col3:
    st.write(' ')

st.divider()

st.write('''
    Końcówka czerwca to czas, w którym w końcu trzeba zaplanować wakacje.
    Dla większości Polaków, wakacje odbędą się w kraju. 
    
    Według badań Polskiej Organizacji Turystycznej, przeprowadzonego 
    na przełomie maja i czerwca, **42%** badanych wybierze wyjazd nad morze,
    **22%** w góry, **19%** pojedzie nad jezioro, a **17%** wybierze inne miejsce.''')

st.write("")
piechart_zaczynamy()
st.divider()

st.write('''
    W momencie podejmowania decyzji odnośnie wyboru miejsca odpoczynku,
    warto jest porównać te miejsca pod względem kosztów związanych z noclegami.
    
    Nasza strona prezentuje analizę wielu popularnych miejsc w Polsce, 
    w oparciu o oferty z portalu Booking.com.
    
    Okres trwania noclegu został, przez nas wybrany na **7 nocy**, jako że jest to
    najczęstszy wybór Polaków - **65%** (rownież POT). Użytkownik będzie mógł sprawdzić
    dane dla różnej ilość osób.
    ''')

st.divider()


