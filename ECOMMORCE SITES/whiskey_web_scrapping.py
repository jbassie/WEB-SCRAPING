import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
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
        r = requests.get(url, headers=headers)
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
        products_info_content = soup.find_all('div', class_ ='product-card__content' )
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

        products_info_price = soup.find_all('div', class_ = "product-card__data")
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
            alcohol_name = name_p.contents[0].strip()

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
            alcohol_percent_str = al_p.contents[0].strip()
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
                alcohol_price = products_info_price[product].contents[0].contents[0].replace('£', '').strip()

                #Append each alcohol price to the list
                product_price.append(alcohol_price)
        return product_price 

    def create_df(self,names,alcohol_amount, alcohol_percent,price):
        """
        Create a dataframe that will hold the extracted data.

        Args
            name(List) -  A list of product name
            alcohol_amount (list) - A list of product alcohol amount
            alcohol_percent(list)  - A list of product alcohol percent
            price(list) - A list of product prices.

        Returns
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
    
    def insert_to_df(self, original_df, new_df):
        '''
        insert new data into an existing dataframe

        Args:
            original_df(DataFRame): DataFrame with Data from first page of a product
            new df(DataFraem)  DataFrame with data from other pages

        Returns:
            Original_df(DataFrame): DataFrame with data from original_df + new_df
        '''

        self.original_df = original_df
        self.new_df = new_df

        #Insert new data into the DataFrame of the first page
        original_df = original_df.append(new_df, ignore_index = True, verify_integrity = True)

        return original_df
    
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

    def scrape_whisky(self, url = 'https://www.thewhiskeyexchange.com' , number_of_pages = 5):
        '''
        1.  Combining all of the methods into a single place.
        2.  Extracting a default number of pages from every page that showcases a type of whiskey
        3.  Export each data of each whiskey type to a CSV file
        4.  Return a single DataFrame with all of the scrapped  whiskey data.

        Args:
            url(string) - The base url to extract data from.
                Default - https://www.thewhiskeyexchange.com

            number_of_pages(int) -The total number of pages to scrape.
            Default = 5
        
        Returns:
        df(DataFrame) - The entire data scraped throughout this project in a single DataFrame.
        '''

        self.url = url
        self.number_of_pages = number_of_pages

        df = pd.DataFrame()

        #creating a scraper object
        s = whiskey_web_scraping()

        #Generating the relevant links to scrape data from
        links = s.get_links()

        #Iterating through out each link
        for link in links:
            try:
                #for each page in each link, generate a DataFrame of whiskey related data
                for page in range(0, number_of_pages):
                    soup = s.crape_html(base_url = url + link +'?pg =' , page = page +1)
                
                content_html = s.get_page_content(soup)
                price_html = s.get_page(soup)

                names = s.get_product_name(content_html)
                alcohol_amount = s.get_product_alochol_amount(content_html)
                alcohol_percent  = s.get_product_alcohol_percent(content_html)
                price = s.get_product_price(price_html)

                #create a new dataframe for the frist page of eacg whiskey type
                if page == 0:
                    data = s.create_df(names, alcohol_amount, alcohol_percent, price)
                
                #insert to an existing DataFrame new data
                data = s.insert_to_df(data, s.create_df(names, alcohol_amount, alcohol_percent, price))
            except:
                print('Error with the link.{}'. format(link))
            # Export data for each whiskey type to s seperate csv file

            finally:
                start_location = link.rfind('/')+1
                end_location = len(link)
                data.to_csv(link[start_location:end_location] + '.csv')
                df = df.append(data, ignore_index = True)
                
        return df
