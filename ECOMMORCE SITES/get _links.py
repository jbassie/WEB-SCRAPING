from urllib.request import urlretrieve
from bs4 import BeautifulSoup

from requests import request
import requests


def get_links(self, url = 'https://www.thewhiskeyexchange.com/'):
    """
    Generate a lsit of links that showcase whiskey beverages.

    Args:
        url(string) - The URL of the main page
        Default = https://www.thewhiskeyexcahnge.com/

    Returns:
        relevant_links(List) - A list of only the links that showcase a type of whiskey
    """

    self.url = url

    # Generate a Beautiful soup object called soup
    url = url
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    #collect all the html objects of type 'a'
    a_tags = soup.find_all('a', class_ = 'subnav__link')

    links_list = []

    #collect all the hyper links of the webpage
    for link in a_tags:
        links_list.append(link.get('href'))
    
    relevant_links = []

    #iterate through the links and filter only the relevant ones that showcase a type of whiskey
    for link in links_list:
        if link is not None and '/c/' in link and 'whisky' in link and '?' not in link:
            relevant_links.append(link)
    
    return relevant_links