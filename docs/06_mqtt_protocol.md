# MQTT Protocol Layer

MQTT is Lisa's optional lightweight event bus.

It reduces backend polling and makes chat updates, brain loop status, DevShell output, and nightly progress easier to stream.

---

## 1. MQTT Role

MQTT is for:

- Task status events.
- Brain loop events.
- DevShell terminal output.
- Eval progress.
- Worker heartbeats.
- Nightly harness events.
- Telegram notification pipeline events.

MQTT is not for:

- Secrets.
- Source of truth.
- Large files.
- Full prompts.
- Raw private memory.
- Audit-log-only storage.

Postgres/SQLite remains the source of truth.

---

## 2. Topic Structure

```txt
lisa/{env}/chat/{channel}/{chat_id}/events
lisa/{env}/tasks/{task_id}/status
lisa/{env}/tasks/{task_id}/events
lisa/{env}/brains/planner/in
lisa/{env}/brains/planner/out
lisa/{env}/brains/feasibility/in
lisa/{env}/brains/feasibility/out
lisa/{env}/brains/ranker/in
lisa/{env}/brains/ranker/out
lisa/{env}/devshell/{session_id}/status
lisa/{env}/devshell/{session_id}/terminal/out
lisa/{env}/devshell/{session_id}/terminal/exit
lisa/{env}/nightly/events
lisa/{env}/system/health/{component}
```

---

## 3. Event Payload

```json
{
  "event_id": "evt_001",
  "task_id": "task_001",
  "source": "planner",
  "event_type": "PLAN_CREATED",
  "active_brain": "PLANNER_ACTIVE",
  "risk_level": "P1",
  "payload": {},
  "created_at": "datetime"
}
```

---

## 4. MQTT Disabled Mode

MQTT must be optional.

If MQTT is disabled:

- Internal event dispatch must still work.
- Telegram notifications must still work.
- Planning loop must still work.
- Audit logs must still be written.

Config:

```env
MQTT_ENABLED=false
MQTT_BROKER_HOST=localhost
MQTT_BROKER_PORT=1883
MQTT_ENV=dev
MQTT_USERNAME=
MQTT_PASSWORD=
```

---

## 5. Security Rules

- Do not publish secrets.
- Do not retain sensitive messages.
- Do not use MQTT as the audit log.
- Do not allow UI/user clients broad wildcard access.
- Validate payloads with JSON schema.
- Sanitize terminal output before publishing.

---

## 6. Required Files

```txt
backend/app/messaging/mqtt_client.py
backend/app/messaging/mqtt_topics.py
backend/app/messaging/mqtt_payloads.py
backend/app/mux/mqtt_mux.py
backend/app/schemas/mqtt_event.schema.json
```

---

## 7. Tests

Required tests:

- MQTT payload validates.
- MQTT-disabled mode works.
- Sensitive values are redacted.
- Task status event is emitted.
- Brain event is emitted.
- DevShell output is summarized.
