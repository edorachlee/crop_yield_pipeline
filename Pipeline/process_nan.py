import pandas as pd
def process_nan(df):
    #Conduct imputation here
    new = df.fillna(df.mean())
    return new