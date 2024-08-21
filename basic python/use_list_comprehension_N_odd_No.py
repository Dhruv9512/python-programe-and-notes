# n=int(input("Enter a number to get odd number:- "))
# l1=[ n for n in range(1,n*2,2)]
# print(l1)





# l1=list(range(1,n*2,2))
# print(l1)




#   ------------------------- Best method of doing this---------------------
l1=[ (n*2)-1 for n in range(1,int(input("Enter a number to get odd number:- "))+1)]
print(l1)
