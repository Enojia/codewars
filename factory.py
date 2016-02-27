def factory(x):
    def multByx(array):
        array = [y * x for y in array]
        return array
    return multByx


fives = factory(5)
my_array = [1,2,3]

fives(my_array)
print my_array
