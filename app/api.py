from flask import Flask, request, jsonify
from logger import log_event

app = Flask(__name__)

@app.route("/")
def home():
    return "Unified Logging System API is running!"

@app.route("/log", methods=["POST"])
def create_log():

    data = request.json

    log_event(
        module=data["module"],
        event=data["event"],
        data=data["data"]
    )

    return jsonify({
        "message": "Log stored successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)
