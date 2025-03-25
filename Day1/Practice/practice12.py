
my_set = {1, 2, "apple", 4, 5}

#printing the set
for item in my_set:
    print(item)

 # checking if apple is present in the set   
if "apple" in my_set:
    print("'apple' is present in the set")

if 3 not in my_set:
    print("3 is not present in the set")


#adding an element to the set
my_set.add(6)
print(my_set)

# removing an element from the set
my_set.remove(6)
print(my_set)

# using update to add multiple elements
my_set.update([6, 7, 8])
print(my_set)


my_set.discard(8)
print("After discard(8):", my_set)

popped_element = my_set.pop()
print("Popped element:", popped_element)
print("After pop():", my_set)

del my_set