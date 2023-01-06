import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

df = pd.read_csv("./practise/tennis.csv")

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

obj = LabelEncoder()
tmp={}
for key in x.keys():
    tmp[key] = list(obj.fit_transform(x[key]))
x = pd.DataFrame(tmp)
y = obj.fit_transform(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.1)

classifier = GaussianNB()
classifier.fit(x_train,y_train)

print("ACUURACY SCORE:\t",accuracy_score(y_test,classifier.predict(x_test))*100)

new_test = pd.read_csv("./practise/question.csv")
tmp={}
for key in new_test.keys():
    tmp[key]=list(obj.fit_transform(new_test[key]))
new_test = pd.DataFrame(tmp)
print("ANSWER: ",classifier.predict(new_test))