def print_hollow_square(n):
    if n<=0:
        return
    
    numbers = []
    for i in range(1,n*n+1):
        numbers.append(str(i))
    
    matrix=[[' ' for _ in range(n)] for _ in range(n)]
    
    index=0
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                matrix[i][j]=numbers[index]
                index+= 1
    
    for i in range(n):
        for j in range(n):
            if i==0 or i== n - 1 or j== 0 or j== n - 1:
                print(str(matrix[i][j]).rjust(2), end=' ')
            else:
                print('  ',end=' ')
        print()

n=int(input("enter the number= "))
print_hollow_square(n)