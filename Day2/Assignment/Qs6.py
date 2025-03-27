def print_pascals_triangle(n):
    for i in range(n):
       
        print(' ' * (n - i - 1), end='')
        
        row = [1]
        
        for j in range(1, i + 1):
            
            next_val = row[j - 1] * (i - j + 1) // j
            row.append(next_val)
        
        print(' '.join(map(str, row)))

print_pascals_triangle(int(input("Enter the number of rows: ")))