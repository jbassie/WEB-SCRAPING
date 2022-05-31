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
            data.to_csv(Link[start_location:end_location] + '.csv')
            df = df.append(data, ignore_index = True)
            
    return df