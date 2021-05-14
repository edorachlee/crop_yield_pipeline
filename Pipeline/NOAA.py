import requests
import pandas as pd
import numpy as np
import json
from datetime import datetime
from process_nan import process_nan

def fetch_weather(key, state, year, station_id):

       start_call = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'

       ###----------------------------------------------------------------------
       #Daily summaries of air temp, precipitation, and sunshine
       MO_station_id = 'GHCND:USC00231801'  # Columbia Univ of MO, MO
       IL_station_id = 'GHCND:USC00116344'  # OGDEN, IL US
       IA_station_id = 'GHCND:USC00130200'  # AMES 8 WSW, IA US

       datasetid = 'GHCND'
       datatypes = ['TMIN', 'TMAX', 'TOBS', 'SN32', 'SX32', 'PRCP']
       limit = 1000
       #year = 2017
       date_start = str(year)+'-01-01'
       date_end = str(year)+'-12-31'
       ###----------------------------------------------------------------------

       df = pd.DataFrame(columns=['Date'])
       #df_list = []
       for datatypeid in datatypes:
              # construct payload for request
              payload = {'datasetid': datasetid, 'datatypeid': datatypeid, 'stationid': station_id,
                         'startdate': date_start, 'enddate': date_end, 'limit': str(limit)}
              r = requests.get(start_call, headers={'token': key}, params = payload)
              d = json.loads(r.text)

              values = []
              dates = []
              for item in d['results']:
                  values.append(item['value'])
                  dates.append(item['date'])
              dict = {'Date': dates, datatypeid: values}
              col = pd.DataFrame(data = dict)
              #df_list.append(col)
              df=df.merge(col, on='Date', how='outer', sort=True)

       #Impute nans with column means
       df = process_nan(df)
       #Add state to dataframe
       df['State'] = [state for i in df.index]
       return df



