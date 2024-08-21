month=int(input("Enter a month:- "))
year=int(input("Enter a year:- "))

if year%4==0:
    days=[31,29,31,30,31,30,31,31,30,31,30,31]
    print("This month has ",days[month-1],"days.")
else:
     days=[31,28,31,30,31,30,31,31,30,31,30,31]
     print("This month has",days[month-1],"days.")