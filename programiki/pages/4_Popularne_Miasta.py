import streamlit as st
import pandas as pd
from streamlit_main import ch_option, city_page

st.title("Popularne miasta")
st.write("")

city_files = ['av_cities1.csv', 'av_cities2.csv', 'av_cities2_1.csv', 'av_cities2_2.csv']
ch_option(city_files, city_page)