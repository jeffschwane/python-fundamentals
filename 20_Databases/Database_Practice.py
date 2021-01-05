import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine(
    "mysql+pymysql://root:plant-outside-123-World@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table(
    'actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table(
    'film_actor', metadata, autoload=True, autoload_with=engine)

join_statement = actor.join(
    film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(
    film, film.columns.film_id == film_actor.columns.film_id)
query = sqlalchemy.select([
    film.columns.film_id,
    film.columns.title,
    actor.columns.first_name,
    actor.columns.last_name]).select_from(join_statement)

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)
