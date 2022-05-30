import numpy
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

class whiskey_web_scrapping():  
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
        products_info_content = soup.find_all('header', class_ ='product-main_header' )
        return products_info_content


    def get_page_price(self, soup):
        """
        Extract from soup all the html object of type div and of class product-main_data

        Args:
            soup(BeautifulSoup Object)

        
        Returns:
            Products_info_data(List of html objects)  - List of div objects that contain the price of the beverage


        """

        self.soup = soup

        products_info_price = soup.find_all('div', class_ = "product-card_data")
        return products_info_price

    def get_product_name(self, products_info_content):
        '''
        Extract name of product.

        Args:
            products_info_content(string) -  the div object of the class product-main.
        
        Returns
            product_name(List) - A list of names

        '''
        self.products_info_content = products_info_content

        product_name = []

        #iterate through each product in the webpage
        for product in range(len(products_info_content)):

            #Extract the first class P - Which holds the name of the beverage
            name_p = products_info_content[product].find_all('p')[0]

            #Extract the contents of the first paragraphs -  the name of the beverage
            alcohol_name = name_p.contents[0].strip

            #Append each name to the list
            product_name.append(alcohol_name)
        
        return product_name

    def get_product_alcohol_percent(self, products_info_content):
        '''
        Extract the alcohol percent of the product.

        Args:
            products_info_content(string) -  the div object of the class product-main.
        
        Returns
            product_name(List) - A list of alcohol percent

        '''

        self.products_info_content = products_info_content

        product_al_percent = []

        # iterate through each product in the webpage
        for product in range(len(products_info_content)):

            #Extract the second  P- Which holds the alcohol values
            al_p = products_info_content[product].find_all('p')[1]

            #Apply string manipulation to extract the alcohol percent
            alcohol_percent_str = al_p.contents[0].strip()
            start_location_percent = alcohol_percent_str.find('/')
            end_location_percent = alcohol_percent_str.find('%')
            alcohol_percent = alcohol_percent_str[start_location_percent + 2:end_location_percent]

            #Append each alcohol percent to the list
            product_al_percent.append(alcohol_percent)
        return product_al_percent

    def get_product_alcohol_amount(self, products_info_content):
        '''
        Extract alcohol_amount  of product.

        Args:
            products_info_content(string) -  the div object of the class product-main.
        
        Returns
            product_al_percent(List) - A list of alcohol amount

        '''
        self.products_info_content = products_info_content
        product_al_amount = []

        #iterate through each product in the webpage
        for product in range(len(products_info_content)):
            #Extract the second class P - Which holds the alcohol value
            al_p = products_info_content[product].find_all('p')[1]

            #Apply string manipulation to extract the alcohol amount
            alcohol_percent_str = products_info_content[product].find_all('p')[1]
            start_location_amount = 0
            end_location_amount = alcohol_percent_str.find('cl')
            alcohol_amount = alcohol_percent_str[start_location_amount :end_location_amount]

            #Append each alcohol amount to the lsit
            product_al_amount.append(alcohol_amount)

        return product_al_amount

    def get_product_price(self, products_info_price):
        '''
        Extract price of product.

        Args:
            products_info_content(string) -  the div object of the class product-main_data.
        
        Returns
            product_al_percent(List) - A list of prices

        '''
        self.products_info_price = products_info_price
        product_price = []

        #Iterate through each product in the webpage
        for product in range(len(products_info_price)):

                #Extract the price for each product
                alcohol_price = products_info_price[product].content[0].content[0].replace('£', '').strip()

                #Append each alcohol price to the list
                product_price.appednd(alcohol_price)
        return product_price 

    def create_df(self,names,alcohol_amount, alcohol_percent,price):
            """
            Create a dataframe that will hold the extracted data.

            Args
            name(List) -  A list of product name
            alcohol_amount (list) - A list of product alcohol amount
            alcohol_percent(list)  - A list of product alcohol percent
            price(list) - A list of product prices.

            returns
            original_df(dataframe)
            """

            self.names = names
            self.alcohol_amount = alcohol_amount
            self.alcohol_percent= alcohol_percent
            self.price = price

            # Create a DataFrame
            original_df = pd.DataFrame(names, columns = ['Product_name'])
            original_df['Alcohol_percent'] = alcohol_percent
            original_df["Alcohol_amount"] = alcohol_amount
            original_df["Alcohol_price"] = price

            return original_df