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
def searchAsin(asin):
    url = "https://www.amazon.com/dp/" + asin
    page = requests.get(url, headers = header)
    return page

#Extract the product names
def getProductNames(asin):
    url = "https://www.amazon.com/dp/" + asin
    page = requests.get(url, headers = header)
    soup = BeautifulSoup(page.content, "lxml")
    
    for i in soup.findAll("span", {'class': 'a-size-large product-title-word-break'}):
        product_name = i.text
    return product_name

#to see all Reviews link and extract content
def searchReviews(reviewLink):
    url = "https://www.amazon.com" + reviewLink
    page = requests.get(url, headers = header)
    return page


#query = "graphics+cards"
query = "ps5"
#url = amazon_url + query

#Without the header amazon will not give me access
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.91 Safari/537.36 ',
          'referer': 'https://www.amazon.com/s?k=ps5&crid=MFZYID64FVKA&sprefix=ps%2Caps%2C605&ref=nb_sb_noss_1'}

#https://www.amazon.com/s?k=graphics+cards&ref=nb_sb_noss
page = getAmazonSearch(query)
soup = BeautifulSoup(page.content, "lxml")




#extract the asin numbers 
asins = []
for i in soup.findAll("div", {'class': 's-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'}):
    asins.append(i['data-asin'])
    

#call the getProductNames and store the names in a list
product_names = []
for i in range(0, len(asins)):
    product_names.append(getProductNames(asins[i]))
    
links = []
for i in range(len(asins)):
    page = searchAsin(asins[i])
    soup = BeautifulSoup(page.content, "lxml")
    for j in soup.findAll("a", {'data-hook': "see-all-reviews-link-foot"}):
        links.append(j['href'])
        


reviews = []
for i in range(len(links)):
    for j in range(2):
        page = searchReviews(links[i] + '&pageNumber=' + str(j))
        soup = BeautifulSoup(page.content, "lxml")
        for k in soup.findAll("span", {'data-hook' : 'review-body'}):
            reviews.append(k.text)















