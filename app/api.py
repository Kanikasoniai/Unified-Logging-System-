from flask import Flask, request, jsonify
from logger import log_event

app = Flask(__name__)

@app.route("/")
def home():
    return "Unified Logging System API is running!"

@app.route("/log", methods=["POST"])
def create_log():

    data = request.json

    required_fields = ["module", "event", "data"]

    for field in required_fields:

        if field not in data:

            return jsonify({
                "error": f"Missing field: {field}"
            }), 400

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