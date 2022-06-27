from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup

items = ['two seater sofa', 'bench','book cases','coffee table','dining set','queen beds','arm chairs','chest drawers','garden seating','bean bags','king beds']


url = []
drs = []
for query in items:
    query = query.replace(' ','')
    url = f'https://www.pepperfry.com/site_product/search?q={query}'

    response = Request(url)
    data = respoosne.read(response)
    my_data = soup(data,'html.parser')

    data_r = my_data.findAll('div',{'class':'pf-col xs-12 clipprods'})
    print(data_r)
    break

