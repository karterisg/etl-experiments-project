import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import os       

df = pd.read_csv("data/clean_data.csv")


X = df[['Age']]
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)

mse = mean_squared_error(y_test, preds)

print("Predictions:", preds)
print("Mean Squared Error:", mse)
print("True values:", list(y_test))
print("Coefficient (slope):", model.coef_)
print("Intercept:", model.intercept_)


os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/salary_model.pkl")
print("Model saved as models/salary_model.pkl")
