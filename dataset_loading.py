import pandas as pd

# Load the training dataset
file_path = "datasets/KDDTrain+.txt"  # Adjust the path if necessary
try:
    train_data = pd.read_csv("datasets/nsl kddest.txt", header=None)
    print("Training dataset loaded successfully.")
    print("First few rows of the dataset:")
    print(train_data.head())
except Exception as e:
    print(f"Error loading dataset: {e}")