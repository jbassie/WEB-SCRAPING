import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://www.jumia.com.ng/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
    

productlinks = []
    
for x in range(1,3):
    r = requests.get(f'https://www.jumia.com.ng/catalog/?q=shoes&page={x}#catalog-listing')
    soup = BeautifulSoup(r.content, 'html.parser')
    
    productlist = soup.find_all('div', class_ = "-paxs row _no-g _4cl-3cm-shs")
    
    
    for item in productlist:
        for link in item.find_all('a', href = True):
            productlinks.append(base_url + link['href'])
        

shoelist = []
#test_link = 'https://www.jumia.com.ng/fashion-2020-new-childrens-shoes-breathable-sport-sneakers-72160718.html'
for link in productlinks:
    r = requests.get(link, headers = headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    names = soup.find('h1', class_="-fs20 -pts -pbxs").text.strip()
    rating = soup.find('div', class_ = 'stars _s _al').text.strip()[:3]
    price = soup.find('span', class_ = '-b -ltr -tal -fs24').text.strip()[1:]
    reviews = soup.find('a', class_ ='-plxs _more').text.strip()[1:3]


    shoes = {
        'names': names,
        'rating': rating,
        'reviews': reviews,
        'price': price
        }
    shoelist.append(shoes)
    print('Saving:', shoes['names'])
    
df = pd.DataFrame(shoelist)
print(df.head(20))
df.to_csv('JUMIA2.csv', header=True, index=False)
