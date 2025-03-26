def identify_triangle(a, b, c):

    if a+b>c and a+c>b and b+c>a:
        return "Equilateral Triangle" if a == b == c else "Isosceles Triangle" if a == b or b == c or a == c else "Scalene Triangle"
    return "Not a Triangle"

a, b, c = float(input("Enter first side= ")), float(input("Enter second side= ")), float(input("Enter third side= "))
print(identify_triangle(a, b, c))
