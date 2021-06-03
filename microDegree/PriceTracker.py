import requests
from bs4 import BeautifulSoup

import pandas as pd
import csv

df = pd.read_csv('product_to_track.csv')

def give_product_price(URL):
    headers = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content,'html.parser')

    #Amazon_Tracker
    product_price = soup.find(id='priceblock_dealprice')

    if(product_price==None):
        product_price = soup.find(id='priceblock_ourprice')
    return product_price.getText()

price_list= []
for every_product in df['URL']:
    # print(every_product)
    product_price_returned = give_product_price(every_product)
    # print(product_price_returned)
    my_product_price = product_price_returned[2:]
    my_product_price = my_product_price.replace(',','')
    my_product_price = int(float(my_product_price))
    price_list.append(my_product_price)
    # print(my_product_price)
print(price_list)


df['available_price'] = price_list
df.to_csv('product_to_track.csv', index=False)


#Flipkart_tracker
# price3 = soup.find("div", {"class": "_1vC4OE _3qQ9m1"})
# print (price3)
# print(price3.string)


#Snapdeal_Tracker
# price3 = soup.find("span", {"class": "payBlkBig"})
# print(price3)
# print(price3.string)
