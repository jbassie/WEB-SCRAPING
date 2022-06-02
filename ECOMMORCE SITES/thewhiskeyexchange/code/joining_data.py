import pandas as pd
import os

files = [file for file in os.listdir('C:/Users/hp/Documents/GitHub/WEB-SCRAPING/ECOMMORCE SITES/thewhiskeyexchange/scraped_data')]
all_data = pd.DataFrame()
for file in files:
    df = pd.read_csv('C:/Users/hp/Documents/GitHub/WEB-SCRAPING/ECOMMORCE SITES/thewhiskeyexchange/scraped_data/' + file)
    all_data = pd.concat([all_data, df])

all_data.to_csv('all_data.csv')