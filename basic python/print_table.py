n = int(input("Enter a number to get it's table:- "))
table = [a*n for a in range(1,11) ]
for a in range(1,11):
    print(n,"*",a," = ", table[a-1])