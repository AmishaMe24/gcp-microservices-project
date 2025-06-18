# 🚀 GCP Microservices Project: Order Processing System

This project demonstrates a beginner-friendly, event-driven microservices architecture using **Google Cloud Pub/Sub**, **Cloud Run**, and **Docker**. It includes three independent microservices:

- 📦 **Order Service** – Accepts orders and publishes messages to Pub/Sub.
- 📊 **Inventory Service** – Listens for new orders and updates inventory.

---

## 🧱 Folder Structure

gcp-microservices-project/
├── order-service/
├── inventory-service/
├── notification-service/
└── README.md

Each microservice has its own `Dockerfile`, `main.py`, and `requirements.txt`.

---

## ✅ Prerequisites

- Google Cloud account with billing enabled
- Git + GitHub
- Docker Desktop installed
- Python 3.10+
- Google Cloud SDK installed (`gcloud`)
- Basic familiarity with HTTP & Python

---

## ⚙️ Step-by-Step Setup

### 1. 🚀 Clone the Repository

```bash
git clone https://github.com/<your-username>/gcp-microservices-project.git
cd gcp-microservices-project
```

### 2. 🛠 Initialize GCP Project
```bash
gcloud init
gcloud config set project <your-project-id>

gcloud services enable run.googleapis.com pubsub.googleapis.com artifactregistry.googleapis.com
```

### 3. 🐳 Create Container Registry
For each service:
```bash
cd order-service  # or inventory-service / notification-service

gcloud builds submit --tag gcr.io/<project-id>/order-service
Repeat this for all 3 services.
```

### 4. ☁️ Deploy Services to Cloud Run
```bash
gcloud run deploy order-service \
  --image gcr.io/<project-id>/order-service \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
Note the deployed URL for each service. Repeat for inventory-service and notification-service.
```

### 5. 🔔 Set Up Pub/Sub
```bash
gcloud pubsub topics create order-topic
Create push subscriptions for both subscriber services:

gcloud pubsub subscriptions create inventory-sub \
  --topic=order-topic \
  --push-endpoint=https://<inventory-service-url>/ \

gcloud pubsub subscriptions create notification-sub \
  --topic=order-topic \
  --push-endpoint=https://<notification-service-url>/ \
```

### 6. 🧪 Test the System
```bash
Send a test order:
curl -X POST https://<order-service-url>/order \
  -H "Content-Type: application/json" \
  -d '{"order_id": "001", "item_id": "X123", "user_id": "U001"}'
Then check logs:

gcloud logging read "resource.type=cloud_run_revision" --limit 50
```
