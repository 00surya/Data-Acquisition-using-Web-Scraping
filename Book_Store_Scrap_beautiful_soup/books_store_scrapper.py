from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


def scrap(url):
    
    reaponse = urlopen(url)
    data =  reaponse.read()
    f_data = soup(data, 'html.parser')
    f_obj = f_data.findAll('li',{'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})

    for i in f_obj:

        img_lk = i.img.attrs['src']
        img_lk = img_lk.replace(',',' ')
        title = i.h3.a.text
        title = title.replace(',',' ')
        price = i.findAll('div',{'class':'product_price'})[0].p.text
        x = [img_lk,title,price]
        bk_data.append(x)
    if len(bk_data)<1000:
        next = f_data.findAll('li',{'class':'next'})
        n = next[0].a.attrs['href']
        ul = f"http://books.toscrape.com/catalogue/{n}"
        print(ul)
        scrap(ul)


bk_data = []
url = 'http://books.toscrape.com/catalogue/page-1.html'
scrap(url)

hdrs = ['image_url','book_title','product_price'] 

file_name = 'books_data.csv'


with open(file_name, 'w',encoding='utf-8') as f:
    hdr_str = ','.join(hdrs)
    hdr_str+='\n'
    f.write(hdr_str)
    for row in bk_data:
        row_str = ','.join(row)
        row_str+='\n'
        f.write(row_str)

