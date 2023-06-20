import streamlit as st
import pandas as pd
from streamlit_main import ch_option, woj_page


st.title("Województwa")
st.write("")


csv_files = ['av_woj1.csv', 'av_woj2.csv', 'av_woj2_1.csv', 'av_woj2_2.csv']
ch_option(csv_files, woj_page)
