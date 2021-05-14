from NOAA import fetch_weather
from USDA import fetch_yield
import pandas as pd

def request_data(year):
    key_NOAA = 'yPFsuqYIqueOKcwwFXMYDrCEqnSGYiLK'
    key_USDA = '73E99788-D2E4-361F-858A-3ADA46264158'
    state_list = ['MO', 'IL', 'IA']
    #year = 2018

    stations = {'MO': 'GHCND:USC00231801', # Columbia Univ of MO, MO
                'IL': 'GHCND:USC00116344', # OGDEN, IL
                'IA': 'GHCND:USC00130200'} # AMES 8 WSW, IA
    districts = {'MO': ['10', '20', '30', '40', '50', '60', '70', '80', '90'],
                'IL': ['10', '20', '30', '40', '50', '60', '70', '80', '90'],
                'IA': ['10', '20', '30', '40', '50', '60', '70', '80', '90']}

    district_coords = {
        'MO': [[39.8931, -94.4047], [38.4604, -91.8617], [39.8059, -91.6223], [38.2572, -94.3400], [38.2144, -92.4283],
               [38.4108, -91.0752], [37.1063, -93.8329], [37.1573, -91.4005], [36.5944, -89.6519]],
        'IL': [[41.9333, -89.6167], [42.15, -88.2333], [40.6333, -90.4333], [40.75, -89.2667], [41.5833, -87.5167],
               [39.5333, -89.7], [39.3833, -88], [37.95, -89.15], [38.25, -88.3667]],
        'IA': [[43.2667, -95.3833], [43.25, -93.5], [43.0833, -91.6], [42.2167, -95.0833], [42.2167, -93.2333],
               [41.95, -90.8833], [41.1667, -94.9333], [41.1667, -93.55], [41.1667, -91.7167]]}

    #MO: DeKalb, Linn, Marion, Bates, Miller, Franklin, Lawrence, Shannon, New Madrid
    #IL: Whiteside, Kane, McDonough, Tazewell, Iroquois, Macoupin, Cumberland, Jackson, Hamilton
    #IA: O'Brien, Hancock, Fayette, Crawford, Story, Cedar, Montgomery, Clarke, Jefferson

    #MO_station_id = 'GHCND:USC00231801'  # Columbia Univ of MO, MO
    #IL_station_id = 'GHCND:USC00116344'  # OGDEN, IL US
    #IA_station_id = 'GHCND:USC00130200'  # AMES 8 WSW, IA US

    states_NOAA_data = []
    states_USDA_data = []
    for state in state_list:
        df_NOAA_state = fetch_weather(key_NOAA, state, year, stations[state])
        df_USDA_state = fetch_yield(key_USDA, year, state, districts[state])
        df_USDA_state['Coordinates'] = district_coords[state]
        states_NOAA_data.append(df_NOAA_state)
        states_USDA_data.append(df_USDA_state)

    df_NOAA = pd.concat(states_NOAA_data, ignore_index=True)
    df_USDA = pd.concat(states_USDA_data, ignore_index=True)

    return df_NOAA, df_USDA
