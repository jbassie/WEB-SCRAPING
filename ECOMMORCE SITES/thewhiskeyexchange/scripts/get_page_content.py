from bs4 import BeautifulSoup
from requests import requests

def get_page_content(self, soup):
    '''
    Extract from soup all the html object of type div and of class product_page

    Args:
        soup(Beautifulsoup)

    Returns:
        products_info_content(list of html objects) - list  div objects that contains the name of the beverage, alcohol amount
        and percent
    '''

    self.soup = soup
    products_info_content = soup.find_all('div', class_ ='product-card__content' )
    return products_info_content