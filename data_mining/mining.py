from dputils.scrape import Scraper, Tag
page = 1
query = 'laptops'
limit = 10
all_results = []
for i in range(1,limit+1):
    url = f'https://www.flipkart.com/search?q={query}&page={page}'
    print(url)
    # create a scraper object
    scr = Scraper(webpage_url=url)
    # content to extract
    t = Tag(cls='_4rR01T') # title
    p = Tag(cls='_30jeq3 _1_WHN1') # price
    l = Tag('a', cls='_1fQZEK', output='href') # link
    i = Tag('img', cls='_396cs4', output='src') # image
    # extract data
    results = scr.get_repeating_page_data(
        target=Tag(cls='_1YokD2 _3Mn1Gg'),
        items=Tag(cls='_1AtVbE col-12-12'),
        title = t, price = p, link = l, imgurl = i
    )
    print(results)
    page += 1
    if len(results) == 0:
        break
    all_results += results
    print('------------------------------------')

# save data to csv
import pandas as pd
df = pd.DataFrame(all_results)
df.to_csv('flipkart.csv', index=False)