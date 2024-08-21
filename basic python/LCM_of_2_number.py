a=int(input("Enter a first number:- "))
b=int(input("Enter a second number:- "))

# --------------------- best way ------------------

LCM = [n for n in range(max(a,b),a*b+1) if n%a==0 and n%b==0]
print("The lcm is:- ",min(LCM))


