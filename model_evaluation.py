# ✅ model_evaluation.py
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Step 1: Column names (same as training)
column_names = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
    "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login",
    "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate",
    "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate",
    "srv_diff_host_rate", "dst_host_c                                        ount", "dst_host_srv_count",
    "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label", "difficulty_level"
]

# Step 2: Load test dataset
test_data = pd.read_csv("datasets/nsl kddest.txt", header=None)
test_data.columns = column_names
print("✅ Dataset loaded successfully.")

# Step 3: Prepare features and labels
X_test_raw = test_data.drop(columns=["label", "difficulty_level"])
y_test = test_data["label"]

# Step 4: One-hot encoding
X_test_encoded = pd.get_dummies(X_test_raw)

# Step 5: Load trained model and columns
model = joblib.load("trained_model.pkl")
trained_columns = joblib.load("model_columns.pkl")
print("✅ Model & training columns loaded successfully.")

# Step 6: Align test data with training columns
for col in trained_columns:
    if col not in X_test_encoded.columns:
        X_test_encoded[col] = 0

X_test_encoded = X_test_encoded[trained_columns]  # Reorder columns

# Step 7: Predict and evaluate
predictions = model.predict(X_test_encoded)

print("\n🎯 Accuracy:", accuracy_score(y_test, predictions))
print("\n📊 Classification Report:\n", classification_report(y_test, predictions, zero_division=0))
print("\n🧩 Confusion Matrix:\n", confusion_matrix(y_test, predictions))

