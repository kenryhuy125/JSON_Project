import json

in_file = open('US_fires_9_1.json','r')

out_file = open('readable_fires_data.json','w')

fires_data = json.load(in_file)

limit = 450

brights,lons,lats = [],[],[]

for fire in fires_data:
    bright = fire["brightness"]
    lon = fire["longitude"]
    lat = fire["latitude"]
    if bright > 450:
        brights.append(bright)
        lons.append(lon)
        lats.append(lat)
        

print("Brights")
print(brights)

print("Lons")
print(lons)

print("Lats")
print(lats)

import plotly

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        #'size':[1.2*bright for bright in brights],
        'color':brights,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Brightness'}
    },
}]

my_layout = Layout(title='US Fires - 9/1/2020 through 9/13/2020')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename ='US_fires.html')
