from math import prod


def get_page_price(self, soup):
    """
    Extract from soup all the html object of type div and of class product-main_data

    Args:
        soup(BeautifulSoup Object)

    
    Returns:
        Products_info_data(List of html objects)  - List of div objects that contain the price of the beverage


    """

    self.soup = soup

    products_info_price = soup.find_all('div', class_ = "product-action__row")
    return products_info_price