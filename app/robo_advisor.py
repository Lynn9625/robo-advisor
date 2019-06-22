import os
import requests
import json
import csv
import time
import pygal


from urllib.parse import urlencode
from urllib.parse import unquote
from dotenv import load_dotenv

load_dotenv()

def to_usd(my_price):
   return "${0:,.2f}".format(my_price)

##1. INFO INPUT AND VALIDATION
while True:
    selected_symbol = input("Please input the stock symbol(s) that you are interested in:")
    if selected_symbol.isupper() == True and len(selected_symbol) == 4:
        break
    else:
        print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
        next    





