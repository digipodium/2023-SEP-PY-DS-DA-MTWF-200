import streamlit as st
from orm import Product, create_engine
from sqlalchemy.orm import sessionmaker
from spider import execute_spider

def open_db():
    engine = create_engine('sqlite:///spider.db')
    Session = sessionmaker(bind=engine)
    return  Session()

def save_data(data):
    db = open_db()
    item = Product(
        title =data['title'],
    )
    db.add(item)
    db.commit()

st.title("Article Scraper")

start = st.number_input("Start Page", value=1,
                        help="if you want to start from another page")
limit = st.number_input("Limit", value=10, 
                        help="how many pages to scrape, -1 for all")
if st.button("Scrape data"):
    db = open_db()
    with st.spinner("Scraping data..."):
        result = execute_spider(start, limit)
        st.success("Done!")
        st.write(result)
        for item in result:
            save_data(item)
