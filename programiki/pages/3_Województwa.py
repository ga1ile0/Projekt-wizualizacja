import streamlit as st
import pandas as pd
from streamlit_main import ch_option, woj_page


st.title("Województwa")
st.write("")


csv_files = ['average.csv']
ch_option(csv_files, woj_page)
