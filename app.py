from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "company": "UTA Retail Corporation",
        "message": "Welcome to UTA Retail",
        "version": "1.0"
    })

@app.get("/health")
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
