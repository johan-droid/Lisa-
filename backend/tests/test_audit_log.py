from app.core.audit_log import AuditLogger

def test_audit_log_stores_events():
    logger = AuditLogger()

    logger.log("stage_1", {"key": "value1"}, "test_channel")
    logger.log("stage_2", {"key": "value2"}, "test_channel", "task-123")

    logs = logger.get_logs()

    assert len(logs) == 2
    assert logs[0].stage == "stage_1"
    assert logs[0].channel == "test_channel"
    assert logs[1].stage == "stage_2"
    assert logs[1].task_id == "task-123"
