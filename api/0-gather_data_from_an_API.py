#!/usr/bin/python3
"""Script to return info about todo list progress"""
import requests
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

    completed_tasks = [todo['title'] for todo in todos if todo['userId'] == id_employee and todo['completed']]
    total_tasks = len(completed_tasks) + user_info['id']

    print('Employee {} is done with tasks({}/{}):'.format(user_info['name'], len(completed_tasks), total_tasks))
    for title in completed_tasks:
        print('\t{}'.format(title))

if __name__ == "__main__":
    information_employee()
