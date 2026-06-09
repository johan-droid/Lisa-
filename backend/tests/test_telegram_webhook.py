from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_telegram_webhook_route():
    response = client.post("/webhooks/telegram")
    assert response.status_code == 200
