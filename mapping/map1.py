import folium
import pandas as pd
data = pd.read_csv("volcanoes.txt")
def setColor(height):
    if height<1000:
        return 'green'
    elif height<3000:
        return 'orange'
    else:
        return 'red'

map= folium.Map(location=[38.58,-99.09],zoom_start=5,tiles="Stamen Terrain")

fgvolc=folium.FeatureGroup(name="volcanoes")
for lat,lon, el in zip(list(data.LAT),list(data.LON),list(data.ELEV)):
    fgvolc.add_child(folium.CircleMarker(location=[lat,lon],radius=8,popup=str(el)+" meters",fill_color=setColor(el),color='grey',fill_opacity=0.8))

fgpop=folium.FeatureGroup(name="Population")
fgpop.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgvolc)
map.add_child(fgpop)

map.add_child(folium.LayerControl())
map.save("Map.html")
