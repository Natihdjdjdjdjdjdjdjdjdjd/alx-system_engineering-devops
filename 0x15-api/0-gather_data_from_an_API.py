#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == '__main__':
    emp_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users"
    url = user_url + "/" + emp_id

    my_response = requests.get(url)
    emp_NAME = my_response.json().get('name')

    todoUrl = url + "/todos"
    my_response = requests.get(todoUrl)
    tasks = my_response.json()
    totalTasks = len(tasks)

    NUMBER_OF_DONE_TASKS = 0
    tasksList = []

    for task in tasks:
        if task.get('completed'):
            tasksList.append(task)
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_NAME, NUMBER_OF_DONE_TASKS, totalTasks))

    for task in tasksList:
        print("\t {}".format(task.get('title')))
