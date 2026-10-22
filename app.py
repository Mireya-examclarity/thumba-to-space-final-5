from flask import Flask, send_from_directory
import os

# thumba to space > my stardance project
# kilimanoor to thumba to space theme

app = Flask(__name__)
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

@app.route("/")
def home():
    return send_from_directory(BASE, 'index.html')

# To check the health of the app(DOCTOR COME IN HERE!)
@app.route("/health")
def health():
    # simple check if app running
    return {"status": "running"}

@app.route("/api/mission")
def mission():
    # my mission data
    data = {
        "mission": "Kilimanoor -> Thumba -> Space",
        "status": "READY",
        "launch_site": "Thumba, Kerala",
        "destination": "Low Earth Orbit"
    }
    return data

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print("starting thumba to space app on port", port)
    app.run(host="0.0.0.0", port=port)
