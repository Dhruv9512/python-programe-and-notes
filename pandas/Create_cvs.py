from operator import index
import pandas as pd
c = {"1":pd.Series(["Dhruv","Sharma"],name="Dhruv_Table"),"2":pd.Series(["Riya","Sharam"]),"3":pd.Series(["Priya","sharma"])}
var2 = pd.DataFrame(c)
print(var2)


First_csv = var2.to_csv("First_CVS.csv",index=False)
# -------------- By using header -------------------
First_csv = var2.to_csv("First_CVS.csv",index=False,header=["A","B","C"])