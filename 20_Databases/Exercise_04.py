'''

Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!


'''

'''
import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine(
    "mysql+pymysql://root:plant-outside-123-World@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()

# Get input from the user
while entry not in str(list(range(1, 6))):
    entry = input("Please select from the following options(enter the number of the action you'd like to take): \n1) Create a new table \n2) Insert data into table \n3) Update data in a table\n4) View data in a table \n5) Delete data from a table

# Create a new table
if entry == "1":
    table_name=input("Enter a name for the new table: ")
    newTable=sqlalchemy.Table(table_name, metadata,
        sqlalchemy.Column('Id', sqlalchemy.Integer()),
        sqlalchemy.Column('name', sqlalchemy.String(255), nullable=False),
        sqlalchemy.Column('salary', sqlalchemy.Float(), default=100.0),
        )

# Insert data into a created table
if entry == "2":
    i=input("Enter the ID #: ")
    n=input("Enter the name: ")
    s=int(input("Enter the salary: "))
    query=sqlalchemy.insert(newTable).values(Id=i, name=n, salary=s)
    result_proxy=connection.execute(query)

# Select data from each table
if entry == "3":
    pass
'''
