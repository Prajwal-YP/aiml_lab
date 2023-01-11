import pandas as pd 
import numpy as np
from numpy import log2

def entropy(df):
    target = df.keys()[-1]
    labels = np.unique(df[target])
    entropy = 0
    for label in labels:
        fraction = len(df[df[target]==label])/len(df)
        entropy += -fraction * log2(fraction)
    return entropy

def attrEntropy(df,attr):
    target = df.keys()[-1]
    labels = np.unique(df[target])
    variables = np.unique(df[attr])
    entropy2=0
    for variable in variables:
        entropy1=0
        for label in labels:
            num = len(df[df[attr]==variable][df[target]==label]) 
            den = len(df[df[attr]==variable])
            fraction1 = num/(den+eps)
            entropy1 += -fraction1 * log2(fraction1+eps)
        fraction2 = len(df[df[attr]==variable])/len(df)
        entropy2 += -fraction2*entropy1
    return abs(entropy2)


def findWinner(df):
    IG=[]
    for attr in df.keys()[:-1]:
        IG.append(entropy(df)-attrEntropy(df,attr))
    return df.keys()[:-1][np.argmax(IG)]

def getSubtable(df,node,variable):
    return df[df[node]==variable].reset_index(drop=True)

def build(df,tree=None):
    node = findWinner(df)
    variables =np.unique(df[node])
    if tree==None:
        tree={}
        tree[node]={}
    for variable in variables:
        subtable = getSubtable(df,node,variable)
        if len(np.unique(subtable['play']))==1:
            tree[node][variable]=subtable["play"][0]
        else:
            tree[node][variable]=build(subtable)
    return tree

eps = np.finfo(float).eps
df = pd.read_csv("./practise/tennis.csv")
tree = build(df)
import pprint
pprint.pprint(tree)

test={'Outlook':'Sunny','Temperature':'Hot','Humidity':'High','Wind':'Weak'}
def func(test, tree):
    attr= next(iter(tree))
    if test[attr] in tree[attr].keys():
        if type(tree[attr][test[attr]])==dict:
            return func(test,tree[attr][test[attr]])
        else:
            return tree[attr][test[attr]]
    else:
        return None
ans=func(test,tree)
print("--------------------------------------")
print("Will he play tennis? :",ans)
