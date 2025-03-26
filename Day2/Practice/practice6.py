def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("enter a number: "))
for num in range(2, n + 1):
    if is_prime(num):
        print(num, end=' ')