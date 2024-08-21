a = int(input("Enter a first number:- "))
b = int(input("Enter a second number:- "))

HCF = [ n for n in range(1,min(a,b)+1) if a%n==0 and b%n==0]

print("The hcf is:- ",max(HCF))
