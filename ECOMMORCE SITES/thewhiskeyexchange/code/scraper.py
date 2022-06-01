#mport the whiskey_web_scrapping class
from whiskey_web_scrapping import whiskey_web_scrapping

#create a scraper object
scraper = whiskey_web_scrapping()

#scrape Data
data = scraper.scrape_whisky(number_of_pages=5)

print(data.head())
