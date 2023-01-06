import numpy as np

x = np.array( ([1,2,4,5],[2,3,9,5],[4,6,1,8]), dtype=float)
y = np.array( ([78],[89],[98]), dtype=float)
x = x/np.amax(x,axis=0)
y = y /100

enoch = 3000
lr    = 5

inputlayers  = 4
hiddenlayers = 5
outputlayers = 1

wh   = np.random.uniform(size=(inputlayers,hiddenlayers))
bh   = np.random.uniform(size=(1,hiddenlayers))
wout = np.random.uniform(size=(hiddenlayers,outputlayers))
bout = np.random.uniform(size=(1,outputlayers))

def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivativeSigmoid(x):
    return x*(1-x)

for i in range(enoch):
    # Forward Propogation
    h = sigmoid( np.dot(x,wh) + bh)
    o = sigmoid( np.dot(h,wout) + bout)
    
    # Backward Propogation
    EO      = y-o
    dOutput = EO * derivativeSigmoid(o)
    EH      = np.dot(dOutput,wout.T)
    dHidden = EH * derivativeSigmoid(h)
    
    wh   += np.dot(x.T,dHidden) * lr
    wout += np.dot(h.T,dOutput) * lr
print("ACTUAL OUTPUT:\t",y)
print("PREDICTED OUTPUT:\t",o)

    
 