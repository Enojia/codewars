def get_sum(a,b):
    if a==b:
        return a
    else:
        x=0
        for i in range(a,b+1):
            x+=i
        return x

print get_sum(4,1)
