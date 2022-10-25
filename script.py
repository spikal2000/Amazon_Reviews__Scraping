# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:18:29 2022

@author: spika
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup


def getAmazonSearch(query):
    amazon_url = "https://www.amazon.com/s?k="+ query
    page = requests.get(amazon_url, headers = header)
    return page


#Get context of individual product pages with data-asin 
def findAsin(asin):
    url = "https://www.amazon.com/dp/" + asin
    page = requests.get(url, cookies = cookie, headers = header)
    return page

#to see all Reviews link and extract content
def searchReviews(reviewLink):
    url = "https://www.amazon.com" + reviewLink
    page = requests.get(url, cookies = cookie, headers = header)
    return page

# building the URL:
#amazon_url = "https://www.amazon.com/s?k="

query = "graphics+cards"

#url = amazon_url + query

#Without the header amazon will not give me access
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 ',
          'referer': 'https://www.amazon.com/s?k=graphics+cards&ref=nb_sb_noss'}
page = getAmazonSearch(query)
cookie = page.cookies
#page.text
#page.cookies




soup = BeautifulSoup(page.content)
#Extract the product names
product_names = []
for i in soup.findAll("span", {'class': 'a-size-medium a-color-base a-text-normal'}):
    product_names.append(i.text)

#extract the asin numbers 
asins = []
for i in soup.findAll("div", {'class': 's-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'}):
    asins.append(i['data-asin'])


