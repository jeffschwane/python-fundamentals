'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''

import sqlalchemy
import requests
from pprint import pprint
base_url = "http://demo.codingnomads.co:8080/tasks_api"

# Get all of the users
response = requests.get(base_url + "/users")
user_data = response.json()
user_list = user_data["data"]
for item in user_list:
    item['user_id'] = item.pop('id')
# pprint(user_list)

# Get all of the tasks
response = requests.get(base_url + "/tasks")
task_data = response.json()
task_list = task_data["data"]
for item in task_list:
    item['task_id'] = item.pop('id')
    item['user_id'] = item.pop('userId')
# pprint(task_list)

# Connect to local database
engine = sqlalchemy.create_engine(
    "mysql+pymysql://root:plant-outside-123-World@localhost/database_lab")
connection = engine.connect()
metadata = sqlalchemy.MetaData()

# Create new tables

# User table
user = sqlalchemy.Table('user', metadata,
                        sqlalchemy.Column('user_id', sqlalchemy.Integer()),
                        sqlalchemy.Column(
                            'first_name', sqlalchemy.String(255), nullable=False),
                        sqlalchemy.Column(
                            'last_name', sqlalchemy.String(255), nullable=False),
                        )

# Tasks table
task = sqlalchemy.Table('task', metadata,
                        sqlalchemy.Column('task_id', sqlalchemy.Integer()),
                        sqlalchemy.Column(
                            'name', sqlalchemy.String(255), nullable=False),
                        sqlalchemy.Column(
                            'description', sqlalchemy.String(255), nullable=False),
                        )

# User_tasks table
user_task = sqlalchemy.Table('user_task', metadata,
                             sqlalchemy.Column(
                                 'user_id', sqlalchemy.Integer()),
                             sqlalchemy.Column(
                                 'task_id', sqlalchemy.Integer())
                             )

# Execute table creation
metadata.create_all(engine)


# Insert API data into database tables (check to see if the record already exists before inserting it)

# User table

query = sqlalchemy.insert(user)
new_records = user_list
result_proxy = connection.execute(query, new_records)

# Tasks table

query = sqlalchemy.insert(task)
new_records = task_list
result_proxy = connection.execute(query, new_records)

# User_tasks table

query = sqlalchemy.insert(user_task)
new_records = task_list
result_proxy = connection.execute(query, new_records)
