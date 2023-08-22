#!/usr/bin/python3
"""Script to return info about todo list progress"""
import requests
import sys
import json

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(api_url)

    employee_data = response.json()
    employee_name = employee_data["name"]
    username = employee_data["username"]

    api_url2 = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(api_url2)

    tasks = response.json()

    user_tasks = []
    for task in tasks:
        user_tasks.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        })

    output_data = {str(employee_id): user_tasks}
    output_filename = f"{employee_id}.json"

    with open(output_filename, "w") as output_file:
        json.dump(output_data, output_file, indent=4)

    print(f"Data exported to {output_filename}")
