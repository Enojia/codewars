#!/bin/bash/python2

def tribonacci(sig, n):
    arr = sig
    i=3

    while(i<=n):
        arr.append(arr[i-1] + arr[i-2] + arr[i-3])
        i+=1
    return arr

print tribonacci([1,2,3], 9)
