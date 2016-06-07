#!/bin/bash/python
from __future__ import division
from fractions import Fraction
import math

def decompose(n):
    ##check if n = "0"
    if n == "0":
        return [];
    
    ##check if we have a float value
    if "/" not in n:
        n = float(n)
        print n
        n = str(Fraction(*n.as_integer_ratio()).limit_denominator())
    
    ## n is a fraction we assign x and y
    x, y = n.split("/")
    x = int(x)
    y = int(y)
    
    ##check if the result is a whole number
    tempResult = x/y
    if tempResult.is_integer():
        return [int(tempResult)]
    
    ##main routine greedy algo 
    result = []

    ## x/y = (1/[y/x] + ((-y) % x) / y[y/x]))
    ## repeat this until there s no more fractions with a numerator > 1

    while(True):
        denom = int(math.ceil(y/x))
        result.append("1/%d" %(denom))
        
        x = ((-y)%x)
        y = y * denom

        print "%d / %d" %(x, y)

        if(x <= 1):
            break

    return result


temp = decompose("0.66")
print temp

