#!/usr/bin/python3

""" The Documented module """

from sys import argv
import requests


userId = argv[1]
if __name__ == "__main__":
    r_todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    r_employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                              .format(userId))
    tasks = [task for task in r_todos.json()
             if int(task.get("userId")) == int(userId)]

    NAME = r_employee.json().get('name')

    with open(f"{userId}.csv", "w") as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(task.get("userId"),
                                                      NAME,
                                                      task.get("completed"),
                                                      task.get("title")))
