import streamlit as st
import pandas as pd
from streamlit_main import ch_option, morze_page


st.title("Morze")
st.write("")

csv_files = ['av_morze1.csv', 'av_morze2.csv', 'av_morze2_1.csv', 'av_morze2_2.csv']
ch_option(csv_files, morze_page)

