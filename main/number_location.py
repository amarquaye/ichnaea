
import phonenumbers
from my_number import number
from phonenumbers import geocoder

sanNumber = phonenumbers.parse(number)

your_location = geocoder.description_for_number(sanNumber, "en")

print(your_location)