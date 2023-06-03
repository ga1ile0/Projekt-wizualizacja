import os
import pandas as pd


state_df = pd.DataFrame()
param_name = ['Cost', 'Rating', 'Comfort']
state_df[''] = pd.Series(param_name)

csv_files = os.listdir()

for file in csv_files:
    if file.endswith('.csv'):

        df = pd.read_csv(f'{file}')

        av_cost = df["Cost"].mean()
        av_rating = df["Rating"].mean()
        av_comfort = df["Comfort"].mean()

        param = [av_cost.round(), av_rating.round(2), av_comfort.round(2)]

        state_name = file[:-4]
        state_df[f'{state_name}'] = pd.Series(param)

df = state_df.to_csv('average.csv', index=False)

print(state_df)