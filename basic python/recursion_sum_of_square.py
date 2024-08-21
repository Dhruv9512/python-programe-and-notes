#---------------- using function -----------------
# def sum_square(i):
#     if i==1:
#        return 1 
#     return i**2 + sum_square(i-1)


# i=int(input("Enter a number to find sum of it's square:- "))
# print("The sum of square of",i,"is :- ",sum_square(i))




#------------------ using lambda -------------------
i=int(input("Enter a number to find sum of it's square:- ")) 
sum_square=lambda i : 1 if i==1 else i**2 + sum_square(i-1)
print("The sum of square of",i,"is :- ",sum_square(i))