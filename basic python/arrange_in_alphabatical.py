str=input("Enter your name:- ").lower().split(' ')
l=[n for n in str if not n=='']
l.sort()

print(' '.join(l))