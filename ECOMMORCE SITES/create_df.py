import pandas as pd

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

