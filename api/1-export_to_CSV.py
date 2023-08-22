#!/usr/bin/python3
"""Script to export todo list progress to CSV"""
import requests
import csv
from sys import argv

def information_employee():
    """Returns information about employees"""
    if len(argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        return

    id_employee = int(argv[1])

    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    try:
        response_users = requests.get(url_users)
        response_todos = requests.get(url_todos)
        response_users.raise_for_status()
        response_todos.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error fetching data from the API:", e)
        return

    users = response_users.json()
    todos = response_todos.json()

    user_info = next((user for user in users if user['id'] == id_employee), None)
    if not user_info:
        print("Employee with ID {} not found.".format(id_employee))
        return

    completed_tasks = [
        (user_info['id'], user_info['username'], str(todo['completed']), todo['title'])
        for todo in todos if todo['userId'] == id_employee
    ]

    if not completed_tasks:
        print("No completed tasks for Employee {}.".format(user_info['name']))
        return

    csv_filename = "{}.csv".format(user_info['id'])
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(completed_tasks)

    print("Data exported to {}".format(csv_filename))

if __name__ == "__main__":
    information_employee()
