import pandas as pd

# Correct path for the test data file
file_path = "datasets/nsl kddest.txt"  # Ensure this path is correct

try:
    test_data = pd.read_csv("datasets/nsl kddest.txt", header=None)
    print("Test dataset loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Column names
column_names = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
    "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login",
    "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate",
    "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate",
    "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
    "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate", "dst_host_srv_serror_rate", "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate", "label", "difficulty_level"
]

# Assign the column names to the loaded data
if 'test_data' in locals():
    test_data.columns = column_names  # Apply column names to test data

    # One-hot encoding on test data (same as training data)
    test_data = pd.get_dummies(test_data, columns=["protocol_type", "service", "flag"])

    # Features aur Labels define karna
    X_test = test_data.drop(columns=["label", "difficulty_level"])
    y_test = test_data["label"]

    print("Test data and labels prepared successfully.")
