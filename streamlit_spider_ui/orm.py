# object relational mapping
from sqlalchemy.orm import declarative_base 
from sqlalchemy import create_engine 
from sqlalchemy import Column, Integer, String, DateTime 
from datetime import datetime

Base = declarative_base()
class Product(Base):
    __tablename__ = 'articles' # double underscore
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author = Column(String(255))
    length = Column(String(255))
    link = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title
    

# creating the database
if __name__ == "__main__":
    path_to_db = 'streamlit_spider_ui/spider.db'
    engine = create_engine(f'sqlite:///{path_to_db}')
    Base.metadata.create_all(engine)
    print('🌀 Database Created')