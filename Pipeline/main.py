from request_data import request_data
from display import display
year=2019
df_NOAA, df_USDA = request_data(year)
print(df_NOAA)
print(df_USDA)
display(df_NOAA, df_USDA)

