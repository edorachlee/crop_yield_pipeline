import folium
import webbrowser
from sklearn.preprocessing import MinMaxScaler

def display(df_NOAA, df_USDA):
    #min-max normalization for radius calculation
    df_USDA['Radius'] = MinMaxScaler(feature_range=(1,3)).fit_transform(
        df_USDA['Annual Yield(BU)'].str.replace(',', '').astype(float).values.reshape(-1,1))

    print(df_USDA['Radius'])

    m = folium.Map(location=[40.3660, -91.5112], zoom_start = 6)

    for i in range(len(df_USDA.index)):
        folium.CircleMarker(
        df_USDA.loc[i, 'Coordinates'],
        popup=('Annual Yield(BU): ' + str(df_USDA.loc[i, 'Annual Yield(BU)'])
               + '   Avg. Min Air Temp.: ' + str(round(df_NOAA['TMIN'].mean(), 1))
               + '   Avg. Max Air Temp.: ' + str(round(df_NOAA['TMAX'].mean(), 1))
               + '   Avg. Min Soil Temp.: ' + str(round(df_NOAA['SN32'].mean(), 1))
               + '   Avg. Max Soil Temp.: ' + str(round(df_NOAA['SX32'].mean(), 1))
               + '   Avg. Precipitation: ' + str(round(df_NOAA['PRCP'].mean(), 1))
               ),
        color='b',
        radius=10 * df_USDA.loc[i, 'Radius'],
        fill_color='crimson',
        fill=True,
        fill_opacity=0.7
        ).add_to(m)

    m.save('map.html')
    url = 'file:///Users/buggu/Desktop/info577/map.html'
    webbrowser.open(url, new=2)

