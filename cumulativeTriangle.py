
def cumulative_triangle(n):
    result = 0
    init_num = 1
    
    for i in range(1, n):
        init_num += i 

    for i in range(0, n):
        result += (init_num + i)

    return result

print cumulative_triangle(5)
