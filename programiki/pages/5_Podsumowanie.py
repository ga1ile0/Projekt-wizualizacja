import streamlit as st
from PIL import Image
from graph_functions import piechart_average


st.title("Podsumowanie")
st.divider()

col1, col2, col3 = st.columns([1, 15, 1])
image = Image.open("../podsum.jpg")#do zmiany zdjęcie

with col1:
    st.write(' ')
with col2:
    st.image(image, width=600)
with col3:
    st.write(' ')

st.divider()
piechart_average()
st.divider()

st.write('''
    Widzimy, że jeżeli jest duży popyt, to ceny rosną - najwięcej zapłacimy za
    pobyt nad Morzem, ale też najwięcej Polaków spędza tam swoje wakacje.
    
    W przypadku gór oraz Mazur, ceny są bardzo zbliżone, co również pokrywa się
    ze statystykami.
''')

st.divider()