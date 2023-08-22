#!/usr/bin/python3
"""This script retrieves employee TODO list progress and exports it in CSV format"""
import requests
import sys
import csv

def export_to_csv(employee_id, employee_name, tasks):
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks:
            task_completed_status = "True" if task["completed"] else "False"
            task_title = task["title"]
            csv_writer.writerow([employee_id, employee_name, task_completed_status, task_title])

    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(api_url)

    if response.status_code != 200:
        print("Error fetching user data from the API.")
        sys.exit(1)

    employee_name = response.json()["username"]

    api_url2 = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(api_url2)

    if response.status_code != 200:
        print("Error fetching tasks data from the API.")
        sys.exit(1)

    tasks = response.json()

    total_tasks = len(tasks)

    completed_tasks = [task for task in tasks if task["completed"]]

    n_total_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with "
        f"tasks({n_total_tasks}/{total_tasks}):"
    )

    for task in completed_tasks:
        print(f"\t {task['title']}")

    export_to_csv(employee_id, employee_name, completed_tasks)
