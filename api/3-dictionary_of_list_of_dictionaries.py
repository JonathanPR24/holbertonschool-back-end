#!/usr/bin/python3
"""Script to return info about todo list progress"""
import json
import requests

def get_user_tasks(user_id):
    api_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(api_url)
    user_data = response.json()

    api_url2 = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(api_url2)
    tasks = response.json()

    user_tasks = []
    for task in tasks:
        user_tasks.append({
            "username": user_data["username"],
            "task": task["title"],
            "completed": task["completed"]
        })

    return user_tasks

def main():
    api_users_url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(api_users_url)
    users = response.json()

    json_dict = {}

    for user in users:
        user_id = user["id"]
        json_dict[user_id] = get_user_tasks(user_id)

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(json_dict, json_file, indent=4)

if __name__ == "__main__":
    main()
