def print_pattern(n):
    if n > 26 or n<1:
        print("invalid")
        return
    
    char = chr(96 + n)
    print(" ".join([char] * n))

n = int(input("enter a number ="))
print_pattern(n)