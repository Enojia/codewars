#!bin/bash/python2

class liquid:
    def __init__(self, char, value):
        self.data = char
        self.value = value

def insertionSort(array):
    for j in range(1, len(array)):
        i = j
        while(i>0 and array[i].value > array[i-1].value):
            temp = array[i]
            array[i] = array[i-1]
            array[i-1] = temp
            i-=1
            print [liquid.value for liquid in array]
    return array

def init_liquid(data):
    if data == "O":
        return liquid("O", 1)
    elif data == "A":
        return liquid("A", 2)
    elif data == "W":
        return liquid("W", 3)
    elif data == "H":
        return liquid("H", 4)

def separate_liquids(glass):
    tempGlass = [liquid for subGlass in glass for liquid in subGlass]
    tempGlass = [init_liquid(liquid) for liquid in tempGlass]
    sortedGlass = insertionSort(tempGlass)
    for i in range(0,len(glass)):
        for j in range(0, len(glass[i]):
            glass[i][j] = sortedGlass.pop().data
    return glass

test = separate_liquids([["O","O","O","O"],["A","H","W","W"]])
print test
