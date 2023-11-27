# object relational mapping
from sqlalchemy.orm import declarative_base # required for creating models classes
from sqlalchemy import create_engine # required for db connection
from sqlalchemy import Column, Integer, String, DateTime # required for columns
from datetime import datetime # required for datetime column

# create base class
Base = declarative_base()
# create model class -> table in db
class Product(Base):
    __tablename__ = 'products' # double underscore
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    price = Column(String(255))
    url = Column(String(255))
    imgurl = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())

    def __str__(self):
        return self.title
# creating the database
if __name__ == "__main__":

    engine = create_engine('sqlite:///mining.db', echo=True)
    Base.metadata.create_all(engine)
    print('🌀 Database Created')