import streamlit as st
import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(0)

# Define the start and end dates for the time series
start_date = '2022-01-01'
end_date = '2022-12-31'

# Generate the dates for the time series
dates = pd.date_range(start=start_date, end=end_date, freq='D')

# Generate the trend component
trend = np.arange(len(dates))

# Generate the monthly seasonality component
month_day = dates.day
month_seasonality = np.sin(2 * np.pi * month_day / 30)

# Generate the noise component
noise = np.random.normal(0, 10, len(dates))

# Calculate the final values by combining the trend, seasonality, and noise
values = trend + month_seasonality + noise

# Create the DataFrame
df = pd.DataFrame({'date': dates, 'value': values})

# Convert the 'value' column to floating-point numbers
df['value'] = df['value'].astype(float)

# steamlit code
st.write("""
# My first app
Hello *world!*
""")

# steamlit line chart
st.line_chart(df.set_index('date'))

# steamlit selectbox
option = st.selectbox(
    "Pick an animal",
    ["Dog","Cat","Fish"],
    )

# steamlit pick a date
date = st.date_input(
    "Pick a date",
    pd.to_datetime('2022-01-01'),
    )

# steamit slider
number = st.slider(
    "Pick a number",
    0,
    100,
    )
    