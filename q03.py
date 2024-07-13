from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt
# import numpy as np

diabetes = load_diabetes()

X = diabetes.data[:,None,8]
Y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

plt.scatter(X_test,y_test,label="Data Points")
plt.plot(X_test,y_pred,label="Fitted Line")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.title("Question 3. Linear Regression")
plt.legend()
plt.show()