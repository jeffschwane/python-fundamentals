'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

'''

import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine(
    "mysql+pymysql://root:plant-outside-123-World@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
actor = sqlalchemy.Table(
    'actor', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table(
    'film_actor',
    metadata,
    autoload=True,
    autoload_with=engine)
category = sqlalchemy.Table(
    'category', metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table(
    'film_category', metadata, autoload=True, autoload_with=engine)

join_statement = actor \
    .join(
        film_actor,
        film_actor.columns.actor_id == actor.columns.actor_id) \
    .join(
        film,
        film.columns.film_id == film_actor.columns.film_id)

join_statement_2 = category \
    .join(
        film_category,
        film_category.columns.category_id == category.columns.category_id) \
    .join(
        film,
        film.columns.film_id == film_category.columns.film_id
    )


def display_sql(query):
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()
    pprint(result_set)


query_1 = sqlalchemy.select([actor]).where(actor.columns.first_name == 'GARY')
query_2 = sqlalchemy.select([
    actor.columns.first_name,
    actor.columns.last_name,
    film.columns.title
]).select_from(join_statement)
query_3 = sqlalchemy.select([
    film.columns.title
]).where(
    category.columns.name == "Comedy").select_from(join_statement_2)
query_4 = sqlalchemy.select([
    actor.columns.first_name,
    actor.columns.last_name,
    film.columns.title
]).select_from(join_statement).where(film.columns.title == "GROUNDHOG UNCUT")
query_5 = sqlalchemy.select([
    film.columns.title,
    film.columns.rental_rate
]).where(
    category.columns.name == "Comedy").select_from(join_statement_2).order_by(sqlalchemy.asc(film.columns.rental_rate))


display_sql(query_5)
