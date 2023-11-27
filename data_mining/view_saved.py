from sqlalchemy.orm import sessionmaker
from orm import Product, create_engine

engine = create_engine('sqlite:///mining.db')
Session = sessionmaker(bind=engine)
db = Session() # will create a session object
# retrieve all the records
products = db.query(Product).all()
for i in products:
    print(i.title)

# filtering record
query = 'A'
products_with_A = db.query(Product).filter(Product.title.like(f'{query}%')).all()
print(f'Products with {query}')
for item in products_with_A:
    print(item.title)

