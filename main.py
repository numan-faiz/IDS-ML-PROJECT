import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# 📌 Step 1: Load and preprocess dataset
print("🔄 Loading and preprocessing data...")
file_path = "datasets/KDDTrain+.txt"
column_names = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
    "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login",
    "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate",
    "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate",
    "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
    "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label", "difficulty_level"
]

# Load raw data
raw_data = pd.read_csv(file_path, header=None)
raw_data.columns = column_names

# Drop missing values
raw_data = raw_data.dropna()

# One-hot encode categorical columns
cleaned_data = pd.get_dummies(raw_data, columns=["protocol_type", "service", "flag"])

# Save cleaned data (optional)
cleaned_data.to_csv("datasets/cleaned_data.csv", index=False)

# 📌 Step 2: Train model
print("🧠 Training model...")
X = cleaned_data.drop(columns=["label", "difficulty_level"])
y = cleaned_data["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and columns
joblib.dump(model, "trained_model.pkl")
joblib.dump(X_train.columns.tolist(), "model_columns.pkl")

# 📌 Step 3: Evaluate using test dataset
print("📊 Evaluating model on test dataset...")
test_data = pd.read_csv("datasets/nsl kddest.txt", header=None)
test_data.columns = column_names

X_test_raw = test_data.drop(columns=["label", "difficulty_level"])
y_test = test_data["label"]
X_test_encoded = pd.get_dummies(X_test_raw)

# Align test data columns with training
trained_columns = joblib.load("model_columns.pkl")
for col in trained_columns:
    if col not in X_test_encoded.columns:
        X_test_encoded[col] = 0
X_test_encoded = X_test_encoded[trained_columns]

# Predictions
predictions = model.predict(X_test_encoded)

# Known Threat Detection - Alerts for known attacks
known_attack_types = ["neptune", "smurf", "back", "ipsweep", "nmap", "normal"]
for attack in predictions:
    if attack in known_attack_types:
        print(f"✔️ Known Threat - {attack} detected!")
    else:
        print(f"🚨 ALERT: Unknown threat detected - {attack}")

# Save alerts to a CSV file
alerts = []
for attack in predictions:
    if attack in known_attack_types:
        alerts.append(f"✔️ Known Threat - {attack} detected!")
    else:
        alerts.append(f"🚨 ALERT: Unknown threat detected - {attack}")

# Write alerts to a CSV file
pd.DataFrame({'Alerts': alerts}).to_csv('attack_alerts.csv', index=False)
print("📁 All alerts have been saved to attack_alerts.csv")

# Results
print("\n🎯 Accuracy:", accuracy_score(y_test, predictions))
print("\n📊 Classification Report:\n", classification_report(y_test, predictions, zero_division=0))
print("\n🧩 Confusion Matrix:\n", confusion_matrix(y_test, predictions))

print("\n✅ IDS pipeline complete.")
