#import the whiskey_web_scrapping class

from whiskey_web_scrapping import whiskey_web_scrapping

#create a scrapper object
scraper = whiskey_web_scrapping()

#Generate a BeautifulSoup object
soup = scraper.scrape_html(base_url = 'https://www.thewhiskyexchange.com/search?q=single-malt-scotch-whisky', page = 1)

#collecting div objects from the first page
products_info_content = scraper.get_page_content(soup)
products_info_price = scraper.get_page_price(soup)

# Extracting from div objects the name, alcohol percent, alcohol_amount and price of each product
product_name = scraper.get_product_name(products_info_content)
products_al_percent = scraper.get_product_alcohol_percent(products_info_content)
products_al_amount = scraper.get_product_alcohol_amount(products_info_content)
product_price = scraper.get_product_price(products_info_price)

# Creatign a DataFrame from the first page
df = scraper.create_df(names = product_name,alcohol_amount = products_al_amount, alcohol_percent = products_al_percent,
                        price = product_price)

print(df.head())
