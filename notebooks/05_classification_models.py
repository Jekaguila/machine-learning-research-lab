from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

data = load_iris()

X = data.data
y = data.target

model = RandomForestClassifier()

model.fit(X,y)
