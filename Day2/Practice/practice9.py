def sum_of_numbers(*args):
    return sum(args)

result = sum_of_numbers(1, 2, 3, 4, 5)
print("The sum is:", result)


# using positional and keyword arguments in function definition
def my_function(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

my_function(1, 2, 3, d=4, e=5, f=6)