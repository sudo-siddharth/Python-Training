def print_hollow_square(n):
    if n <= 0:
        return
    
    # Create a list to store the numbers in spiral order
    numbers = []
    for i in range(1, n*n + 1):
        numbers.append(str(i))
    
    # Create an n x n matrix filled with spaces
    matrix = [[' ' for _ in range(n)] for _ in range(n)]
    
    # Fill the outer layer (border) with numbers in order
    index = 0
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                matrix[i][j] = numbers[index]
                index += 1
    
    # Print the matrix with the same format
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print(str(matrix[i][j]).rjust(2), end=' ')
            else:
                print('  ', end=' ')
        print()

n = int(input("Enter the number: "))
print_hollow_square(n)