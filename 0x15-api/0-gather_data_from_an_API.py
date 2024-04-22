#!/usr/bin/python3

""" Gets a todo from a web api """

import requests
from pprint import pprint
from sys import argv

u_id = argv[1]

r_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
r_employee = requests.get(f'https://jsonplaceholder.typicode.com/users/{u_id}')

EMPLOYEE_NAME = r_employee.json().get('name')

# The total number of task assigned to this employee
tasks = [task for task in r_todos.json() if int(task["userId"]) == int(u_id)]

# Get the total task done by the employee
count = 0
for task in tasks:
    if str(task["completed"]) == "True":
        count = count + 1

TOTAL_NUMBER_OF_TASKS = len(tasks)
NUMBER_OF_DONE_TASKS = count

# print the completed tasks by specified employee
print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

for task in tasks:
    if "True" in str(task["completed"]):
        print("\t {}".format(task["title"]))
