# GOOGLE API
import requests

url = 'https://maps.google.com/maps/api/geocode/json?address=coding+blocks+pitampura'
# either we can make this strign on your own  

# or let reqquest library to do the work for us :)
url = 'https://maps.google.com/maps/api/geocode/json?'

params = {
    "address":"coding blcoks pitampura",

    }


r = requests.get(url,params=params)

print(r.url)

print(r.content.decode('UTF-8')) #bcz it is not free it reqires api key :/