# import numpy as np
# from sklearn.linear_model import LinearRegression 

# x=np.array([[1,1],[1,2],[2,2],[2,3]])
# y=np.dot(x,np.array([1,2]))+3

# model=LinearRegression().fit(x,y)

# print("coefficient: ",model.coef_)
# print("intercept: ",model.intercept_)

import numpy as np 
from sklearn.linear_model import LinearRegression 

x=np.array([[1,1],[1,2],[2,2],[2,3]])
y=np.dot(x,np.array([1,2]))+3

model=LinearRegression().fit(x,y)

print("coefficient: ",model.coef_)
print("intercept: ",model.intercept_)