# import numpy as np

# def normal(x,mean,sd):
#     print(np.pi*sd)
#     prob=(np.pi*sd)*np.exp(-0.5*((x-mean)/sd)**2)
#     return prob

# x=1
# mean=0
# sd=1

# result=normal(x,mean,sd)
# print(result)

import numpy
import matplotlib.pyplot as plt 

x=numpy.random.normal(5.0,1.0,10000)
plt.hist(x,100)
plt.show()