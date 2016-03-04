#!/bin/bash/python2

def revrot(strng, sz):
    if sz <= 0 or sz > len(strng) or strng =="":
        return ""

    array = [strng[i:i+2] for i in range(0, len(strng), 2)]

    if len(array[len(array)-1]) < sz:
        array.pop()
    result = []

    for chunk in array:
        print chunk
        res = 0
        for num in  list(chunk):
            res += int(num)**3
        if res % 2 == 0:
            result.append(chunk[::-1])
            print result
        else:
            temp = [chunk[(i+1)%len(chunk)] for i in range(0,len(chunk))]
            result.append("".join(temp))
            print result


    return "".join(result)


lst = revrot("1234567", 2)
print lst

