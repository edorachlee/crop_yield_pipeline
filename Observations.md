#Personal observations when creating this data pipeline

Preprocessing: Not much to do(scaling, normalization, etc.). However, replacing NaNs in NOAA data could be much more robust. For example, replacing a NaN value by the mean of the current month(and not the whole year) would be more reasonable.
NOAA:
1. Conflicting documentation(V1? V2?)
2. Not all stations had features I was looking for (eg. Some stations would have weather and precipitation, but not soil data, and vice versa) - had to collect soil data from separate stations in the same state
3. Regarding soil temps - hard to unify a standard: had different depths, different covering types(sod, bare ground, etc.)
4. NOAA caps the maximum number of results in one call at 1000 results, so had to make multiple calls. One weird thing is that I’m unable to pull data for more than a year’s worth even though I’m very well under the results limit. So I’ve had to make separate calls for each year, for separate features.
5. From NOAA, air temps were very low or high in improbable amounts. Thus it seems to me that the temperature of the sensor surface is measured, not the actual air temperature itself. I checked the distribution, and was left-skewed but did not seem to be wacky or anything.
I quote weather.gov/lsx/excessiveheat-automobiles , “a dark dashboard or seat can easily reach temperatures in the range of 180 to more than 200 degrees F.” The same logic applies for cold temperatures.
6. Some years are missing chunks of data
7. Folium does not support newline operators in popup texts

Limitations: Currently, years can be changed but list of states is hardcoded, which detracts from modularity.
Works up only until 2019, as USDA data has not been collected for 2020.
Limited to one year only(did not add cumulative year function)

openWeather API: Free student version only goes back one year for historical data - not much use!
