# TODO: Implement most common words in name
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


maxPrice = input("Please enter the price you are willing to pay max: ")
print("You will be looking within $100-" + str(maxPrice) + " range")

my_url1 = 'https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xthinkpad+t440s.TRS0&_nkw=thinkpad+t440s&_sacat=0'

pageSoup = conn(my_url1)

name = pageSoup.findAll("h3", {"class": "lvtitle"})

link = pageSoup.findAll("a", {"class": "vip"})

price = pageSoup.findAll("li", {"class": "lvprice prc"})


# print("number of items: " + str(totalItems))

i = 0
totalPrice = 0
includedPrice = 0
included = 0

totalItems = len(price)

while i < totalItems:
    printName = name[i].a.text.strip()
    printLink = link[i].get('href')
    printPrice = price[i].span.text.replace(" ", "")
    slicePrice = float(re.search(r'\d+\.+\d+\d', printPrice).group())
    totalPrice += slicePrice

    if slicePrice < float(maxPrice) and slicePrice > 100:
        print("name: " + printName)
        print("link: " + printLink)
        print("price: " + printPrice)
        print("_" * 40 + "\n")
        included += 1
        includedPrice += slicePrice

    i += 1

avgPrice = totalPrice / totalItems
includedPrice = includedPrice / included

print("The average price of all " + str(totalItems) + " Thinkpads is: $" + str(avgPrice))

print("The average price of the listed " + str(included) + " Thinkpads is: $" + str(includedPrice))
