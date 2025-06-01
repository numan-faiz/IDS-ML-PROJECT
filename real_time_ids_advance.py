import joblib
import pandas as pd
from scapy.all import sniff, TCP, UDP, ICMP

# Load trained model and expected columns
model = joblib.load('trained_model.pkl')
model_columns = joblib.load('model_columns.pkl')  # List of all feature names used during training


# Prepare a blank dictionary with all model columns set to 0
def initialize_features():
    return {col: 0 for col in model_columns}


# Extract meaningful features from packet
def extract_features(packet):
    features = initialize_features()

    # Basic simulated mapping to trained features
    features['src_bytes'] = len(packet)  # Size of packet as src_bytes
    features['duration'] = 0  # Live packets won't have session duration info
    features['dst_bytes'] = 0  # Simplified assumption

    if TCP in packet:
        features['protocol_type_tcp'] = 1
    elif UDP in packet:
        features['protocol_type_udp'] = 1
    elif ICMP in packet:
        features['protocol_type_icmp'] = 1

    # Return as DataFrame in expected column order
    df = pd.DataFrame([features])
    df = df[model_columns]  # Ensure correct column order
    return df


# Predict attack or normal from each packet
def detect_intrusion(packet):
    try:
        input_data = extract_features(packet)
        prediction = model.predict(input_data)[0]
        if prediction != 'normal':
            print(f"⚠️ Intrusion Detected: {prediction}")
        else:
            print("✅ Normal traffic")
    except Exception as e:
        print("Error processing packet:", e)


# Start sniffing live network packets
print("🚀 Real-Time IDS started... (Press Ctrl+C to stop)")
sniff(prn=detect_intrusion, store=0)