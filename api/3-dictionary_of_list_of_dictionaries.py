#!/usr/bin/python3
"""Script to return info about todo list progress"""
import requests
import sys
import json

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(api_url)
    employee_name = response.json()["name"]

    api_url2 = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(api_url2)
    tasks = response.json()
    
    completed_tasks = []
    for task in tasks:
        completed_tasks.append({
            "username": employee_name,
            "task": task["title"],
            "completed": task["completed"]
        })

    with open("todo_all_employees.json", "a") as json_file:
        json.dump({employee_id: completed_tasks}, json_file)
        json_file.write("\n")
