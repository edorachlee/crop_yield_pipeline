import requests
import pandas as pd
import json
"""
Contains parameters specific to querying USDA weather database(currently hardcoded with list of states and features).
"""

def fetch_yield(key, year, state, district_list):
    ###------------HARDCODED DATA------------###
    #What
    source_desc = 'SURVEY'
    sector_desc = 'CROPS'
    group_desc = 'FIELD CROPS'
    commodity_desc = 'CORN'
    statisticcat_desc = 'PRODUCTION'
    unit_desc = 'BU'
    format = 'JSON'

    #Where
    agg_level_desc = 'AGRICULTURAL DISTRICT'

    #When
    freq_desc = 'ANNUAL'
    reference_period_desc = 'YEAR'
    ###--------------------------------------###

    values = []
    start_call = ' http://quickstats.nass.usda.gov/api/api_GET'
    for district in district_list:
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
        d = json.loads(r.text)
        col = [item['Value'] for item in d['data']]
        values.append(col)

    df = pd.DataFrame(data=values, columns=['Annual Yield(BU)'])

    # Add state and county codes to dataframe
    df['State'] = [state for i in df.index]
    df['County Code'] = district_list
    return df