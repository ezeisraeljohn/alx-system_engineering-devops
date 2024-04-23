#!/usr/bin/python3


""" This module talks about how this will be implemented """


gett = __import__("0-gather_data_from_an_API")


if __name__ == "__main__":


    with open(f"{gett.id}.csv", "w") as file:
        for task in gett.tasks:
            file.write('"{}","{}","{}","{}"\n'.format(gett.id, gett.NAME,
                                                      task.get("completed"),
                                                      task.get("title")))
