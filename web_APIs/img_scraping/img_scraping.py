# pip install bs4
# pip install html5lib

from bs4 import BeautifulSoup as soup
import requests

url = "https://unsplash.com/s/photos/inspiration"

response = requests.get(url)
# print(response.content)
#html parser
data = soup(response.content,'html.parser')

article_element = data.findAll('div',{'class':'_1tO5-'})
# print(imgs)

article = article_element[0]

# print(article.img) # this only works for comman html tags only :)

# print(article.img.attrs) # will return all the attributes like class, id , src etc etc...
#  soup creates a dictionary of these attributes attrs and we can extract the image link.

# print(article.img.attrs['src'])
print(len(article_element))


# for i,article in enumerate(article_element):
#     with open(f'inspiration{i}.jpg', 'wb') as file:
#         img_url = article.img.attrs['src']
#         response = requests.get(img_url)

#         file.write(response.content)


url = f"https://unsplash.com/s/photos/inspiration"

response = requests.get(url)
# print(response.content)

data = soup(response.content,'html.parser')
page_element = data.findAll('div',{'class':'_1tO5-'})
print(page_element)
imgs = []
for i in page_element:
    img_url = i.img.attrs['src']
    imgs.append(img_url)

print(imgs)    