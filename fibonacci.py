#!/bin/bash/python2

def fibonacci(n):
    arr=[0,1]
    i=2
    while i <= n:
        arr.append(arr[i-1] + arr[i-2])
        i+=1

    return arr[n]

print fibonacci(9)
