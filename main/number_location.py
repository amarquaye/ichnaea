
import phonenumbers
from my_number import number
from phonenumbers import geocoder

sanNumber = phonenumbers.parse(number)

your_location = geocoder.description_for_number(sanNumber, "en")

print(your_location)

#get carrier information
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))