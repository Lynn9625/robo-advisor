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



##3. INFO OUTPUT 
#print(parsed_response.keys())
request_time = time.strftime("%Y-%m-%d %H:%M %p", time.localtime())

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

time = parsed_response["Time Series (Daily)"]
dates = list(time.keys())

latest_day = dates[0]
latest_close = time[latest_day]["4. close"]

high_prices = []
for date in dates:
    high_price = time[date]["2. high"]
    high_prices.append(float(high_price))
recent_high =  max(high_prices)

low_prices = []
for date in dates:
    low_price = time[date]["3. low"]
    low_prices.append(float(low_price))
recent_low =  min(low_prices)

yes = "BUY!"
reason_yes = "Close price was higher than open price more than 60 per cent of the time in the approximately past 100 available days"
no = "DON'T BUY!"
reason_no = "Close price was lower than open price more than 40 per cent of the time in the approximately past 100 available days"

a = 0
for date in dates:
    open_price = time[date]["1. open"]
    close_price = time[date]["4. close"]
    if close_price > open_price:
        a = a+1

if a > len(dates)*0.6:
    rocommendation = yes
    reason = reason_yes
else:
    rocommendation = no
    reason = reason_no

print("-------------------------")
print("SELECTED SYMBOL:",selected_symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:",request_time)
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print(f"RECOMMENDATION: {rocommendation}")
print(f"RECOMMENDATION REASON: {reason}")
print("-------------------------")
print("WRITING DATA TO CSV...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")



##4. WRITE CSV FILE
csv_file_path = os.path.join(os.path.dirname(__file__),"..","Data","prices.csv")
with open(csv_file_path,"w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames = ["timestamp","open", "high","low","close","volume"])
    writer.writeheader()
    for date in dates:
        daily_prices = time[date]
        writer.writerow({
            "timestamp":date,
            "open":daily_prices["1. open"],
            "high":daily_prices["2. high"],
            "low":daily_prices["3. low"],
            "close":daily_prices["4. close"],
            "volume":daily_prices["5. volume"]
        })

