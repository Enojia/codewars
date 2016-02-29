#!/bash/python2

def convertFracts(lst):
    results = []

    for arr in lst:
        for i in range(arr[1],0,-1):
            if arr[0]%i == 0 and arr[1]%i == 0:
                results.append([arr[0]/i, arr[1]/i])
                break
    return results


print  convertFracts([[1,2],[25,20]])


