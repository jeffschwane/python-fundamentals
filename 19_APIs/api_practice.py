'''import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8081/tasks_api/tasks"
body = {
    "description": "I created a post - yay!",
    "id": 75,
    "name": "Jeff",
    "userId": 0
}
response = requests.post(base_url, json=body)
print(response.status_code)
response = requests.get(base_url)
data = response.json()
pprint(data)
'''

import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 216,
    "first_name": "Paige",
    "last_name": "Turner",
    "email": "email-shemail@gmail.com"
}

# here we execute the PUT request
response = requests.put(base_url, json=body)
# print the status code (hopefully it's 200 which means all is well)
print(f"Response Code: {response.status_code}")

# let's make a GET request to retrieve the new data from the server
response = requests.get(base_url)
# print the data - see your updated record?
print(f"Response Content: {response.content}")
