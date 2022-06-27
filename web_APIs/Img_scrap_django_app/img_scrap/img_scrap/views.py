from bs4 import BeautifulSoup as soup
import requests
from django.shortcuts import HttpResponse,render
from urllib.request import urlopen


def home(request):
    return render(request, 'home.html')    
    
def response(request):
    if request.method=="GET":
        try:
            query = request.GET.get('query','')
            print(query)
            url = f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

            response = urlopen(url)
            print(response)
            r_data = response.read()
            data = soup(r_data,'html.parser')

            page_element = data.findAll('div',{'class':'z'})
            print(page_element[0].img.attrs['src'])
            # print(page_element)
            imgs = []
            for i in page_element:
                img_url = i.img.attrs['src']
             
                imgs.append(img_url)
            print(imgs)    
            check = "http"
            checkv = ""
            m = 0
            for i in imgs[0]:
                checkv+=i
                if m>2:
                    break
                m+=1    
            if check!=checkv:
                imgs = []
                res = f"Your search - {query} - mar gya."
                context = {'results':imgs,'res':res}
            else:    
                context = {'results':imgs}
            return render(request,'home.html',context)    
        except:
            return HttpResponse("Network error....")    