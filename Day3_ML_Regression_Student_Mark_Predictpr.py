# Step 1 - Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

#Step 2: Loading Simple data
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Scores': [20, 23, 35, 40, 50, 60, 62, 70, 80, 85]
}
df = pd.DataFrame(data)
print(df)

#Step 3: Visualize the data
plt.scatter(df['Hours'], df['Scores'], color='blue')
plt.title('Study Hours vs Student Score')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.show()

#Step 4: Prepare data for Model
X = df[['Hours']]  # independent variable
y = df['Scores']   # dependent variable

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#Step 5 Training Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)


#Step 6 Predict and Evaluate
y_pred = model.predict(X_test)

results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(results)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("R² Score:", r2)

#Step 7 Visualize Regression Line]
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.title('Regression Line: Study Hours vs Score')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.show()

#Step 8 Predict thr New Input
hours = np.array([[9.5]])
predicted_score = model.predict(hours)
print(f"Predicted Score for {hours[0][0]} study hours is: {predicted_score[0]:.2f}")


