# Lightweight Deployment

Lisa must be able to run on a small instance first.

The initial target is a single lightweight backend with optional MQTT and a simple database.

---

## 1. Target Profile

```txt
1 vCPU
512 MB - 1 GB RAM
single backend container
SQLite for development
Postgres for production
optional MQTT broker
no heavy always-on research process
```

---

## 2. Recommended MVP Stack

```txt
Backend: FastAPI
Database: SQLite for local/dev, Postgres for production
Messaging: Optional MQTT
Chat: Telegram Bot, Slack App, WhatsApp Cloud API
LLM: Provider-configurable router
RAG: Lightweight trust-zoned document store
Sandbox: local isolated workspace first, container later
```

---

## 3. Deployment Rules

- Do not run every brain as a separate service initially.
- Do not load high-context models for every task.
- Do not run Research Brain continuously.
- Do not keep DevShell sessions alive forever.
- Do not store huge raw logs in DB.
- Do not send huge outputs over chat.
- Use summaries and safe artifact references.
- Keep MQTT optional.
- Keep deterministic stubs for tests if no LLM is configured.

---

## 4. Environment Variables

```env
APP_ENV=dev
APP_NAME=Lisa
DATABASE_URL=sqlite:///./lisa.db

LLM_PROVIDER=
LLM_MODEL=
LLM_API_KEY=
LLM_BASE_URL=

MQTT_ENABLED=false
MQTT_BROKER_HOST=localhost
MQTT_BROKER_PORT=1883
MQTT_ENV=dev
MQTT_USERNAME=
MQTT_PASSWORD=

TELEGRAM_BOT_TOKEN=
TELEGRAM_WEBHOOK_SECRET=
TELEGRAM_ADMIN_CHAT_ID=

SLACK_BOT_TOKEN=
SLACK_SIGNING_SECRET=
SLACK_APP_TOKEN=

WHATSAPP_VERIFY_TOKEN=
WHATSAPP_ACCESS_TOKEN=
WHATSAPP_PHONE_NUMBER_ID=
WHATSAPP_APP_SECRET=

INTERNAL_API_TOKEN=
SANDBOX_ROOT=./sandbox_workspaces
MAX_LOOP_ITERATIONS=4
```

---

## 5. Process Model

Initial process model:

```txt
FastAPI app
  ├─ webhook routes
  ├─ internal task runtime
  ├─ planning loop
  ├─ notification engine
  ├─ optional MQTT publisher
  └─ lightweight background scheduler
```

Later process model:

```txt
FastAPI API
worker process
MQTT broker
sandbox runner
scheduler/nightly worker
```

Do not over-distribute too early.

---

## 6. Storage Model

Use database for:

- tasks
- task events
- plan packets
- scores
- approvals
- notifications
- audit logs
- memory metadata

Use artifacts for:

- large terminal output
- diffs
- full test logs
- RAG source docs
- MCP scan logs

---

## 7. Success Criteria

Lisa is lightweight-ready when:

- It starts as one backend service.
- Health route works.
- Telegram webhook works.
- Planning loop runs without external tools.
- MQTT disabled mode works.
- SQLite mode works.
- No heavy always-on brain process is required.
