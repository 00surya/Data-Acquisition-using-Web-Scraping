import scrapy


class books(scrapy.Spider):
    name = "books"
    lst = []
    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/page-1.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes.csv' 
        
        # For Creating JSON        
        
        for q in response.css("article.product_pod"):
            img = q.css("img.thumbnail::attr(src)").get()
            name = q.css("h3 a::attr(title)").get()
            price = q.css("p.price_color::text").get()

            img = str(img).replace(',','')
            name = str(name).replace(',','')
            body = [img,name,price]
            self.lst.append(body)
        

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
                
        with open('books.csv', 'w+', encoding='utf-8') as f:
            for i in self.lst:
                print(i)
                body_str = ','.join(i)

                body_str+="\n"
                f.write(body_str)
                