from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Activer l’export des métriques
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "<h1>Bonjour 👋</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

