# creating tuple with one item with and without comma and checking the type of both
my_tuple = (1,)
print(type(my_tuple))

my_tuple = (1)
print(type(my_tuple))

#unpacking a collection each of them to variable from list
my_list = [1, 2, 3]
a, b, c = my_list
print(a)

#slicing a tuple
my_tuple = (1, 2, 3, 4, 5)  
print(my_tuple[1:4])

#checking if an item exists in a tuple
print(3 in my_tuple)
