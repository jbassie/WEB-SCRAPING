import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import etree

base_url = 'https://finance.yahoo.com/quote/MMM'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
    


#<td class="Ta(end) Fw(600) Lh(14px)" data-test="PREV_CLOSE-value">112.30</td>

r = requests.get(base_url)
soup = BeautifulSoup(r.content, 'html.parser')



ask_price = soup.find("td", { "data-test" : "ASK-value" }).text.strip()[0:6]
bid_ = soup.find("td", { "data-test" : "BID-value" }).text.strip()[0:6]
dividend = soup.find("td", { "data-test" : "DIVIDEND_AND_YIELD-value" }).text.strip()[0:4]

print(bid_)
print(ask_price)
print (dividend)

