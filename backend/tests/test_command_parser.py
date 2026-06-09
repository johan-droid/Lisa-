from app.chat.command_parser import CommandParser

def test_command_parser_standard():
    parser = CommandParser()
    res = parser.parse("/lisa plan this is a test")
    assert res.command == "/lisa plan"
    assert res.args == "this is a test"
    assert res.is_valid

def test_command_parser_nl():
    parser = CommandParser()
    res = parser.parse("lisa plan this: fix the db")
    assert res.command == "/lisa plan"
    assert res.args == "fix the db"
    assert res.is_valid

def test_command_parser_invalid():
    parser = CommandParser()
    res = parser.parse("hello world")
    # Our new implementation sets is_valid=True with 'unknown' command to let JobRouter handle it
    assert res.is_valid
    assert res.command == "unknown"
