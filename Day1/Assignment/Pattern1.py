
def print_pattern(n):
    
    for i in range(1, n + 1):
        print('* ' * i)
    
    for i in range(n - 1, 0, -1):
        print('* ' * i)

# Input from the user
n = int(input("Enter the value of n: "))
print_pattern(n)