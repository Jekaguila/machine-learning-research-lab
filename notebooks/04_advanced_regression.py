from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston

data = load_boston()

X = data.data
y = data.target

model = RandomForestRegressor()

model.fit(X,y)
