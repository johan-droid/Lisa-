from fastapi import FastAPI
from app.routes import health, telegram, slack, whatsapp
from app.config import settings

app = FastAPI(title="Lisa", version="0.1.0")

app.include_router(health.router)
app.include_router(telegram.router)
app.include_router(slack.router)
app.include_router(whatsapp.router)

# Provide aliases for old test structures
# the router prefix already contains "/slack" "/whatsapp" "/telegram" so we just need /webhooks
app.include_router(telegram.router, prefix="/webhooks")
app.include_router(slack.router, prefix="/webhooks")
app.include_router(whatsapp.router, prefix="/webhooks")

@app.get("/")
def read_root():
    return {"status": "ok", "app": "Lisa"}
