#!/usr/bin/python3


""" This module talks about how this will be implemented """

from sys import argv
import requests
import json


userId = argv[1]
# if __name__ == "__main__":
gett = __import__("0-gather_data_from_an_API")
r_todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
r_employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(userId))
tasks = [task for task in r_todos.json()
         if int(task.get("userId")) == int(userId)]

NAME = r_employee.json().get('name')
username = r_employee.json().get('username')


credentials = {}
list_1 = []

with open(f"{userId}.json", "w") as file:
    for task in tasks:
        task_credentials = {"task": f"{task.get('title')}",
                            "completed": f"{task.get('completed')}",
                            "username": f"{username}"}
        list_1.append(task_credentials)
    credentials[f"{userId}"] = list_1
    json.dump(credentials, file)
