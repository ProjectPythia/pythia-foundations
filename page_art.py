###############################################################################
# Import packages

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cartopy.crs as ccrs
import cartopy.feature as cfeature

###############################################################################
# Read in the data, file path will need to be updated

ds = xr.open_dataset("daymet_v3_prcp_2013_na_subset.nc", engine="netcdf4")
prcp = ds.prcp

# Create figure for plotting, adding land and state features
fig = plt.figure(figsize=(15, 15), frameon=False)
proj = ccrs.PlateCarree()
ax = plt.axes(projection=proj)
ax.axis('off')
ax.coastlines()
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.STATES)

# Create function to loop over precip data and plot each day
anim_artists = [] # Generate empty list to place plots in

for prcp_slice in prcp:
    cntr = ax.contourf(prcp_slice.lon,
                       prcp_slice.lat,
                       prcp_slice,
                       transform=proj,
                       levels=np.arange(0,55,2))
    anim_artists.append(cntr.collections)

plt.tight_layout()

# Call Matplotlib animation function to create gif
anim = animation.ArtistAnimation(fig, anim_artists, interval=500)

# Uncomment to save gif
# anim.save('boulder_prcp.gif', writer="pillow")



