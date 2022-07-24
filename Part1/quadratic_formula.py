from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

d = b**2 - 4*a*c

if d < 0:
    print("The equation has no real roots")
elif d == 0:
    x = (-b + sqrt(d)) / (2*a)
    print("There is a double root at", x)
else:
    x1 = (-b + sqrt(d)) / (2*a)
    x2 = (-b - sqrt(d)) / (2*a)
    print("The roots are", x1, "and", x2)