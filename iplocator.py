import geocoder
import folium

g = geocoder.ip("me")

my_address = g.latlng

#print(my_address)

my_map1 = folium.Map(location=my_address, zoom_start=12)

folium.CircleMarker(location=my_address, radius=50, popup="Target").add_to(my_map1)

folium.Marker(my_address, popup="Target").add_to(my_map1)

my_map1.save("my_map.html")