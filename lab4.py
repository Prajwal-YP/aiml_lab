import pandas as pd
import numpy as np
from pprint import pprint

def entropy(df):
    entropy = 0
    targets = df.iloc[:,-1]
    targets,counts = np.unique(targets,return_counts=True)
    print(targets,counts)
    for i in targets:
        

def findWinner(df):
    IG = []
    for key in df.keys()[:-1]:
        IG.append(entropy(df)-attrEntropy(df,key))
    return df.keys()[:-1][np.argmax(IG)]

def build(df,tree=None):
    node = findWinner(df)
    if tree==None:
        tree={}
        tree[node]={}
    for variable in variables:
        subtable = getSubtable(df,node,variable)
        if len(np.unique(subtable['play']))==1:
            tree[node][variable]=subtable['play'][0]
        else:
            tree[node][variable]=build(subtable)
    return tree

eps = np.finfo(float).eps
df = pd.read_csv("tennis.csv")
tree = build(df)
pprint(tree)