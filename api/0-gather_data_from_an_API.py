#!/usr/bin/python3
"""Script to return info about todo list progress"""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(api_url)

    employee_name = response.json()["name"]

    api_url2 = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(api_url2)

    tasks = response.json()
    total_tasks = len(tasks)

    completed_tasks = []
    for task in tasks:
        if task["completed"]:
            completed_tasks.append(task)

    n_total_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({n_total_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task['title']}")
