a=int(input("Enter a number to find it's digit:- "))
i=a
count=0
while not i==0:
    count+=1
    print(i)
    i//=10
print("The digit in",a,"number is:- ",count)