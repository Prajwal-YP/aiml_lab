import pandas as pd

df = pd.read_csv("lab3ds.csv")

concepts = (df.iloc[:,:-1]).values.tolist()
targets  = (df.iloc[:,-1]).values.tolist()

specific_h = ['0' for i in range(len(concepts[0]))]
general_h = [['?' for i in range(len(concepts[0]))] for i in range(len(concepts[0]))]

for i,instance in enumerate(concepts):
    if targets[i]=='Yes':
        for x in range(len(specific_h)):
            if specific_h[x]=='0':
                specific_h[x]=instance[x]
            elif specific_h[x]!=instance[x]:
                specific_h[x]='?'
                general_h[x][x]='?'
    if targets[i]=='No':
        for x in range(len(specific_h)):
            if specific_h[x]!=instance[x]:
                general_h[x][x]=specific_h[x]
            else:
                general_h[x][x]='?'

unknown=['?','?','?','?','?','?']
i = ['0' for i in general_h if i==unknown]
for x in range(len(i)):
    general_h.remove(unknown)
    
print(specific_h)
print(general_h)