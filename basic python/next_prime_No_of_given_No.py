n = int(input("Enter a number to find it's next prime number:- "))
i=2
a=n+1
while i<a:
    if a%i==0:
      a+=1
      i=1
    i+=1
else:
    print("Next prime number of",n,"is :- ",a)      