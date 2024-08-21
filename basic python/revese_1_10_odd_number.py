a=int(input("Enter number to print odd number in reverse order:- "))
i=a*2
while i>=1:
    if not i%2==0:
        print(i)
    i-=1