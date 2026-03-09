from sklearn.metrics import accuracy_score, confusion_matrix

predictions = model.predict(X)

accuracy_score(y,predictions)
