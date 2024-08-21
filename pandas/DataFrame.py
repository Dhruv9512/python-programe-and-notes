from math import nan
from tkinter.tix import COLUMN
import pandas as pd

# ------------------  By single list -----------------
a = [1,2,3,4,5,6,7,8,9]
var = pd.DataFrame(a)
print(var)



# ------------------------  By dict ----------------------
b = {"a":[1,2,3,4],"b":[1,2,3,4]}
var1 = pd.DataFrame(b)
print(var1)


# ------------------------- By Multiple Series --------------
c = {"1":pd.Series(["Dhruv","Sharma"],name="Dhruv_Table"),"2":pd.Series(["Riya","Sharam"]),"3":pd.Series(["Priya","sharma"])}
var2 = pd.DataFrame(c)
print(var2)



# ---------------------- By multiple list --------------------------
d = [[1,2,3,4,5],[11,12,13,14,15],[nan,200,300,nan,500]] # There must be same length
var3 =pd.DataFrame(d)

print(var3)

