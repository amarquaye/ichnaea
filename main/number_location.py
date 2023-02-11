
import phonenumbers
import folium
from my_number import number
from phonenumbers import geocoder

Key = "6c88f3edf15448a582a99183d722b39c"

sanNumber = phonenumbers.parse(number)

your_location = geocoder.description_for_number(sanNumber, "en")

print(your_location)

#get carrier information
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)
query = str(your_location)

results = geocoder.geocode(query)
#print(results)

lat = results[0]["geometry"]["lat"]

lng = results[0]["geometry"]["lng"]

print(lat, lng)

my_map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=your_location).add_to(my_map)

# Save map to html file
my_map.save("mylocation.html")