a=int(input("Enter a number to find it is prime number or not:- "))
check=True
for n in range(2,a):
    if a%n==0:
        check=False

if check:
    print("It is a prime.")
else:
    print("It is not a prime.")

    

