#!/usr/bin/python3

"""0-gather_data_from_an_API
Gather data from an API.
"""


import csv
import requests
import sys


def export_employee(employee_id):
    """Retrieves employess details & prints in specified manner"""

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_response = requests.get(user_url)
    employee_data = user_response.json()
    name = employee_data.get('name')

    user_todo = requests.get(todos)
    todo_data = user_todo.json()

    with open(f"{employee_id}.csv", 'w', newline="") as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)

        for task in todo_data:
            row = [employee_id, name, task.get('completed'), task.get('title')]
            writer.writerow(row)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    export_employee(employee_id)
