def length_of_sequence(arr, n, testNum):
    x = arr.count(n)
    if x == 2:
        num1, num2 = testNum(arr,n)
        return num2 - num1 + 1
    else:
        return 0

def testNum(array, n):
    for i in range(len(array)):
        if array[i]==n:
            yield i


array = [1, 23, 2, 4, 23, 4, 12]
length = length_of_sequence(array, 23, testNum)
print length
