import os
from joblib import dump
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

X, y = make_regression(n_samples=100, n_features=2, noise=0.1)
model = LinearRegression()
model.fit(X, y)

os.makedirs("models", exist_ok=True)
dump(model, "models/model.joblib")
