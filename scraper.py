from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

url = 'https://www.newegg.ca/p/pl?PageSize=96&N=100007708%204018%204017'

# Opening up connection and grabbing the page
client = urlopen(url)
page_html = client.read()
client.close()

# HTML parsing
page_soup = soup(page_html, "html.parser")

# Grabs each product
containers = page_soup.findAll("div", {"class":"item-container"})

# Open a csv file
filename = "output.csv"
f = open(filename, "w")

# Write in the headers
header = "brand,product_name,price\n"
f.write(header)

# Iterate through each product and scrape details
for container in containers:
	# Get the brand of the product
	try:
		brand_container = container.findAll("a", {"class":"item-brand"})
		brand = brand_container[0].img["title"]
	except:
		pass

	# Get the name of the product
	try:
		product_name = container.a.img["title"]
	except:
		pass

	# Get the price of the product
	try:
		price_container = container.findAll("li", {"class":"price-current"})
		price = price_container[0].strong.text
	except:
		pass

	# Print for debugging
	print("brand: " + brand)
	print("product_name: " + product_name)
	print("price: " + price)

	# Write each product to the csv file
	f.write(brand + "," + product_name.replace(",", "|") + "," + price + "\n")

# Close the csv file
f.close()
