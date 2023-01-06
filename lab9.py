import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("tips.csv")

bill = np.array(df.total_bill)
tip  =np.array(df.tip)
mbill = np.mat(bill)
mtip  = np.mat(tip)

m = np.shape(mbill)
One = np.ones(m)
X = np.hstack((One.T,mbill.T))
sortIndex = X[:,1].argsort(0)
xsort = X[sortIndex][:,0]

def Kernal(point,xmat,k):
    m,n = np.shape(xmat)
    weights = np.mat(np.eye((m)))
    for j in range(m):
        diff = point - X[j]
        weights[j,j] = np.exp(diff*diff.T/(-2 * k**2))
    return weights

def localWeight(point,xmat,ymat,k):
    wei = Kernal(point,xmat,k)
    W = (X.T*(wei*X)).I * (X.T*(wei*ymat.T))
    return W

def localWeightRegression(xmat,ymat,k):
    m,n = np.shape(xmat)
    ypred = np.zeros(m)
    for i in range(m):
        ypred[i] = xmat[i] * localWeight(xmat[i],xmat,ymat,k)
    return ypred

ypred = localWeightRegression(X,mtip,0.5)
plt.scatter(bill,tip)
plt.plot(xsort[:,1],ypred[sortIndex],c="black")