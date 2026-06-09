from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_slack_webhook():
    payload = {
        "event": {
            "type": "message",
            "client_msg_id": "msg-123",
            "user": "U123",
            "channel": "C123",
            "text": "/lisa plan do something"
        }
    }
    response = client.post("/webhooks/slack/events", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"

def test_whatsapp_webhook():
    payload = {
        "entry": [{
            "changes": [{
                "value": {
                    "messages": [{
                        "id": "msg-123",
                        "from": "1234567890",
                        "text": {"body": "/lisa plan stuff"}
                    }]
                }
            }]
        }]
    }
    response = client.post("/webhooks/whatsapp", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
