import geocoder
import folium

g = geocoder.ip("me")

my_address = g.latlng

print(my_address)