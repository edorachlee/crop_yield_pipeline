"""
A custom function to replace NaNs in NOAA data. Current method is to replace NaNs with column mean, which is pretty barebones.
It has been intentionally separated from request_data.py for more robust preprocessing in the future.
"""
def process_nan(df):
    #Conduct imputation here
    new = df.fillna(df.mean())
    return new