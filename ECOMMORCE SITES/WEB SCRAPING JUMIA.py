import requests
from bs4 import BeautifulSoup

base_url = 'https://www.jumia.com.ng/'

headers = [{
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }]
    

productlinks = []
    
for x in range(1,51):
    r = requests.get(f'https://www.jumia.com.ng/catalog/?q=shoes&page={x}#catalog-listing')
    soup = BeautifulSoup(r.content, 'lxml')
    
    productlist = soup.find_all('div', class_ = "-paxs row _no-g _4cl-3cm-shs")
    
    
    for item in productlist:
        for link in item.find_all('a', href = True):
            productlinks.append(base_url + link['href'])
        


test_link = 'https://www.jumia.com.ng/fashion-2020-new-childrens-shoes-breathable-sport-sneakers-72160718.html'

r = requests.get(test_link, headers = headers)
soup = BeautifulSoup(r.content, 'lxml')

names = soup.find('div', class_="-fs0-pls-prl")

    