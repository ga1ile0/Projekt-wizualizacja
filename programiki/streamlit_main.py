import streamlit as st
import pandas as pd


st.title("Wakacje w Polsce")


csv_name = 'average.csv'
df = pd.read_csv(f'{csv_name}')


st.write(df)
woj_df = pd.DataFrame(df.loc[0, :])

woj_df.columns = ['Cost']
st.dataframe(woj_df)


st.line_chart(woj_df)
st.bar_chart(woj_df)
