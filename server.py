from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "status": "Beacon Prospecta Online"
    })


@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "Beacon Prospecta"
    })


@app.post("/discover")
def discover():
    data = request.get_json(force=True)

    agency_url = data.get(
        "agency_url",
        ""
    )

    return jsonify({
        "agency_url": agency_url,
        "status": "prospect_discovery_ready"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )
