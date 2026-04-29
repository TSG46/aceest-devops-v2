from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ACEest Fitness App Running"

@app.route("/members")
def members():
    return jsonify(["Ravi", "Anita", "John", "Priya"])  # ✅ Added Priya

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)