###############################################################################
# Import packages

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cartopy.crs as ccrs
import requests
# import datetime
from datetime import (date, datetime)
import json
from wrf import (getvar, latlon_coords)

###############################################################################
# Code pulled from https://towardsdatascience.com/getting-weather-data-in-3-easy-steps-8dc10cc5c859
# NOAA API https://www.ncdc.noaa.gov/cdo-web/webservices/v2#dataTypes
# Data Set: https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:US1COJF0072/detail
token = 'oBcoXnGGBRZqmVExtdaZjvPdwXYJEAWB'
url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?'
date = date.today()
year = str(date.year)
print(year)
station_id = 'GHCND:US1COJF0072'#'FGHCND:US1COJF0072' # Station in Denver, CO
location_id = 'CITY:US080001'
#initialize lists to store data
dates_temp = []
dates_prcp = []
temps = []
prcp = []

r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?locations=' + location_id + '&datasetid=GHCND&limit=1000&startdate=' + year + '-01-01&enddate=' + year + '-12-31', headers={'token':token})
print(r)

# load the api response as a json
# d = json.loads(r.text)
# print(d['results'])
# # get all items in the response which are average temperature readings
# avg_pre = [item for item in d['results'] if item['datatype']=='PRCP']
# datatype = []
# # get the date field from all average temperature readings
# dates_temp += [item['date'] for item in avg_pre]
#
# # get the actual average temperature from all average temperature readings
# temps += [item['value'] for item in avg_pre]
#
# # initialize dataframe
# df_pre = pd.DataFrame()
#
# # populate date and average temperature fields (cast string date to datetime and convert temperature from tenths of Celsius to Fahrenheit)
# df_pre['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_temp]
# df_pre['avg_temps'] = [float(v) for v in temps]
# #df_pre['latitude'] = 39.8826
# #df_pre['longitude'] = -105.1056
#
# print(df_pre)