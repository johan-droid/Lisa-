import pytest
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

@pytest.mark.asyncio
async def test_e2e_telegram_autopilot_inspection():
    from fastapi.testclient import TestClient
    from app.main import app
    client = TestClient(app)
    payload = {
        "message": {
            "message_id": 999,
            "text": "Autopilot mode: inspect this repo and prepare a safe plan",
            "chat": {"id": 1},
            "from": {"id": 1, "username": "tester"}
        }
    }
    response = client.post("/webhooks/telegram", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "reply" in data
    reply = data["reply"]
    # Check enhanced metadata response parts
    assert "Autopilot Mode Completed" in reply
    assert "Metadata" in reply
    assert "Mode: autopilot" in reply
    assert "Simulated LocalSandboxSimulator" in reply
