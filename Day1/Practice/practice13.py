
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("Union = ", union_set)


intersection_set = set1 & set2
print("Intersection = ", intersection_set)

difference_set = set1 - set2
print("Difference = ", difference_set)


print(intersection_set==difference_set)