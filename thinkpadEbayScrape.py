# This script just scrapes ebay looking for t440s thinkpad within a certain price range
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bSoup
import re



def conn(my_url):
    # open connection and read from page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    pageSoup = bSoup(page_html, "html.parser")
    return pageSoup


priceLookup = input("Please enter the price you are willing to pay max: ")
print("You will be looking within $100-" + str(priceLookup) + " range")

my_url = 'https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xthinkpad+t440s.TRS0&_nkw=thinkpad+t440s&_sacat=0'

pageSoup = conn(my_url)

name = pageSoup.findAll("h3", {"class": "lvtitle"})

link = pageSoup.findAll("a", {"class": "vip"})

price = pageSoup.findAll("li", {"class": "lvprice prc"})


# print("number of items: " + str(len(price)))

i = 0
while i < len(price):
    printName = name[i].a.text.strip()
    printLink = link[i].get('href')
    printPrice = price[i].span.text.strip()
    slicePrice = int(re.search(r'\d+', printPrice).group())

    if slicePrice < int(priceLookup) and slicePrice > 100:
        print("name: " + printName)
        print("link: " + printLink)
        print("price: " + printPrice)
        print("_"*40 + "\n")

    i += 1
