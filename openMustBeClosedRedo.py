#!/bin/bash/python

def is_balanced(source, caps):
    starter = caps[::2]
    closer = caps[1::2]
    search = ["0"]

    for char in source:
        if char in closer and char == search[-1]:
            search.pop()

        elif char in starter:
            search.append(closer[starter.index(char)])

        elif char in closer and char != search[-1]:
            return False

    if len(search) != 1:
        return False

    else:
        return True



test = is_balanced("Sensei -says no!", "--")
print test
