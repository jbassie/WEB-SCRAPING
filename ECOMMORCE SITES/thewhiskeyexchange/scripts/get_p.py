from math import prod
from numpy import product


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