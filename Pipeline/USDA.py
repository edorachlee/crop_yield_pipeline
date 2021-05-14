import requests
import pandas as pd
import numpy as np
import json
from datetime import datetime

def fetch_yield(key, year, state, district_list):

    #key = '1EBC1628-CE23-3603-A9DA-2CCF4BFDDFCE'
    start_call = ' http://quickstats.nass.usda.gov/api/api_GET'
    ###-----------------------------------------------------------------
    #What
    source_desc = 'SURVEY'
    sector_desc = 'CROPS'
    group_desc = 'FIELD CROPS'
    commodity_desc = 'CORN'
    statisticcat_desc = 'PRODUCTION'
    unit_desc = 'BU'
    format = 'JSON'

    #Where
    #agg_level_desc = 'STATE'
    #states = ['MO', 'IL', 'IA']  # state_alpha
    agg_level_desc = 'AGRICULTURAL DISTRICT'

    #When
    #year = 2017
    freq_desc = 'ANNUAL'
    reference_period_desc = 'YEAR'
    ###-----------------------------------------------------------------

    values = []
    for district in district_list:
        #print(district)
        payload = {'key': key,
                   'source_desc': source_desc,
                   'sector_desc': sector_desc,
                   'group_desc': group_desc,
                   'agg_level_desc': agg_level_desc,
                   'state_alpha': state,
                   'asd_code': district,
                   'commodity_desc': commodity_desc,
                   'statisticcat_desc': statisticcat_desc,
                   'unit_desc': unit_desc,
                   'year': str(year),
                   'freq_desc': freq_desc,
                   'reference_period_desc': reference_period_desc,
                   'format': format}
        r = requests.get(start_call, params=payload)
        # r = requests.get('http://quickstats.nass.usda.gov/api/api_GET/?key='+key+'&commodity_desc=CORN&year=2012&state_alpha=VA&format=JSON')
        d = json.loads(r.text)
        #print(d)
        col = [item['Value'] for item in d['data']]
        #print(column_data)
        values.append(col)

    df = pd.DataFrame(data=values, columns=['Annual Yield(BU)'])
    #df['Annual Yield(BU)'] = df['Annual Yield(BU)'].str.replace(',', '')
    # Add state to dataframe
    df['State'] = [state for i in df.index]
    df['County Code'] = district_list
    return df