'''

=> Data Acquistion - Web API's
    . Applicatin Progaramming Interface - Set of routines over web server.
    . Connects Application and Database
    . Specify Data with URL
    . Retrive Data and parse
    . Api may return data in JSON,XML data dormat

=> JSON
    . JavaScript Object Notation
    . Dictionary Like Data-structure : key value pairs
    . Keys are strings, values can be anything.
    . Easy to read and write

=> XML
    . eXtensible Markup Language
    . Structure similar to XML
    . Custom Tags
    . No Style  

=> Type of Requests
    .GET 
    .POST
    .DELETE
    .PUT
    PATCH

Intead of requesting request through browser we are goinf to request it by our python script
 - To do this we have some libraries
    .Urllib (traditonal)
    .Requests(most popular python library and works we with python 3>>> pip install requests)

'''    

from urllib.request import urlopen

url = "https://samples.openweathermap.org/data/2.5/weather?q=India,uk&appid=b6907d289e10d714a6e88b30761fae22"
data = urlopen(url) #get requests
data = data.read()  
# print(data)

import json

json_data = json.loads(data) # convert data into json format
# print(json_data)
# print(type(json_data))
print(json_data['base'])

json_string = json.dumps(json_data)
# print(json_string)
print(type(json_string))





