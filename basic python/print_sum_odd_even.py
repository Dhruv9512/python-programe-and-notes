l =[2,2,6,4,5,9,5]
sum_odd=[n for n in l if not n%2==0]
sum_even=[n for n in l if  n%2==0]

print("The sum of odd is:- ",sum(sum_odd))
print("The sum of even is:- ",sum(sum_even))