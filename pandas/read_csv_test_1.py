from multiprocessing import Value
import pandas as pd
var = pd.read_csv("C:\\Users\\dhruv sharma\\Downloads\\panda test 1.csv",nrows=2,usecols=["Value"])
print(var)