import os
import pandas as pd


state_df = pd.DataFrame(index=['Cost', 'Rating', 'Comfort'])
csv_files = os.listdir()

for file in csv_files:
    if file.endswith('.csv'):

        df = pd.read_csv(f'{file}')

        av_cost = df['Cost'].mean()
        av_rating = df['Rating'].mean()
        av_comfort = df['Comfort'].mean()

        state_name = file[:-4]
        state_df[state_name] = [av_cost.round(), av_rating.round(2), av_comfort.round(2)]

df = state_df.to_csv('average.csv', index=False)
print(state_df)
