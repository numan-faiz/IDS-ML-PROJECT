import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Load cleaned data
data = pd.read_csv("datasets/cleaned_data.csv")

# Step 2: Define features and target
X = data.drop(columns=["label", "difficulty_level"])
y = data["label"]

# Step 3: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

importances = model.feature_importances_
for feature, score in zip(X.columns, importances):
    print(f"{feature}: {score}")

# Step 5: Predict & evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# Step 6: Save model
joblib.dump(model, "trained_model.pkl")
joblib.dump(X_train.columns.tolist(), "model_columns.pkl")
print("✅ Model & columns saved.")


