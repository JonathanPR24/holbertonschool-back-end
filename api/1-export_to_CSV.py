#!/usr/bin/python3
"""This script retrieves employee TODO list progress and exports it in CSV format"""
import requests
import sys
import csv

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(api_url)

    employee_name = response.json()["username"]
    
    api_url2 = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(api_url2)

    tasks = response.json()

    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for task in tasks:
            task_completed_status = "True" if task["completed"] else "False"
            task_title = task["title"]
            csv_writer.writerow([employee_id, employee_name, task_completed_status, task_title])

    print(f"Data exported to {csv_filename}")
