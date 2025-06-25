import streamlit as st
import requests
import pandas as pd
import io
import matplotlib.pyplot as plt
import GrabData as gd

gd.grab_data('https://files.zillowstatic.com/research/public_csvs/zori/Metro_zori_uc_sfrcondomfr_sm_month.csv?t=1750824099')

df = pd.read_csv('data.csv')

# Assume first 5 columns are floats (metadata), rest are time periods
# Skip first 5 columns for time series data
region_name = df.iloc[4, 0]
time_periods = df.columns[5:]
values = df.iloc[0, 5:].astype(float)

# Create a DataFrame for plotting
plot_df = pd.DataFrame({'Time': time_periods, 'Value': values})

st.write(f"Line chart for region: {region_name}")
st.line_chart(plot_df.set_index('Time'))