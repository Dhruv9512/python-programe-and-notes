import pandas as pd
D_l_1 = {"A":[1,2,3,4],"B":[10,20,30,40],"F":[100,200,300,400]}
var = pd.DataFrame(D_l_1)
print(var)
var1 = var.pop("F") # -> Delete column
print(var)

# ------------------ Del use --------------------
del var["B"]
print(var)