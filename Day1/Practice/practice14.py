
my_dict = {
    "name": "Siddharth",
    "age": 21, "city":
    "Hyderabad"
    }

print(my_dict)

# accessing the value of key name
print(my_dict["name"])

#accessing with for loop
for key in my_dict:
    print(key, my_dict[key])

print(my_dict.keys())

#accessing with items() method
for key, value in my_dict.items():
    print(key, value)

#updating the value of key age
my_dict["age"] = 22

#other method to update the value of key age
my_dict.update({"age": 23})

#multiple values can be updated at once
my_dict.update({"age": 24, "city": "Bangalore"})

#multiple values in one key
my_dict["address"] = ["Hyderabad", "Bangalore"]
print(my_dict)

#using popitem() method
popped_item = my_dict.popitem()
print(popped_item)

#using pop() method
if "address" in my_dict:
    popped_item = my_dict.pop("address")
    print(popped_item)

#using clear() method
my_dict.clear()
print(my_dict)

#using del keyword
del my_dict
print(my_dict)
