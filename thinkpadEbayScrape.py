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


def scrapeTheWeb(my_url, maxPrice):

    print("You will be looking within $100-" + str(maxPrice) + " range")
    pageSoup = conn(my_url)
    name = pageSoup.findAll("h3", {"class": "lvtitle"})
    price = pageSoup.findAll("li", {"class": "lvprice prc"})

    i = 0
    totalPrice = 0
    includedPrice = 0
    included = 0
    totalItems = len(price)

    while i < totalItems:
        printName = name[i].a.text.strip()
        printLink = name[i].a.get('href')
        printPrice = price[i].span.text.replace(" ", "").replace(",", "")
        slicePrice = float(re.search(r'\d+\.+\d+\d', printPrice).group())
        totalPrice += slicePrice

        if slicePrice < float(maxPrice) and slicePrice > 100:
            print("name: " + printName)
            print("link: " + printLink)
            print("price: " + printPrice)
            print("_" * 40 + "\n")
            print(slicePrice)
            included += 1
            includedPrice += slicePrice

        i += 1

    avgPrice = totalPrice / totalItems
    includedPrice = includedPrice / included

    print("The average price of all " + str(totalItems) + " Thinkpads is: $" + str(avgPrice))

    print("The average price of the listed " + str(included) + " Thinkpads is: $" + str(includedPrice))

# --- Code goes here ---


maxPrice = input("Please enter the price you are willing to pay max: ")

my_url1 = 'https://www.ebay.ca/sch/i.html?_from=R40&_sacat=0&_nkw=thinkpad+t440s&_ipg=200&rt=nc'

scrapeTheWeb(my_url1, maxPrice)
