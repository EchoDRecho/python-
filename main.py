import requests as rq
from bs4 import BeautifulSoup as bs


url = "https://uk.finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch"
cprice = 0
while True:

	page = rq.get(url)
	soup = bs(page.content, "html.parser")
	bsoup = soup.prettify()
	price = soup.find_all("span", class_="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)")
	rprice = price[0].get_text()
	if cprice != rprice[0]:
		print(price[0].get_text())
		cprice = rprice[0]
