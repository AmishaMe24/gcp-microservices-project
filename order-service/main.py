from fastapi import FastAPI, Request
from google.cloud import pubsub_v1
import os
import json

app = FastAPI()
publisher = pubsub_v1.PublisherClient()
PROJECT_ID = os.getenv("GCP_PROJECT")
TOPIC_PATH = publisher.topic_path(PROJECT_ID, "order-topic")

@app.post("/order")
async def create_order(request: Request):
    order_data = await request.json()
    data = json.dumps(order_data).encode("utf-8")
    future = publisher.publish(TOPIC_PATH, data=data)
    return {"message": "Order received", "id": future.result()}
