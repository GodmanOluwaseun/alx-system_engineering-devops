#!/usr/bin/python3

"""2-export_to_JSON
Export data from an API to json file.
"""


import json
import requests
import sys


def export_employee(employee_id):
    """Retrieves employess details & exports to json"""

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_response = requests.get(user_url)
    employee_data = user_response.json()
    name = employee_data.get('username')

    user_todo = requests.get(todos)
    todo_data = user_todo.json()


    task_list = []
    for task in todo_data:
        tasks = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": name
        }
        task_list.append(tasks)

    tasks_data = {str(employee_id): task_list}

    with open(f"{employee_id}.json", 'w') as file:
        json.dump(tasks_data, file)


if __name__ == "__main__":
    employee_id = (sys.argv[1]
    export_employee(employee_id)
