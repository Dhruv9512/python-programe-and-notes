n = int(input("Enter a number to find that much prime number:- "))
# count = 0
# a = 2
# while not count==n:
#     i = 2
#     while i<a:
#         if a%i==0:
#             a+=1
#             i=1
#         i+=1
#     else:
#         print(a, end=' ')
#         a+=1       
#         count+=1



#-------------------------- other way -----------------
def prime(i):
    for a in range(2,i):
        if i%a==0:
            return False
    return True
p=[]
for a in range(2,n**2):
    if len(p)==n:
        break
    if prime(a):
        p.append(a)
print(p)
print("length is:- ",len(p))