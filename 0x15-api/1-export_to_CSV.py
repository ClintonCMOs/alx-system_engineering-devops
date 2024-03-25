#!/usr/bin/python3
"""
The script will fetch data from a jsonplaceholder API
about an employee's TODO list progress
It will accept an employee ID as an integer parameter
and print the information in the specified format

After that, it will export data in the CSV format
"""

import requests
import sys
import csv

if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                    .format(employeeId, username, task.get('completed'),
                            task.get('title')))