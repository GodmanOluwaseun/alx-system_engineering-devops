#!/usr/bin/python3

"""3-dictionary_of_list_of_dictionaries
Export all user data from an API to json file.
"""


import json
import requests
import sys


def export_employees():
    """Retrieves all employess details & exports to json"""

    user_url = "https://jsonplaceholder.typicode.com/users"
    todos = "https://jsonplaceholder.typicode.com/todos"

    user_response = requests.get(user_url)
    employee_data = user_response.json()

    user_todo = requests.get(todos)
    todo_data = user_todo.json()

    tasks_dict = {}

    for user in employee_data:
        user_id = user.get('id')
        username = user.get('username')

        task_list = []
        for task in todo_data:
            if task.get('id') == user_id:
                tasks = {
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                task_list.append(tasks)

        tasks_dict[str(user_id)] = task_list

    with open("todo_all_employees.json", 'w') as file:
        json.dump(tasks_dict, file)


if __name__ == "__main__":
    export_employees()
