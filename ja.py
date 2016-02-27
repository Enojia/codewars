#!/bin/bash/python2

def toJadenCase(string):
    arr = string.split()
    result = []
    for word in arr:
        result.append(word.capitalize())
    return " ".join(result)

quote = "How can mirrors"
print toJadenCase(quote)

