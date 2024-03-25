#!/usr/bin/python3
"""
The script will fetch data from a jsonplaceholder API
It will export data in the JSON format.
After that, Records all tasks from all employees
"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dictionary, f)
