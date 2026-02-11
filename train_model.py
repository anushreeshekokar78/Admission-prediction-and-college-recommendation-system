import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib

# Load cleaned dataset
data = pd.read_csv("clean_dataset.csv")

# Separate features and target
X = data.drop("Chance", axis=1)
y = data["Chance"]

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------- Linear Regression (baseline) ----------------
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_score = r2_score(y_test, lr_pred)

print("Linear Regression R2 Score:", round(lr_score, 3))

# ---------------- Random Forest (final model) ----------------
rf = RandomForestRegressor(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_score = r2_score(y_test, rf_pred)

print("Random Forest R2 Score:", round(rf_score, 3))

# Save final model
joblib.dump(lr, "admission_model.pkl")


print("Model saved as admission_model.pkl")
