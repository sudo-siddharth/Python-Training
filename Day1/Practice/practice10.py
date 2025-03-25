my_list = [10, 20, 30, 40, 50]

length = len(my_list)
first_element = my_list[0]
last_element = my_list[-1]
reversed_list = my_list[::-1]
sum_of_elements = sum(my_list)
max_element = max(my_list)
min_element = min(my_list)

my_list.append(60)
my_list.remove(20)
my_list.insert(2, 25)
my_list.pop(3)
sorted_list = sorted(my_list)

print(length)
print(first_element)
print(last_element)
print(reversed_list)
print(sum_of_elements)
print(max_element)
print(min_element)

my_list[0] = 100
print(my_list)

my_list[1:4] = [200, 300, 400]
print(my_list)

my_list.insert(1, 15)  
print(my_list)

my_list.append(500)
print(my_list)

my_list.pop()
print(my_list)

my_list.remove(200) 
print(my_list)

del my_list[2]  
print(my_list)

my_list.clear()
print(my_list)
