#!/usr/bin/python3
"""
The script will fetch data from a fictional API
about an employee's TODO list progress
It will accept an employee ID as an integer parameter
and print the information in the specified format
"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get("name")

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    finished = 0
    finished_tasks = []

    for task in tasks:
        if task.get('completed'):
            finished_tasks.append(task)
            finished += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, finished, len(tasks)))

    for task in finished_tasks:
        print("\t {}".format(task.get('title')))
