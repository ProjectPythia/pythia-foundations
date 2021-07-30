import pandas as pd
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LongitudeFormatter, LatitudeFormatter
import matplotlib.pyplot as plt
from netCDF4 import Dataset

s1 = pd.read_csv('./images/2662924.csv', sep=',', infer_datetime_format=True, header=0,)
# print(s1)
sub = s1.drop(['STATION', 'ELEVATION', 'DAPR', 'MDPR', 'TAVG', 'WT01', 'WT03', 'WT04', 'WT05', 'WT06', 'WT11'], axis=1)
sub= sub[sub['DATE'] == '2013-09-12']
sub = sub.drop(['DATE'], axis=1)
sub = sub.dropna()
# print(sub)

new = sub.to_csv(path_or_buf='new_csv.csv', sep=',')
new = pd.read_csv('./new_csv.csv', sep=',', header=0, index_col=False )

df = new.to_xarray() # Pandas DF into xarray Dataset

df = df.set_index(lon='LONGITUDE', lat='LATITUDE', PRCP='PRCP')

print(df.drop_isel(index=[0,1]))
print(df)


# df = df.to_array() # xarray Dataset into DataArray


# # df = df.assign_coords(lon=sub.LONGITUDE, lat=sub.LATITUDE)
# df.dims(('LATITUDE', 'LONGTITUDE', 'PRCP'))

arr = xr.DataArray(
    data=df,
        # precipitation=(['x', 'y'], df['PRCP']),,
   coords={
       "lon": (["x", "y"], df[1]),
       "lat": (["x", "y"], df[0]),
    },
   dims = ['x', 'y'],
   )
# arr = arr.set_index(x=["LONGITUDE"], y=["LATITUDE"])
# print(arr)
# df.dims(['lon', 'lat'])
# df.assign(precipitation=df.PRCP)
# print(df.LONGITUDE.shape) #lat=1056 lon=1056
#
# This represents the data variables that you want to extract.
# toinclude = [0, 1, 3]
# new_file = 'daily_precp_data.nc'
# This will create a new data file with the variables and file name provided
# arr.to_netcdf(new_file)

# df = df.assign_coords(lon=df[0], lats=df[1])
# ds = xr.DataArray.to_netcdf(df)

# dat = Dataset('daily_precp_data.nc')
# dat = xr.open_dataarray('daily_precp_data.nc')
# print(dat)

# t = dat#.isel(PRCP=0)
# print(t.shape)

# fig = plt.figure(figsize=(6,8))
# proj = ccrs.PlateCarree()
# ax = plt.axes(projection=proj)

# pre = plt.contourf(
#                         df['lon'],
#                         dat['lat'],
#                         dat,
#                        transform=proj)
# plt.show()

