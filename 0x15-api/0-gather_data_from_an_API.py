#!/usr/bin/python3

""" Gets a todo from a web api """

import requests
from sys import argv

id = argv[1]

r_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
r_employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(id))

NAME = r_employee.json().get('name')

# The total number of task assigned to this employee
tasks = [task for task in r_todos.json()
         if int(task.get("userId")) == int(id)]

# Get the total task done by the employee
count = 0
for task in tasks:
    if str(task.get("completed")) == "True":
        count = count + 1

TOTAL_TASKS = len(tasks)
DONE_TASKS = count

if __name__ == "__main__":
    # print the completed tasks by specified employee
    print(f"Employee {NAME} is done with tasks({DONE_TASKS}/{TOTAL_TASKS}):")

    for task in tasks:
        if "True" in str(task.get("completed")):
            print("\t {}".format(task["title"]))
