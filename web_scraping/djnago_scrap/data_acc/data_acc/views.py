from django.shortcuts import HttpResponse
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

def webscrap(request):
    poem_url = "https://www.poemhunter.com/poems/"
    poem_data = urlopen(poem_url)
    poem_html = poem_data.read()
    poem_soup = soup(poem_html,'html.parser')
    poem = poem_soup.findAll('div',{'class':'phRow phBoxStyle moderate-pink'})
    print(poem[0])
    return HttpResponse(poem[0])