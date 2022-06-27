# Data scraping using Beautiful Soup
    #import beautiful soup
    #Make a get request to fetch Page Data
    #Parse Html
    #filter relavent parts

# INSTALLATION
# -pip install bs4      

from urllib.request import urlopen

android_url = "https://en.wikipedia.org/wiki/Android_version_history"

android_data = urlopen(android_url) 

print(android_data) # get request


android_html = android_data.read()
# print(android_html)

# android_data.close()

#Parsing Data

from bs4 import BeautifulSoup as soup

android_soup = soup(android_html,'html.parser')
# print(android_soup)

print(type(android_soup)) # it is a type of a soup object



### EXTARACTIONG OUT BUSINESS INFORMATION

print(android_soup.h1) # return first heading

print(android_soup.findAll('h1',{})) # to find all

tables = android_soup.findAll('table',{'class':'wikitable'})
print(len(tables))
android_table = tables[0]



###EXTARCTING USEFUL INFORMATION
    # Remove underired tags
    # Extract table header and data

# exxtracting table headers
headers = android_table.findAll('th') #The findAll method returns a list of bs4 Tag elements
print(len(headers))
column_titles = [ct.text[:-1] for ct in headers]
print(column_titles)

#extracting table rows

# rows = 
row_data = android_table.findAll('tr')[1:]
print(len(row_data))
first_row = row_data[0].findAll('td',{})
for d in first_row:
    print(d.text)


table_row = []

for row in row_data:
    current_row = []
    row_data = row.findAll('td',{})
    # print(row_data)
    for data in row_data:
        current_row.append(data.text[:-1])
        
    table_row.append(current_row)    
print(table_row)    

# print(table_row)

# WRITING AND READING CSV FILES
 # CSV Stands for Comma Seperated File'

filename = 'android_version.csv'

with open(filename, 'w', encoding='utf-8') as f:
    # write the header
    header_string = ','.join(column_titles) # will return commaserperated string > seperate every element of list with comma and return string of those same element.
    # print(header_string)
    header_string += '\n'
    f.write(header_string)

    for row in table_row:
        row_string = ""
        for w in row:
            w = w.replace(',','')
            row_string += w + ','
            
        row_string +="\n"
        f.write(row_string)

import pandas as pd

df = pd.read_csv('android_version.csv')
m = df.head(n=10)
print(m)

## how to scarp data locally

# with open('android.html',encoding='utf-8') as f:
#     page_soup = soup(f,'html.parser')

# tg = page_soup.find_all('h1')
# print(tg)