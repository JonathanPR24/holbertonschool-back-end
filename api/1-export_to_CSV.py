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

def export_to_csv(employee_id, employee_name, tasks):
    """Exports tasks to CSV file"""
    csv_filename = f"{employee_id}.csv"
    rows = []
    for task in tasks:
        row = (employee_id, employee_name, task["completed"], task["title"])
        rows.append(row)

    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(rows)

def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        return

    employee_id = int(sys.argv[1])

    employee_data = fetch_employee_data(employee_id)
    employee_name = employee_data["username"]

    tasks = fetch_employee_tasks(employee_id)
    completed_tasks = [task for task in tasks if task["completed"]]

    n_total_tasks = len(tasks)
    n_completed_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with "
        f"tasks({n_completed_tasks}/{n_total_tasks}):"
    )

    for task in completed_tasks:
        print(f"\t {task['title']}")

    export_to_csv(employee_id, employee_name, tasks)
    print(f"Data exported to {employee_id}.csv")

if __name__ == "__main__":
    main()
