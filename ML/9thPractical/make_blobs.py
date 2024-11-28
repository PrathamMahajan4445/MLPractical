# from sklearn.datasets import make_blobs 
# import matplotlib.pyplot as plt 

# X,y=make_blobs(n_samples=500,centers=3,n_features=2,random_state=23)

# plt.scatter(X[:,0],X[:,1],c=y)
# plt.show()

from sklearn.datasets import make_blobs 
import matplotlib.pyplot as plt 

X,y=make_blobs(n_samples=500,n_features=2,centers=3,random_state=23)

plt.scatter(X[:,0],X[:,1],c=y)
plt.show()