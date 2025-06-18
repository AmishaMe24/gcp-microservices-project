from flask import Flask, request
import json
import base64

app = Flask(__name__)

@app.route("/", methods=["POST"])
def update_inventory():
    envelope = request.get_json()
    if not envelope or not envelope.get("message"):
        return "Bad Request", 400
    
    payload = json.loads(base64.b64decode(envelope["message"]["data"]).decode("utf-8"))
    print(f"Inventory updated for item: {payload['item_id']}")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
