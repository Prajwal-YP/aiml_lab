from sklearn.cluster import KMeans
from sklearn.preprocessing  import StandardScaler
from sklearn.mixture import GaussianMixture
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = load_iris()
x = pd.DataFrame(dataset.data,columns=["speal_length","speal_width","petal_length","petal_width"])
y = pd.DataFrame(dataset.target,columns=["target"])

plt.figure(figsize=(8,5))
colormap=np.array(["red","lime","blue"])

plt.subplot(1,3,1)
plt.scatter(x.petal_length,x.petal_width,c=colormap[y.target],s=20)
plt.title("BEFORE CLUSTERING")

plt.subplot(1,3,2)
classifier = KMeans(n_clusters=3).fit(x)
ypred = classifier.predict(x) 
plt.scatter(x.petal_length,x.petal_width,c=colormap[ypred],s=20)
plt.title("KMEANS CLUSTERING")

plt.subplot(1,3,3)
#scaler = StandardScaler().fit(x)
xsa = StandardScaler().fit(x).transform(x)
xs = pd.DataFrame(xsa,columns=x.columns)
classifier = GaussianMixture(n_components=3).fit(xs)
ypred = classifier.predict(xs)
plt.scatter(x.petal_length,x.petal_width,c=colormap[ypred],s=20)
plt.title("GMM with EM CLUSTERING")
