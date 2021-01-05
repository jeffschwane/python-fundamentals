'''

Create an application that interfaces with the user via the CLI - prompt the
user with a menu such as:

Please select from the following options (enter the number of the action you'd
like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu
options above.


'''

import requests


def show_tasks(complete):
    """Outputs task name and description to console based on user ID and
    query"""

    userid = input("Enter user ID: ")
    query = {
        "userId": int(userid),
        "complete": complete
    }
    response = requests.get(base_url + "/tasks", params=query)
    data = response.json()
    print([x["name"] + ': ' + x["description"] for x in data["data"]])


base_url = "http://demo.codingnomads.co:8080/tasks_api"
entry = "null"

# Get input from the user
while entry not in str(list(range(1, 8))):
    entry = input("Please select from the following options(enter the number of the action you'd like to take): \n1) Create a new account \n2) View all your tasks \n3) View your completed tasks\n4) View only your incomplete tasks \n5) Create a new task \n6) Update an existing task \n7) Delete a task")


# Create a new account
if entry == "1":
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    body = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    response = requests.post(base_url + "/users", json=body)
    if response.status_code == 200:
        print(f"Created account {first_name} {last_name}, {email}")

# View all your tasks
elif entry == "2":
    show_tasks("*")

# View your completed tasks
elif entry == "3":
    show_tasks("true")

# View your incomplete tasks
elif entry == "4":
    show_tasks("false")

# Create a new task
elif entry == "5":
    userid = input("Enter user ID: ")
    new_task_name = input("Enter new task name: ")
    new_task_desc = input("Enter new task description: ")
    body = {
        "userId": int(userid),
        "name": new_task_name,
        "description": new_task_desc
    }
    response = requests.post(base_url + "/tasks", json=body)
    if response.status_code == 200:
        print(f'Created new task "{new_task_name}: {new_task_desc}"')

# Update an existing task
elif entry == "6":
    userid = input("Enter user ID: ")
    task_no = input("Enter the task number: ")
    name = input("Enter the updated name: ")
    desc = input("Enter the updated description: ")
    body = {
        "name": name,
        "userId": int(userid),
        "id": task_no,
        "description": desc
    }
    response = requests.put(base_url + "/tasks", json=body)
    if response.status_code == 200:
        print(f'Updated task desciption "{desc}"')

# Delete a task
elif entry == "7":
    delete = input("Enter the task number to delete: ")
    response = requests.delete(base_url + "/tasks/" + delete)
    if response.status_code == 200:
        print(f'Deleted task, "{delete}"')
