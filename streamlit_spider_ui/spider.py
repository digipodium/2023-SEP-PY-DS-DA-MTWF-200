from dputils.scrape import Scraper, Tag

def execute_spider(start, limit=10):
    page = start
    all_results = []
    for i in range(start,limit+1):
        if page == 1:
            url = f'https://www.zyte.com/blog/'
        else:
            url = f'https://www.zyte.com/blog/page/{page}/'
        scr = Scraper(webpage_url=url)
        target = Tag('main')
        items = Tag(cls='CardResource_card__BhCok card')
        title = Tag(cls='z-text-blog-title')
        content = Tag(cls='CardResource_info__g1t2c', output='object')
        link = Tag('a',cls='default btn-text btn-link gtm-linkclick Button_btn__WcYUU btn', output='href')
        results = scr.get_repeating_page_data(
            target=target, items=items,
            title=title, content =content, link=link,
            errors=True,
        )
        if len(results) == 0:
            print(f'No more results on page {page}')
            break
        all_results.extend(results)
        page += 1
    return all_results

if __name__ == '__main__':
    out = execute_spider(1, 1)
    print(out[-1]['content'].find_all('span'))