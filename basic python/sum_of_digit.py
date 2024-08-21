a=int(input("Enter a number to find sum of digit of given number:- "))
i=a
sum=0
while i>=1:
    sum+=i%10
    i//=10
print("The sum of digit of",a,"number is:- ",sum)