import cmath

a = float(input("Enter coefficient of a:- "))
b = float(input("Enter coefficient of b:- "))
c = float(input("Enter coefficient of c:- "))

D = (b**2) - (2*a*c)

if D>0:
    root1 = -b + cmath.sqrt(D)/(2*a)
    root2 = -b - cmath.sqrt(D)/(2*a)
    print(root1 , "and", root2 ,"roots are real and unequal.")
elif D==0:
    root = -b/(2*a)
    print(root ,"root are real and same.")
else:
    print("No real roots are there.")
