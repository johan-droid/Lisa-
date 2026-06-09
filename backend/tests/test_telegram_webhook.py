from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_telegram_webhook_route():
    payload = {
        "message": {
            "message_id": 123,
            "chat": {"id": 456},
            "from": {"id": 789, "username": "user"},
            "text": "/lisa plan build auth system",
            "date": 1234567890
        }
    }
    response = client.post("/webhooks/telegram", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"
    assert "Plan created for" in data["reply"]
    assert data["task_id"] is not None
    assert data["approval_required"] is False
    assert data["risk_level"] == "planning_only"

def test_telegram_webhook_blocked_command():
    payload = {
        "message": {
            "message_id": 124,
            "chat": {"id": 456},
            "from": {"id": 789, "username": "user"},
            "text": "/lisa run rm -rf /",
            "date": 1234567891
        }
    }
    response = client.post("/webhooks/telegram", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "blocked"
    assert "Destructive execution is blocked" in data["reply"]
    assert data["risk_level"] == "execution_blocked"
