#!/usr/bin/python3
""" given employee ID, returns information about his/her TODO list """
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(employee_id))

    if user_response.status_code != 200:
        print("User with ID {} not found.".format(employee_id))
        sys.exit(1)

    user = user_response.json()

    todos_response = requests.get(url + "todos", params={"userId": employee_id})

    if todos_response.status_code != 200:
        print("Failed to retrieve TODO list for user with ID {}.".format(employee_id))
        sys.exit(1)

    todos = todos_response.json()

    completed = []

    for todo in todos:
        if todo.get("completed"):
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks ({}/{})".format(user.get("name"), len(completed), len(todos)))

    for complete in completed:
        print("\t{}".format(complete))
