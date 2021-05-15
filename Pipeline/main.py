from request_data import request_data
from display import display
"""
Run this script to see results. Set desired year for visualization in this file.
"""
year=2019 #Set desired year
df_NOAA, df_USDA = request_data(year)
print(df_NOAA)
print(df_USDA)
display(df_NOAA, df_USDA)

