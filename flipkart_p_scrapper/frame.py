from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import numpy as np
import pandas as pd


class Product:
    
    def __init__(self,p_name,no_pages=4,r_v=2000):
        
        self.p_name = p_name
        self.n = no_pages
        self.url = f'https://www.flipkart.com/search?q={self.p_name}&page=1'
        self.d = {'imgs':[],'ratings':[],'ratings_volume':[],'product_urls':[],'price_l':[]}
        self.cnt = 0
        self.r_v = r_v
        
    def get(self):
        
        response = urlopen(self.url)
        data = response.read()
        

        s_data = soup(data,'html.parser')

        s_obj = s_data.findAll('div',{'class':'_13oc-S'})


        target = s_obj[0]
        target_class = target.find_all("div")
        class_name = target_class[1]['class'][0]
        
        
        s_obj = s_data.findAll('div',{'class':f'{class_name}'})
        if len(s_obj)==0:
            return "Nothing Found :/"

        for i in s_obj:
            
            if i.findAll('div',{'class' : '_3LWZlK'}):
                for hit in i.findAll('div',{'class' : '_3LWZlK'}):    
                    hi = hit.text.strip()    
                    self.d['ratings'].append(hi)
                    
            else:
                self.d['ratings'].append("0")
            
            p_url = i.a.attrs['href']
            img_lk = i.img.attrs['src']
            price = i.findAll('div',{'class':'_30jeq3'})[0].text
            
            try:
                rating_v = i.findAll('span',{'class':'_2_R_DZ'})[0].text
                rating_v = rating_v[1:-2]
            except:
                rating_v = "0" 
        
            self.d['price_l'].append(price[1:])   
            self.d['imgs'].append(img_lk)
            self.d['ratings_volume'].append(rating_v)
            self.d['product_urls'].append(p_url)
        
        if self.cnt==0:
            self.cnt = len(self.d['imgs'])

        if int(len(self.d['imgs'])) <= self.cnt*self.n-1: 
            l = len(self.d['imgs'])
            self.url = f'https://www.flipkart.com/search?q={self.p_name}&page={(l//self.cnt)+1}'
            self.get()

        data = self.prep_data()    
        return data

    def prep_data(self):

        df = pd.DataFrame(self.d)
        df['price_l'] = df['price_l'].replace(',','', regex=True)
        df['ratings_volume'] = df['ratings_volume'].replace(',','',regex=True)
        df.sort_values("ratings",axis=0,ascending = False,inplace=True)
        df.reset_index(drop=True, inplace=True)
        df['ratings'] = pd.to_numeric(df['ratings'])
        # df['ratings_volume'] = pd.to_numeric(df['ratings_volume'])
        print(df['ratings_volume'])

        m = df[df['ratings_volume']>self.r_v].sort_values("ratings",ascending=False)
        m = m.values
        
        return m