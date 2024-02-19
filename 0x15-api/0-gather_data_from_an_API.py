#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":

    emp_id = sys.argv[1]
    my_user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(emp_id))

    name = my_user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    for task in todos.json():
        if task.get('emp_id') == int(emp_id):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('emp_id') == int(emp_id) and task.get('completed')]))
