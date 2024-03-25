#!/usr/bin/python3
"""
The script will fetch data from a jsonplaceholder API
about an employee's TODO list progress
It will accept an employee ID as an integer parameter
and print the information in the specified format
"""

import requests
import sys
import csv

if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get("name")

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    # File name in the format USER_ID.csv
    file_name = f"{employeeId}.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Writing the header
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Writing each task
        for task in tasks:
            writer.writerow([employeeId, employeeName, task.get('completed'), task.get('title')])

    print(f"Data for employee {employeeName} has been written to {file_name}")
