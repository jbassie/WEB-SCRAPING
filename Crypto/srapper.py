# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 19:53:17 2022

@author: hp
"""

import requests
from bs4 import BeautifulSoup
import regex as re
base_url = 'https://www.cryptonary.com/'


news_link = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
for x in range(1,5):
    r = requests.get(f'https://www.cryptonary.com/news/page/{x}/')
    soup  =BeautifulSoup(r.content, 'lxml')
    
    news_list= soup.find_all('h3', class_ = 'course-head')
    
    
    
    for item in news_list:
        for links in item.find_all('a', href = True):
            news_link.append(base_url + links['href'])
    
test_link = 'https://www.cryptonary.com/okx-to-expand-its-staff-by-30-aims-to-achieve-gender-balance/'

r = requests.get(test_link, headers = headers)
soup = BeautifulSoup(r.content, 'lxml')


Category  = soup.find('a' , rel = 'category').text
title = soup.find('h1').text.strip()
main_image = soup.find_all('div', class_="featured-image singlepostbgimg")
image = []
date_of_posting = soup.find('div', class_ = 'posttime').text.strip()
reading_time = soup.find('span', class_ = 'rt-time').text + " "+soup.find('span', class_ = 'rt-label rt-postfix').text
for img in main_image:
    s = img['style']
    m = re.findall(r"'(.*?)'", s, re.DOTALL)
    image.append(m)
bullet = soup.find('ul', class_ = 'bulletundertitle').text
body = soup.find('div', class_ ="single-post-text clearfix").text.strip()

dicti = {'category' : Category, 
        'titel': title,
        'main_image' : image,
        'date':date_of_posting,
        'reading_time': reading_time,
        'bullet': bullet,
        'body': body
        
        }
for i, k in dicti.items():
    print(i, ":", k )