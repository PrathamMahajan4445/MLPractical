# from sklearn.datasets import make_multilabel_classification 
# import matplotlib.pyplot as plt 

# X,y=make_multilabel_classification(n_samples=100,n_features=20,n_classes=5,n_labels=3,random_state=42)

# print("Feature Shape: ",X.shape)
# print("Feature Shape: ",y.shape)

# plt.scatter(X[:,0],X[:,1],marker='o',c=y[:,0],edgecolor='k')

# plt.title("Random Multi-Label Classification Data")
# plt.xlabel("Feature1")
# plt.ylabel("Feature2")
# plt.show()

from sklearn.datasets import make_multilabel_classification 
import matplotlib.pyplot as plt 

X,y=make_multilabel_classification(n_samples=100,n_features=20,n_classes=5,n_labels=3,random_state=42)

print("Feature Shape: ",X.shape)
print("Feature Shape: ",y.shape)

plt.scatter(X[:,0],X[:,1],marker='o',c=y[:,0],edgecolors="k")
plt.title("Random Multi-Label Classification Data")
plt.xlabel("Fetaure1")
plt.ylabel("Feature2")
plt.show()