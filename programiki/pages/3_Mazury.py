import streamlit as st
from streamlit_main import ch_option, mazury_page


st.title("Mazury")
st.divider()
st.write("")

csv_files = ['av_mazury1.csv', 'av_mazury2.csv', 'av_mazury2_1.csv', 'av_mazury2_2.csv']
ch_option(csv_files, mazury_page)

