def print_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0:  # Top border
                print(j + 1, end=" ")
            elif j == n - 1:  # Right border
                print(n + i, end=" ")
            elif i == n - 1:  # Bottom border
                print(3 * n - 2 - j, end=" ")
            elif j == 0:  # Left border
                print(4 * n - 3 - i, end=" ")
            else:
                print(" ", end=" ")
        print()

n = int(input("Enter the size of the square "))
print_hollow_square(n)