# ✅ data_preprocessing.py
import pandas as pd

# Step 1: Load the raw dataset
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

print("🔄 Loading dataset...")
data = pd.read_csv(file_path, header=None)
data.columns = column_names

# Step 2: Drop missing values (if any)
data = data.dropna()

# Step 3: One-hot encode categorical features
data = pd.get_dummies(data, columns=["protocol_type", "service", "flag"])

# Step 4: Save preprocessed data
data.to_csv("datasets/cleaned_data.csv", index=False)
print("✅ Data preprocessing complete. Saved as cleaned_data.csv")
