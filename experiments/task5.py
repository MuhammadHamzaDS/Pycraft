import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Training data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)   # X ko 2D banana hota hai
y = np.array([2, 4, 6, 8, 10])

# Model create & train
model = LinearRegression()
model.fit(X, y)

# Predict for x = 10
x_new = np.array([[10]])
y_pred = model.predict(x_new)
print("Prediction for x=10:", y_pred[0])

# Visualization
plt.scatter(X, y, color="blue", label="Data points")
plt.plot(X, model.predict(X), color="red", label="Regression line")
plt.scatter(x_new, y_pred, color="green", marker="x", s=100, label=f"Prediction (10, {y_pred[0]:.2f})")

plt.xlabel("X")
plt.ylabel("y")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()
