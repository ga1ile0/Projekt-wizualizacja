import streamlit as st
from PIL import Image
from graph_functions import piechart_average

st.title("Podsumowanie")
st.divider()

col1, col2, col3 = st.columns([1, 15, 1])
image = Image.open("../tytułowa.jpeg")#do zmiany zdjęcie

with col1:
    st.write(' ')
with col2:
    st.image(image, width=600)
with col3:
    st.write(' ')

piechart_average()

st.divider()