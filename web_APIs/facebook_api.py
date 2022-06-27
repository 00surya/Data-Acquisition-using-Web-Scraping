# pip install requests
import requests 

url = "http://graph.facebook.com/7/picture?type=large"

r = requests.get(url)
print(r.content) #binary encoding

with open("sample)pic.jpg", 'wb') as f:
    f.write(r.content)