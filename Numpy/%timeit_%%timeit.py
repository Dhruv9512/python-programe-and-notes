import timeit
import pandas as pd 
import numpy as np

dic1 = {"A":[1,2,3,4,5,6],"B":[10,20,30,40,50,60],"C":[100,200,300,400,500,600]}

%timeit arr1 = np.array([ dic1[v] for v in dic1])

print(arr1)




