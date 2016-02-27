#!/bin/bash/python2

def xo(s):
    copy = s.lower()
    chars = list(copy)
    numX = 0
    numY = 0
    print chars

    for char in chars:
        if char == "x":
            print char
            numX += 1
        elif char == "o":
            numY += 1
    print numX
    print numY
    if numX == numY:
        return True
    else:
        return False

answer = xo("xoO")


print answer
