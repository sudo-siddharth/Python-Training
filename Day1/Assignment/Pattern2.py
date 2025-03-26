def print_hollow_square(n):
    if n <= 0:
        return

    matrix = [['  ' for _ in range(n)] for _ in range(n)]
    num = 1
    left, right, top, bottom = 0, n - 1, 0, n - 1
    
    while left <= right and top <= bottom:
   
        for i in range(left, right + 1):
            matrix[top][i] = f"{num:2}"
            num += 1
        top += 1
       
        for i in range(top, bottom + 1):
            matrix[i][right] = f"{num:2}"
            num += 1
        right -= 1
      
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = f"{num:2}"
                num += 1
            bottom -= 1
       
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = f"{num:2}"
                num += 1
            left += 1
    
    for row in matrix:
        print(' '.join(cell if i == 0 or i == n - 1 or row is matrix[0] or row is matrix[-1] else '  ' for i, cell in enumerate(row)))

n = int(input("enter the number = "))
print_hollow_square(n)