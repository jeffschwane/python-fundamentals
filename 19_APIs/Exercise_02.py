'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")
data = response.json()

# pprint(data)
print([x["email"] for x in data["data"]])
