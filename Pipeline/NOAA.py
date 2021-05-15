import requests
import pandas as pd
import json
from process_nan import process_nan
"""
Contains parameters specific to querying NOAA weather database(currently hardcoded with list of states and features).
"""

def fetch_weather(key, state, year, station_id):
       ###------------HARDCODED DATA------------###
       datasetid = 'GHCND'
       datatypes = ['TMIN', 'TMAX', 'TOBS', 'SN32', 'SX32', 'PRCP']
       limit = 1000
       date_start = str(year)+'-01-01'
       date_end = str(year)+'-12-31'
       ###--------------------------------------###

       df = pd.DataFrame(columns=['Date'])
       start_call = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'
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
              df=df.merge(col, on='Date', how='outer', sort=True)

       #Impute nans with column means
       df = process_nan(df)

       #Add state to dataframe
       df['State'] = [state for i in df.index]
       return df



