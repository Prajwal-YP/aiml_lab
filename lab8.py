import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score

df = pd.read_csv("iris.csv", names=["sepallength","sepalwidth","petallength","petalwidth"])
x = df.iloc[:,:-1]
y = df.iloc[:,-1]
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.1)

classifier = KNeighborsClassifier(n_neighbors=5).fit(x, y)
ypred = classifier.predict(xtest)

i=0
print("%-25s %-25s %-25s"%("LABEL","PREDICTION","CORRECT/WRONG"))
for label in ytest:
    print("%-25s %-25s "%(label,ypred[i]),end="")
    if(label==ypred[i]):
        print("%-25s"%("Correct"))
    else:
        print("%-25s"%("Wrong"))
print("CONFUSION MATRIX :")
print(confusion_matrix(ytest, ypred))
print("ACCURACY SCORE : ",accuracy_score(ytest, ypred))