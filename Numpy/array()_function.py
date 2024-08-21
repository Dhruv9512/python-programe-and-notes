from email import header
from operator import index
from textwrap import indent
import numpy as np
import pandas as pd

arr2 = np.array(["A","B","c"])
D_arr2 = pd.DataFrame(arr2,index=[1,2,3])
print(D_arr2)


l = [[1,2,3,4,5,6],[10,20,30,40,50,60],[100,200,300,400,500,600]]
arr1 = np.array(l)
D_arr1 = pd.DataFrame(arr1,index=[1,2,3])
print(D_arr1)