import pandas as pd


# --------------  List of series -------------
a=[5,2,6,6,5,8,9,5]
var = pd.Series(a , name="Riy_Table",index=[1,2,3,4,5,6,7,8])
print(var)


# --------------  Dict of series -------------
b={"a":[1,2,3,4],"b":[1,2,3,4,5,6]}
var1 = pd.Series(b, name="Dhr_Table")
print(var1)