import streamlit as st
from streamlit_main import ch_option, woj_page


st.title("Województwa")
st.divider()
st.write("")

csv_files = ['av_woj1.csv', 'av_woj2.csv', 'av_woj2_1.csv', 'av_woj2_2.csv']
ch_option(csv_files, woj_page)
