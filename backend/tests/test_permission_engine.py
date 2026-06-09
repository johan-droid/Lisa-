from app.policy_os.permission_engine import PermissionEngine
from app.policy_os.risk_engine import RiskEngine
from app.chat.command_parser import CommandParser

def test_permission_engine_blocks_destructive():
    parser = CommandParser()
    risk_engine = RiskEngine()
    permission_engine = PermissionEngine()

    # Needs a real command structure, but our parser doesn't natively parse "/lisa run rm -rf /"
    # let's mock the parsed command or use a supported structure
    # Let's say user types "/lisa plan rm -rf /" -> it's destructive
    cmd = parser.parse("/lisa plan rm -rf /")
    risk = risk_engine.evaluate(cmd)
    assert risk == "execution_blocked"

    permission = permission_engine.check(cmd, risk)
    assert not permission["allowed"]
    assert permission["reason"] == "Destructive execution is blocked in Phase 1"

def test_permission_engine_allows_planning():
    parser = CommandParser()
    risk_engine = RiskEngine()
    permission_engine = PermissionEngine()

    cmd = parser.parse("/lisa plan build auth")
    risk = risk_engine.evaluate(cmd)
    assert risk == "planning_only"

    permission = permission_engine.check(cmd, risk)
    assert permission["allowed"]
