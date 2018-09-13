import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

fileName = "products.csv"
f = open(fileName, "w")

headers = "Brand, Product Name, Shipping\n"

f.write(headers)


#HTML Parsing
page_soup = soup(page_html, "html.parser")
	
#Grabs each product
containers = page_soup.findAll("div", {"class":"item-container"})

for container in containers:
	brand = container.div.div.a.img["title"]

	product_title = container.div.findAll("a", {"class":"item-title"})[0].text

	shipping = container.findAll("li", {"class":"price-ship"})[0].text.strip()

	print("brand: " + brand)
	print("product_title: " + product_title)
	print("shipping: " + shipping)

	f.write(brand + "," + product_title.replace(",", "|") + "," + shipping + "\n")

f.close()