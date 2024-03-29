# Pipeline to gather weather/soil data and annual corn yields in Missouri, Illinois, and Iowa for use in yield prediction models
Function: 
 - Requests daily min/max air temperature, min/max soil temperature, and precipitation levels from NOAA database. 
 - Requests annual corn yields of each agricultural district in Missouri, Illinois, and Iowa.
 - Visualizes yield rates for specified year on a map using the Folium package, along with basic weather statistics.
 - Intended to be a skeleton pipeline to request basic information from NOAA and USDA that can be used to construct yield prediction models.

Instructions: You will need Python3.8(or any Python IDE of your choice). Place all files into a single directory and run "main.py" by setting the desired year to retrieve data and see geographic data visualization.

Files:
 - NOAA.py: Contains parameters specific to querying NOAA weather database(currently hardcoded with list of states and features).
 - USDA.py: Similar to NOAA.py, but queries USDA database to request annual corn yield(also hardcoded with list of states and features).
 - process_nan.py: A custom function to replace NaNs in NOAA data. Current method is to replace NaNs with column mean, which is pretty barebones. It has been intentionally separated from request_data.py for more robust preprocessing in the future.
 - request_data.py: Uses NOAA.py and USDA.py to request the specified data.
 - display.py: Overlays data onto Folium map and displays basic statistics.
 - main.py: Run this script to see results. **Set desired year for visualization in this file.**
 
 Upcoming developments:
  - Adding a time slider to the map to view yield rates across multiple years.
  - Flesh out data preprocessing steps.
  - Increase number of weather stations queried in NOAA database.
  - Convert pipeline into workflow(e.g.Airflow).
  - Prep data for PostGRES ingestion.

Note: Performed as part of school work. Course number and instructor information have been omitted to prevent plagiarism.
