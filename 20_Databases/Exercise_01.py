'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''

import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine("mysql+pymysql://root:plant-outside-123-World@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)

for i in [film, category]:
    query = sqlalchemy.select([i])
    result_proxy = connection.execute(query)

    result_set = result_proxy.fetchall()
    pprint(result_set)