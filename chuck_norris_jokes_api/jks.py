from urllib.request import urlopen

from bs4 import BeautifulSoup
import json
url = f"http://api.icndb.com/jokes/15"

response = urlopen(url)

data = response.read()

json_data = json.loads(data)

joke = json_data['value']['joke']
id = json_data['value']['id']
sv = [str(id),joke]
sv = ','.join(sv)
filename = 'joke.csv'

with open(filename, 'w') as f:
    f.write(str(sv))