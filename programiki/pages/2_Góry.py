import streamlit as st
from streamlit_main import ch_option, gory_page


st.title("Góry")
st.divider()
st.write("")

csv_files = ['av_gory1.csv', 'av_gory2.csv', 'av_gory2_1.csv', 'av_gory2_2.csv']
ch_option(csv_files, gory_page)

