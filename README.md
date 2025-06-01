# 🚨 Anomaly-Based Intrusion Detection System using Machine Learning

This project aims to detect network intrusions (known and unknown) using a Machine Learning approach. It uses the **NSL-KDD** dataset and a **Random Forest Classifier** for high-accuracy anomaly detection.

---

## 📁 Dataset

We used the **NSL-KDD Dataset** – an improved version of KDD Cup 1999. It contains labeled network traffic:  
- Normal  
- DoS, DDoS  
- Probe  
- R2L, U2R  
- SQL Injection

Dataset Source: https://www.unb.ca/cic/datasets/nsl.html

---

## 🧠 Machine Learning Model

- **Algorithm**: Random Forest Classifier  
- **Training Split**: 80% train / 20% test  
- **Accuracy Achieved**: **96.8%**  
- **Precision**: 95.4%  
- **Recall**: 94.3%  
- **F1-Score**: 94.8%

---

## ⚙️ Tools & Technologies

- Python 3  
- Pandas, NumPy  
- Scikit-learn  
- Flask (Web Interface)  
- HTML/CSS (Dashboard UI)

---

## 🚀 How to Run (Local Machine)

1. Clone this repository:
```bash
git clone https://github.com/numan-faiz/IDS-ML-PROJECT.git
cd IDS-ML-PROJECT
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the web app:
```bash
python app.py
```

4. Open browser:
```
http://127.0.0.1:5000/
```

---

## 📊 Results Snapshot

- Real-time web-based IDS interface  
- Processes network packets and alerts in < 100ms  
- Low false positives  
- High detection accuracy

---

## 📌 Project Structure

```
IDS-ML-PROJECT/
├── app.py
├── model_training.py
├── model.pkl
├── dataset.csv
├── templates/
├── static/
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Team Members
- Numan Faiz  

---

## 📧 Contact

If you have questions, feel free to reach out.
