from frame import Product


# On Construction
p = Product("pen",1,4)
    
    
x = p.get() 
p_url = "https://www.flipkart.com"
products = p_url+x[:,3]

print(products)

