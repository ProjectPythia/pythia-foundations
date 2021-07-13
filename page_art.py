###############################################################################
# Import packages

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cartopy.crs as ccrs

from wrf import (getvar, latlon_coords)

###############################################################################
# Read in the data, file path will need to be updated
wrfin = Dataset("/Users/misi1684/pythia-foundations/images/wrfout_d01_2005-08-28_00_00_00")

# Extract sea level pressure and 2m dewpoint temp
slp = getvar(wrfin, 'slp')
td2 = getvar(wrfin, 'td2', units='degF')

###############################################################################
# Plot the data

# Get the latitude and longitude coordinate.
lats, lons = latlon_coords(slp)

# Generate figure (set its size (width, height) in inches)
fig = plt.figure(figsize=(10, 8))

# # Generate axes using Cartopy
ax = plt.axes(projection=ccrs.Mercator(central_longitude=-75))
ax.set_extent([-125, -60, 0, 43],)


# ax.set_global()
# ax.coastlines('50m', linewidth=0.8,zorder=11, edgecolor='black')

# Manually set contour levels
slp_levels = np.arange(980, 1013, 3)
td2_levels = np.arange(70, 85, 0.5)

# Add filled contours
# Add the 850 hPa geopotential height contour lines
levels = np.arange(0, 12., 1)
contours = plt.contour(lons,
                       lats,
                       slp,
                       levels=slp_levels,
                       colors="white",
                       zorder=11,
                       transform=ccrs.PlateCarree())

plt.clabel(contours, inline=1, fontsize=10, fmt="%i")

# Add the wind speed filled contours
levels = [52, 54, 60, 64, 70, 76, 80, 88]

wspd_contours = plt.contourf(lons,
                             lats,
                             td2,
                             levels=td2_levels,
                             cmap="magma",
                             zorder=10,
                             transform=ccrs.PlateCarree())
###############################################################################
# Plot image
img = mpimg.imread('/Users/misi1684/pythia-foundations/images/pretty-earth.png')
ax.imshow(img, transform=ccrs.PlateCarree(central_longitude=-75))
plt.tight_layout()
plt.show()