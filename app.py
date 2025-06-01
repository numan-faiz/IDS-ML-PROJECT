import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template

# Flask app create karna
app = Flask(__name__)

@app.route('/')
def home():
    # CSV file ko read karo (attack_alerts.csv ko path de dena)
    alerts_df = pd.read_csv('attack_alerts.csv')

    # Known aur Unknown threats ko count karna
    known_threats = ['normal', 'neptune', 'smurf', 'back', 'ipsweep', 'nmap']
    unknown_threat_count = 0
    known_threat_count = 0

    # Alerts ko loop karke count karenge
    for alert in alerts_df['Alerts']:
        if any(threat in alert for threat in known_threats):
            known_threat_count += 1
        else:
            unknown_threat_count += 1

    # Bar chart banane ke liye data
    labels = ['Known Threats', 'Unknown Threats']
    counts = [known_threat_count, unknown_threat_count]

    # Graph plot karna
    plt.bar(labels, counts, color=['green', 'red'])
    plt.xlabel('Threat Types')
    plt.ylabel('Count')
    plt.title('Known vs Unknown Threats Detected')

    # Graph ko save karna static/images/ mein
    graph_path = 'static/images/attack_graph.png'
    plt.savefig(graph_path)
    plt.close()  # Close the plot to free up memory

    # Flask render_template se HTML page render karenge aur graph ka path pass karenge
    return render_template('index.html', graph_path=graph_path)

if __name__ == '__main__':
    app.run(debug=True)
