from bs4 import BeautifulSoup
import requests


def scrape_html(self, base_url, page):
    """
    Sending a get request to https://www.thewhiskyexchange.com/  and create a beautifulsoup object

    Args:
        base_url(strings)
        page(int) - which page to scrape.

    Returns:
        Soup(BeautifulSoup Object)
    
    """

    self.base_url = base_url
    self.page  = page

    url = base_url + str(page)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup
