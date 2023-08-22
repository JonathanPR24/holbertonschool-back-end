#!/usr/bin/python3
"""Export employee's completed tasks to CSV"""

import csv
import requests
import sys

def fetch_employee_data(employee_id):
    """Fetches employee data from the API"""
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(api_url)
    return response.json()

def fetch_employee_tasks(employee_id):
    """Fetches tasks owned by the employee from the API"""
    api_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(api_url)
    return response.json()

def filter_completed_tasks(tasks):
    """Filters completed tasks from all tasks"""
    return [task for task in tasks if task["completed"]]

def print_task_summary(employee_name, n_completed_tasks, total_tasks):
    """Prints a summary of completed tasks"""
    print(
        f"Employee {employee_name} is done with "
        f"tasks({n_completed_tasks}/{total_tasks}):"
    )

def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        return

    employee_id = int(sys.argv[1])

    employee_data = fetch_employee_data(employee_id)
    employee_name = employee_data["username"]

    tasks = fetch_employee_tasks(employee_id)
    total_tasks = len(tasks)

    completed_tasks = filter_completed_tasks(tasks)
    n_completed_tasks = len(completed_tasks)

    print_task_summary(employee_name, n_completed_tasks, total_tasks)

    for task in completed_tasks:
        print(f"\t {task['title']}")

    rows = []
    for task in tasks:
        row = employee_id, employee_name, task["completed"], task["title"]
        rows.append(row)

    with open(f"{employee_id}.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(rows)
    print(f"Data exported to {employee_id}.csv")

if __name__ == "__main__":
    main()
