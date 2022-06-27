import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes_spider"

    def start_requests(self):
        urls = ['https://quotes.toscrape.com/page/1/',]

        # Generator Function

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        page_id = response.url.split("/")[-2]        
        filename = f"quotes-{page_id}s"
        for q in response.css("div.quote"):
            text = q.css('span.text::text').get()
            author = q.css('span.authod::text').get()
            tags = q.css('span.authod::text').getall()

            yield {
                'text':text,    
                'author':author,
                'tags':tags,
            }

        next_page  = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
            
        # with open(filename,'wb') as f:
        #     f.write((response.body))

        # self.log(f'Saved file {filename}')    















# scrapy shell "http://quotes.toscrape.com/page/1/"
# 2021-04-07 12:52:46 [scrapy.utils.log] INFO: Scrapy 2.5.0 started (bot: myproject)
# 2021-04-07 12:52:46 [scrapy.utils.log] INFO: Versions: lxml 4.6.3.0, libxml2 2.9.5, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 21.2.0, Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)], pyOpenSSL 20.0.1 (OpenSSL 1.1.1k  25 Mar 2021), cryptography 3.4.7, Platform Windows-10-10.0.19041-SP0
# 2021-04-07 12:52:46 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
# 2021-04-07 12:52:46 [scrapy.crawler] INFO: Overridden settings:
# {'BOT_NAME': 'myproject',
#  'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
#  'LOGSTATS_INTERVAL': 0,
#  'NEWSPIDER_MODULE': 'myproject.spiders',
#  'ROBOTSTXT_OBEY': True,
#  'SPIDER_MODULES': ['myproject.spiders']}
# 2021-04-07 12:52:46 [scrapy.extensions.telnet] INFO: Telnet Password: cf153ba16264715b
# 2021-04-07 12:52:46 [scrapy.middleware] INFO: Enabled extensions:
# ['scrapy.extensions.corestats.CoreStats',
#  'scrapy.extensions.telnet.TelnetConsole']
# 2021-04-07 12:52:46 [scrapy.middleware] INFO: Enabled downloader middlewares:
# ['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
#  'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
#  'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
#  'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
#  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
#  'scrapy.downloadermiddlewares.retry.RetryMiddleware',
#  'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
#  'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
#  'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
#  'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
#  'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
#  'scrapy.downloadermiddlewares.stats.DownloaderStats']
# 2021-04-07 12:52:46 [scrapy.middleware] INFO: Enabled spider middlewares:
# ['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
#  'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
#  'scrapy.spidermiddlewares.referer.RefererMiddleware',
#  'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
#  'scrapy.spidermiddlewares.depth.DepthMiddleware']
# 2021-04-07 12:52:46 [scrapy.middleware] INFO: Enabled item pipelines:
# []
# 2021-04-07 12:52:46 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6024
# 2021-04-07 12:52:46 [scrapy.core.engine] INFO: Spider opened
# 2021-04-07 12:52:47 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)      
# 2021-04-07 12:52:47 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
# 2021-04-07 12:52:47 [asyncio] DEBUG: Using proactor: IocpProactor
# [s] Available Scrapy objects:
# [s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
# [s]   crawler    <scrapy.crawler.Crawler object at 0x0000027914B01160>
# [s]   item       {}
# [s]   request    <GET http://quotes.toscrape.com/page/1/>
# [s]   response   <200 http://quotes.toscrape.com/page/1/>
# [s]   settings   <scrapy.settings.Settings object at 0x0000027914B01850>
# [s]   spider     <DefaultSpider 'default' at 0x27914fb31f0>
# [s] Useful shortcuts:
# [s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
# [s]   fetch(req)                  Fetch a scrapy.Request and update local objects
# [s]   shelp()           Shell help (print this help)
# [s]   view(response)    View response in a browser
# 2021-04-07 12:52:47 [asyncio] DEBUG: Using proactor: IocpProactor
# In [1]: response
# Out[1]: <200 http://quotes.toscrape.com/page/1/>

# In [2]: response.css('title')
# Out[2]: [<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

# In [3]: response.css('title').getAll()
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-3-b19e0f3a208e> in <module>
# ----> 1 response.css('title').getAll()

# AttributeError: 'SelectorList' object has no attribute 'getAll'

# In [4]: response.css('title').getall()
# Out[4]: ['<title>Quotes to Scrape</title>']

# In [5]: response.css('title::text').getall()
# Out[5]: ['Quotes to Scrape']

# In [6]: response.css('title::text').getall()[0]
# Out[6]: 'Quotes to Scrape'

# In [7]: response.css('title::text').getall()[0]
# Out[7]: 'Quotes to Scrape'

# In [8]: response.css('div.quote')
# Out[8]: 
# [<Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
#  <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
#  <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
#  <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
#  <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
#  <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
#  <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
#  <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
#  <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
#  <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>]

# In [9]: response.css('div.quote').get
# Out[9]: <bound method SelectorList.get of [<Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), 
# ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>]>

# In [10]: response.css("div.quote").get
# Out[10]: <bound method SelectorList.get of [<Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector 
# xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>, <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), 
# ' quote ')]" data='<div class="quote" itemscope itemtype...'>]>

# In [11]: response.css("div.quote").get()
# Out[11]: '<div class="quote" itemscope itemtype="http://schema.org/CreativeWork">\n        <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>\n    
#     <span>by <small class="author" itemprop="author">Albert Einstein</small>\n        <a href="/author/Albert-Einstein">(about)</a>\n        </span>\n        <div class="tags">\n            Tags:\n            <meta class="keywords" itemprop="keywords" content="change,deep-thoughts,thinking,world"> \n            \n            <a class="tag" href="/tag/change/page/1/">change</a>\n            \n            <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>\n            \n            <a class="tag" href="/tag/thinking/page/1/">thinking</a>\n            \n            <a class="tag" href="/tag/world/page/1/">world</a>\n            \n        </div>\n    </div>'

# In [12]: quote = response.css("div.quote").get()

# In [13]: title = response.css("div.quote").get()

# In [14]: quote = response.css("div.quote").get()

# In [15]: title = q2021-04-07 13:00:01 [parso.python.diff] DEBUG: diff parser start
# 2021-04-07 13:00:01 [parso.python.diff] DEBUG: line_lengths old: 1; new: 1
# 2021-04-07 13:00:01 [parso.python.diff] DEBUG: -> code[replace] old[1:1] new[1:1]
# 2021-04-07 13:00:01 [parso.python.diff] DEBUG: parse_part from 1 to 1 (to 0 in part parser)
# 2021-04-07 13:00:01 [parso.python.diff] DEBUG: diff parser end
# In [15]: title = quote.css("span.text").get()
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-15-04e3e3dae883> in <module>
# ----> 1 title = quote.css("span.text").get()

# AttributeError: 'str' object has no attribute 'css'

# In [16]: quote = response.css("div.quote").get()[0]

# In [17]: title = quote.css("span.text").get()
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-17-04e3e3dae883> in <module>
# ----> 1 title = quote.css("span.text").get()

# AttributeError: 'str' object has no attribute 'css'

# In [18]: quote = response.css("div.quote")[0]

# In [19]: title = quote.css("span.text").get()

# In [20]: print(title)
# <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without 
# changing our thinking.”</span>

# In [21]: print(type(quote))
# <class 'scrapy.selector.unified.Selector'>

# In [22]: title = quote.css("span.text::text").get()

# In [23]: print(title)
# “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”

# In [24]: author = quote.css('small.author::text).get()
#   File "<ipython-input-24-e8df9e1a68a4>", line 1
#     author = quote.css('small.author::text).get()
#                                                  ^
# SyntaxError: EOL while scanning string literal


# In [25]: author = quote.css('small.author::text').get()

# In [26]: print(aut2021-04-07 13:04:00 [parso.python.diff] DEBUG: diff parser start
# 2021-04-07 13:04:00 [parso.python.diff] DEBUG: line_lengths old: 1; new: 1
# 2021-04-07 13:04:00 [parso.python.diff] DEBUG: -> code[replace] old[1:1] new[1:1]
# 2021-04-07 13:04:00 [parso.python.diff] DEBUG: parse_part from 1 to 1 (to 0 in part parser)
# 2021-04-07 13:04:00 [parso.python.diff] DEBUG: diff parser end
# In [26]: author
# Out[26]: 'Albert Einstein'

# In [27]: author = quote.css('small.author::text').get()

# In [28]: print(author)
# Albert Einstein

# In [29]: tags = quote.css("a.tag::text").getall()

# In [30]: print(tags)
# ['change', 'deep-thoughts', 'thinking', 'world']

# In [31]: for i in response.css("div.quote"):
#     ...:     text = i.css('span.text::text').get()
#     ...:     print(text)
#     ...: 
# “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
# “It is our choices, Harry, that show what we truly are, far more than our abilities.”
# “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
# “The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
# “Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
# “Try not to become a man of success. Rather become a man of value.”
# “It is better to be hated for what you are than to be loved for what you are not.”
# “I have not failed. I've just found 10,000 ways that won't work.”
# “A woman is like a tea bag; you never know how strong it is until it's in hot water.”
# “A day without sunshine is like, you know, night.”

# In [32]: for i in response.css("div.quote"):
#     ...:     text = i.css('span.text::text')
#     ...:     print(text)
#     ...: 
# [<Selector xpath="descendant-or-self::span[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]/text()" data='“The world as we have created it is a...'>]
# [<Selector xpath="descendant-or-self::span[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]/text()" data='“It is our choices, Harry, that show ...'>]
# [<Selector xpath="descendant-or-self::span[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]/text()" data='“There are only two ways to live your...'>]
# [<Selector xpath="descendant-or-self::span[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]/text()" data='“The person, be it gentleman or lady,...'>]
# [<Selector xpath="descendant-or-self::span[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]/text()" data='“Imperfection is beauty, madness is g...'>]
# [<Selector xpath="descendant-or-self::span[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]/text()" data='“Try not to become a man of success. ...'>]
# [<Selector xpath="descendant-or-self::span[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]/text()" data='“It is better to be hated for what yo...'>]
# [<Selector xpath="descendant-or-self::span[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]/text()" data="“I have not failed. I've just found 1...">]
# [<Selector xpath="descendant-or-self::span[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]/text()" data='“A woman is like a tea bag; you never...'>]
# [<Selector xpath="descendant-or-self::span[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]/text()" data='“A day without sunshine is like, you ...'>]

# In [33]: for i in response.css("div.quote"):
#     ...:     text = i.css('span.text::text').getall()
#     ...:     print(text)
#     ...: 
# ['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”']
# ['“It is our choices, Harry, that show what we truly are, far more than our abilities.”']
# ['“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”']
# ['“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”']
# ["“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”"]
# ['“Try not to become a man of success. Rather become a man of value.”']
# ['“It is better to be hated for what you are than to be loved for what you are not.”']
# ["“I have not failed. I've just found 10,000 ways that won't work.”"]
# ["“A woman is like a tea bag; you never know how strong it is until it's in hot water.”"]
# ['“A day without sunshine is like, you know, night.”']

# In [34]: 

# In [34]: for i in response.css("div.quote"):
#     ...:     text = i.css('span.text::text').getall()[0]
#     ...:     print(text)
#     ...: 
# “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
# “It is our choices, Harry, that show what we truly are, far more than our abilities.”
# “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
# “The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
# “Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
# “Try not to become a man of success. Rather become a man of value.”
# “It is better to be hated for what you are than to be loved for what you are not.”
# “I have not failed. I've just found 10,000 ways that won't work.”
# “A woman is like a tea bag; you never know how strong it is until it's in hot water.”
# “A day without sunshine is like, you know, night.”

# In [35]: for i in response.css("div.quote"):
#     ...:     text = i.css('span.text::text').get()
#     ...:     print(text)
#     ...: 
# “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
# “It is our choices, Harry, that show what we truly are, far more than our abilities.”
# “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
# “The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
# “Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
# “Try not to become a man of success. Rather become a man of value.”
# “It is better to be hated for what you are than to be loved for what you are not.”
# “I have not failed. I've just found 10,000 ways that won't work.”
# “A woman is like a tea bag; you never know how strong it is until it's in hot water.”
# “A day without sunshine is like, you know, night.”
