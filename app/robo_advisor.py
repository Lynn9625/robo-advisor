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



##2. MAKE AND PARSE REQUEST
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
url = "https://www.alphavantage.co/query"
parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": selected_symbol,
    "apikey": api_key,
    "datatype": "json"
}
trans_parameter = urlencode(parameter)
request_url = unquote(url + "?" + trans_parameter)
response = requests.get(request_url)
parsed_response = json.loads(response.text)


