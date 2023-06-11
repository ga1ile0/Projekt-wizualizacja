import streamlit as st
import pandas as pd


csv_name = 'AVERAGE_FOR_STATES.csv'
df = pd.read_csv(f'{csv_name}')

st.write(df)
