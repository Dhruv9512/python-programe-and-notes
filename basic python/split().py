a="My name is dhruv sharma."
b=a.split(' ')
print(type(b))
print(b)



#  Write a program to input a list value from user.
# p=input("Enter a number for list by seprating it by ',' :- ")
# l1=p.split(',')
# new_list=[ int(n) for n in l1]
# print(new_list)


# Best way to write this above program 
l1=[int(n) for n in input("Enter a number for list by seprating it by ',' :-").split(',')]
print(l1)