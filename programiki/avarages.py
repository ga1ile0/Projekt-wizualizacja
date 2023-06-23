import pandas as pd
import glob

# Define a list of directory paths
directories = ['../morze1', '../morze2', '../morze2_1', '../morze2_2', ]

# Initialize a dictionary to store the maximum average costs for each directory
max_averages = {}

# Iterate over each directory
for directory in directories:
    # Get a list of all CSV files in the current directory
    csv_files = glob.glob(directory + "/*.csv")

    # Initialize variables to keep track of the maximum average and its corresponding file
    max_avg = -float('inf')
    max_avg_file = ""

    # Iterate over each CSV file in the current directory
    for file in csv_files:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file)

        # Calculate the average cost
        avg_cost = df['Cost'].mean()

        # Check if the current average is larger than the previous maximum
        if avg_cost > max_avg:
            max_avg = avg_cost
            max_avg_file = file

    # Store the maximum average and its corresponding file in the dictionary
    max_averages[directory] = {'file': max_avg_file, 'average_cost': max_avg}

# Create a DataFrame from the max_averages dictionary
df_max_averages = pd.DataFrame.from_dict(max_averages, orient='index')

# Save the maximum averages to a CSV file
df_max_averages.to_csv('morze_lac.csv', index_label='directory')


def piechart_average():
    data = {
        'destination': ['Morze', 'Góry', 'Mazury'],
        'volume': [4892.025, 3858.22, 3943.253]
    }

    data = {
        'destination': ['Morze', 'Góry', 'Mazury'],
        'volume': [4892.025, 3858.22, 3943.253]
    }

    df = pd.DataFrame(data)

    # Hide the table by creating an empty placeholder
    table_placeholder = st.empty()

    labels = [f"{d} <br>{v} zł" for d, v in
              zip(df['destination'], df['volume'])]  # Combine destination and volume values for labels

    fig = px.pie(df, names='destination', values='volume', title='Plany Polaków na wakacje')
    fig.update_traces(textposition='inside', text=labels, textinfo='text')

    # Replace the placeholder with the pie chart
    table_placeholder.plotly_chart(fig, use_container_width=True)

    st.markdown("Żródło: pot.gov.pl")