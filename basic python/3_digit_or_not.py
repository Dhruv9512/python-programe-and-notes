a=int(input("Enter a number to check it is a 3 digit or not:- "))
i=a
count=1
while not i==0:
    if count>3:
        print(a,"is not a 3 digit number.")
        break
    count+=1
    i//=10
else:
    print(a,"is a 3 digit number.")
    